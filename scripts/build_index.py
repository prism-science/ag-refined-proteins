#!/usr/bin/env python3
"""Build index.json, MANIFEST.sha256, targets/<ID>/README.md and the results table in README.md from targets/.

Every number written here is read from a file in this repository (the release-time validation under
targets/<ID>/validation/release/, the campaign records under targets/<ID>/refinement/ and targets/<ID>/ledger/,
and the RCSB entry record under targets/<ID>/deposited/). Nothing is typed in by hand except the caveat text in
CAVEATS, each sentence of which cites the campaign decision row (D-number) it comes from.

    python3 scripts/build_index.py            # rebuild everything
    python3 scripts/build_index.py --check    # exit 1 if any generated file would change
"""
from __future__ import annotations

import csv
import hashlib
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ROOT / "targets"
README = ROOT / "README.md"
TABLE_BEGIN, TABLE_END = "<!-- results-table:begin -->", "<!-- results-table:end -->"

# Caveats are the campaign's own, one bullet per decision row (docs/campaign/deviations.md). Keep them short.
CAVEATS: dict[str, list[str]] = {
    "3QUE": [
        "The held-back report half, the unbiased estimate (PROTOCOL §3.6), improved much less than the full set. Ledger values, "
        "previous record (2026-08-28) → this model: full 0.25891 → 0.25246, report 0.26441 → 0.26334, select 0.25365 → 0.24205 "
        "(independent scorer: full 0.25968 → 0.25330, report 0.26517 → 0.26420). Most of the full-set gain sits on the select half, "
        "the half the search consults (D519).",
        "This model is the graph search's third 3QUE promotion on 2026-10-03 (`3QUE.graph-weekend-20261002d`, generation 6). The one "
        "before it (generation 4, D520) had report 0.25983, better on both halves than the 2026-08-28 record; this promotion lowered "
        "full by 0.0004 and raised report by 0.0035. It passed the promotion rules (report inside 2σ_report of the record it replaced); "
        "no decision row covers it yet. The first promotion (generation 2, D518) had made report worse (0.26725).",
        "The gain is water sites transferred from 9MHB, the 1.65 Å isomorphous p38α entry, combined in credited batches against "
        "matched null arms (D518, D520). Waters 15 → 46 against the previous release (deposited 14).",
        "Rotamer outliers are above the campaign's 1.5 % cap: 4.29 % at release time (phenix.molprobity; previous released model "
        "3.96 %, deposited 7.59 %). The campaign records 3.96 % for both records and calls it pre-existing (D518, D520).",
        "The deposited header R-free (0.311) is a REFMAC number; Phenix recomputes the same model at 0.287 on these flags (D008). "
        "Only the recomputed value is comparable.",
        "Most of the gain over the deposited file is Phenix re-refinement of a REFMAC-refined model (TLS, weight optimisation); the "
        "campaign's own credited changes are water edits: three added, two removed, water occupancies refined (D421/D485), then the "
        "9MHB transfer waters.",
        "The model carries no riding hydrogens: adding them was tested and rejected at 2.7 Å (D490).",
    ],
    "3TC7": [
        "The held-back report half did not improve with the 2026-10-03 promotions: ledger 0.16726 → 0.16769 (independent scorer "
        "0.16730 → 0.16772, +1.6σ_report, D519). The full-set gain 0.17276 → 0.17161 is carried by the select half "
        "(0.17815 → 0.17545), the half the search consults. Each promotion passed the promotion rules; D519 proposes a cumulative "
        "report bound that would have refused the second one.",
        "Rotamer outliers 1.59 % at release time (campaign monitor 1.58 %) exceed the campaign's 1.5 % cap (D517); the previous "
        "released model had 0.8 %. Depositable by ordinary standards, not by the campaign's own bar.",
        "What the 2026-10-03 promotions added: qFit alternate conformers at A175, A250 and A30 in a credited batch "
        "(`3TC7.graph-weekend-20261002c` generation 2, D517), then a second credited batch (generation 3, node N3.0, D519).",
        "The largest single credited change on record is riding hydrogens on a model that never had any (no new parameters), −0.011 on every "
        "R-free set with the R-free − R-work gap unchanged (D488). Earlier credits added waters and alternate conformations.",
        "The refinement protocol uses a fixed ADP weight (wxu_scale 0.03) because Phenix's weight optimiser widens the R-gap on the "
        "hydrogen-bearing model (D491/D496); a re-refinement with default weights will not reproduce the R-gap. The credit bar (σ_select) "
        "quoted below is from the noise floor re-measured under that protocol.",
        "Campaign records after 2026-09-28 report a lower R-free on this target from manual Coot–refinement alternation (0.1583, D512). "
        "That model was never scored on the frozen flags and no copy of it was found (E039); plain Phenix water picking on these flags "
        "reaches 0.1702 and fails the R-gap gate. It is not in this release.",
    ],
    "7KR0": [
        "MolProbity rotamer outliers and the altloc-aware clashscore of this model exceed the campaign's own frozen caps (1.5 % and 5.0); the "
        "deposited multiconformer model already exceeds the clashscore cap by construction (D451, D474). Depositable by ordinary standards, not by the campaign's own bar.",
        "The changes carried by this model are two waters removed plus three 15-macro-cycle refinement passes credited at 2.1σ, 2.0σ and 2.5σ (D489, D493, D494): "
        "continued refinement, not remodelling. The deposited model was already near-optimal as a single-conformer representation.",
        "Three credited cycles on record (run `7KR0.exp_sw_distill`) belong to the ensemble-distillation line, which judged its candidates against "
        "its own base and was closed as a negative result (D463, D466); they are not in this model's lineage.",
        "Ensemble representations of the same data score far lower (44PS, the six-conformation model of Passmore et al. 2026 on this dataset, "
        "0.0657 on these flags; the campaign's own six-copy models 0.088–0.092). They are a second representation, not a deliverable "
        "(PROTOCOL §18.1); the campaign's are released separately in `representations/7KR0/`.",
    ],
    "4QO4": [
        "Credited but still worse than the deposited file recomputed on these flags: Phenix's default re-refinement of this CNS-refined model costs "
        "0.037 in R-free and the run recovers 0.026 of it. The campaign reports this as a program artifact, not a result (D509, PROTOCOL §6).",
    ],
    "6UDY": [
        "The single credit recovered cycle-0 drift on an unconverged CNS-era model (D506). The model beats the re-refined baseline on the "
        "consulted half only; on the full and report sets the difference is within its wide noise floor (σ_full 0.0077), and the report half is "
        "worse than the baseline's (D508).",
    ],
    "6CDX": [
        "The phase-2 result (D509): waters added and removed in two credited cycles, then alternate conformations at A5, A34 and B20 plus one water "
        "kept from the surviving half of a bisected cycle 7 (un-credited, within noise). The released model is that cycle-7 base, the best of the run. "
        "The whole-model geometry monitor flagged it (rotamer outliers and clashscore above the frozen caps); the release MolProbity numbers above show the clashscore.",
    ],
    "1N7E": ["One credit: five waters removed. −0.003 beyond re-refinement at 3σ (D509)."],
    "9D5U": ["Two credits, waters removed and added; −0.002 beyond re-refinement at 6σ. The run stopped with its escape ladder exhausted (D510)."],
    "7R2H": [
        "The released model is one Phenix re-refinement of the deposited file; nothing the agent proposed has been credited yet (E044). "
        "The −0.026 over the deposited file is the campaign's re-refinement protocol on its own, and it is mostly an ADP-model change: the "
        "deposited file carries ANISOU on 1 258 of its 1 597 non-hydrogen atoms (the isotropic ones are the 335 waters and the DMSO), the campaign's protocol refines "
        "every non-hydrogen atom anisotropically. R-work falls further than R-free, so the R-free − R-work gap widens from 0.011 to 0.014.",
        "Rotamer outliers rise from 0.00 % to 0.73 % (one residue) and clashscore from 0.8 to 1.2 on re-refinement.",
    ],
    "8C5N": [
        "Refined and scored against the deposited amplitudes (F_meas_au), not the merged intensities: French–Wilson conversion of the "
        "intensities drops 44 of the 9 968 inherited free reflections (D540). The free set itself (status 'f') is unchanged.",
        "The released model is one Phenix re-refinement of the deposited file; nothing the agent proposed has been credited yet (E044). "
        "Rotamer outliers 2.3 % in both the deposited and the released model, above the campaign's 1.5 % cap (pre-existing).",
        "The deposited model carries 665 hydrogens, an incomplete riding set; the released model keeps the deposited hydrogens.",
    ],
}
LEGACY_NOTE = (
    "Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file "
    "(D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, "
    "so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own."
)
FILE_DESC = [
    ("model/", "_refined.cif", "The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json."),
    ("model/", "_refined.pdb", "The same model in PDB format, from the same run."),
    ("maps/", "_map_coeffs.mtz", "Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot)."),
    ("data/", "_data.mtz", "The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors."),
    ("data/", "_flags.mtz", "The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free)."),
    ("data/", "_split.mtz", "The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work)."),
    ("data/", "split.json", "The same split as a list of reflections, with the seed that made it."),
    ("data/", "prep.json", "How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims."),
    ("deposited/", ".cif", "The deposited coordinate file as fetched from RCSB (the starting point)."),
    ("deposited/", ".fasta", "The entry's sequence as fetched from RCSB."),
    ("deposited/", "rcsb_entry.json", "The RCSB entry record (title, citation, experimental details) as fetched."),
    ("deposited/", "FETCHED", "When the raw files were fetched."),
    ("deposited/", "fetch_manifest.sha256", "SHA-256 of the raw files at fetch time."),
    ("refinement/", "current.json", "The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index."),
    ("refinement/", "command.txt", "The verbatim phenix.refine argv that wrote the model."),
    ("refinement/", "refine_001.eff", "The effective parameters of that run."),
    ("refinement/", "refine_001.log", "The phenix.refine log of that run."),
    ("refinement/", "refine_decisions.json", "The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels)."),
    ("refinement/", "refine_result.json", "The parsed result of that run (R factors, geometry, seed, wall clock)."),
    ("refinement/", "model_vs_data.campaign.log", "phenix.model_vs_data as run by the campaign on this model."),
    ("refinement/", "experiment_", "Record of the experiment cycle that produced this model (paired null control, geometry of both arms)."),
    ("validation/release/", "summary.json", "Release-time validation of the deposited and refined models (parsed from the logs beside it)."),
    ("validation/release/", "model_diff.json", "Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens."),
    ("validation/release/", "rfree_indep.", "Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts."),
    ("validation/release/", "model_vs_data.", "phenix.model_vs_data on the merged data+flags MTZ."),
    ("validation/release/", "molprobity.", "phenix.molprobity with default settings."),
    ("validation/release/", "merge_mtz.log", "Log of the data+flags merge used by model_vs_data."),
    ("validation/campaign/", "noise_floor", "A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model)."),
    ("validation/campaign/", "cycle_row.json", "The campaign's per-cycle record for this model (PROTOCOL §7)."),
    ("validation/campaign/", "molprobity", "The campaign's MolProbity run on this model."),
    ("validation/campaign/", "clash", "The campaign's clashscore runs (standard and altloc-aware)."),
    ("validation/campaign/", "dossier.json", "The campaign dossier: xtriage, model audit, composition hypothesis, baselines."),
    ("validation/campaign/verify_", "", "The campaign's independent verification runs (same scorer, earlier dates)."),
    ("validation/campaign/checks/", "", "Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check."),
    ("ledger/", "cycles.csv", "Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry."),
    ("ledger/", "changes.csv", "Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict."),
    ("ledger/", "bisections.csv", "Bisection steps when a cycle regressed."),
    ("ledger/", "noise_floor.csv", "The noise-floor row that set the credit bar: σ of R-free on every set."),
    ("ledger/", "checks.csv", "Gate results G0–G8."),
    ("ledger/", "rfree_consultations.csv", "How many times R-free-select was consulted (PROTOCOL §3.6)."),
    ("ledger/", "defects.csv", "Values that could not be computed, with the reason (never a sentinel)."),
    ("ledger/", "solvent_disagreements.csv", "Phenix/Coot disagreements on solvent sites."),
    ("ledger/", "deviations.csv", "Decision-log rows that name this target."),
    ("ledger/runs/", "DECISIONS.md", "The per-run human-readable decision log written by the driver."),
    ("ledger/runs/", "run_summary.json", "The per-run summary (cycles, credits, stop reason)."),
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def jload(p: Path, default=None):
    return json.loads(p.read_text()) if p.exists() else default


def rows(p: Path) -> list[dict]:
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return list(csv.DictReader(f))


def fnum(x, nd=4):
    return "—" if x is None else f"{float(x):.{nd}f}"


def fint(x):
    return "—" if x is None else str(int(x))


def ffloat(x):
    return float(x) if x not in (None, "") else None


def short(title: str | None, n: int = 64) -> str:
    t = (title or "").strip()
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return cut + "…"


def describe(rel: str) -> str:
    for prefix, part, text in FILE_DESC:
        if rel.startswith(prefix) and part in rel:
            return text
    return ""


def thresholds_by_sha() -> dict[str, str]:
    return {sha256(p): p.stem for p in (ROOT / "docs" / "thresholds").glob("thresholds_v*.yaml")}


def floor_stats(p: Path) -> dict | None:
    d = jload(p)
    if not d:
        return None
    vals = [s["r_free_full"] for s in d.get("per_seed", []) if s.get("ok") and s.get("r_free_full") is not None]
    if len(vals) < 2:
        return None
    return {"file": p.name, "start_model": d.get("start_model"), "n_seeds": len(vals), "mean_full": statistics.fmean(vals),
            "sd_full": statistics.stdev(vals)}


def target_record(tid: str, thr: dict[str, str]) -> dict:
    d = TARGETS / tid
    cur = jload(d / "refinement" / "current.json", {})
    rel = jload(d / "validation" / "release" / "summary.json", {})
    diff = jload(d / "validation" / "release" / "model_diff.json", {})
    dep_i = (rel.get("models", {}).get("deposited") or {}).get("indep") or {}
    ref_i = (rel.get("models", {}).get("refined") or {}).get("indep") or {}
    dep_m = (rel.get("models", {}).get("deposited") or {}).get("molprobity") or {}
    ref_m = (rel.get("models", {}).get("refined") or {}).get("molprobity") or {}
    dep_v = (rel.get("models", {}).get("deposited") or {}).get("model_vs_data") or {}
    ref_v = (rel.get("models", {}).get("refined") or {}).get("model_vs_data") or {}
    prep = jload(d / "data" / "prep.json", {})
    entry = jload(d / "deposited" / "rcsb_entry.json", {})
    result = jload(d / "refinement" / "refine_result.json", {})
    decisions = jload(d / "refinement" / "refine_decisions.json", {})
    # Noise floors. "Re-refined, no changes" is the floor measured from the deposited model; the credit bar (σ_select) is the
    # ledger's noise_floor row, which for 3TC7 comes from a floor re-measured under the released model's protocol.
    floors = [f for f in (floor_stats(p) for p in sorted((d / "validation" / "campaign").glob("noise_floor*.json"))) if f]
    dep_floor = next((f for f in floors if "/data/raw/" in (f["start_model"] or "")), floors[0] if floors else None)
    nf_rows = rows(d / "ledger" / "noise_floor.csv")
    nf = nf_rows[0] if nf_rows else {}
    nf_name = Path(nf.get("run_dir", "")).name or "noise_floor"
    cycles = rows(d / "ledger" / "cycles.csv")
    credited = [c for c in cycles if c.get("verdict") == "accepted"]
    changes = rows(d / "ledger" / "changes.csv")
    bisections = rows(d / "ledger" / "bisections.csv")
    model_path = cur.get("model", "")
    # The cycle whose run directory contains the released model.
    writer = max((c for c in cycles if c.get("run_dir") and model_path.startswith(c["run_dir"].rstrip("/") + "/")),
                 key=lambda c: len(c["run_dir"]), default={})
    bisect_step = None
    if "/bisect/" in model_path:
        step_id = model_path.split("/bisect/")[1].split("/")[0]
        b = next((b for b in bisections if b.get("step_id") == step_id), None)
        if b:
            bisect_step = {"step_id": step_id, "change_ids": json.loads(b["change_ids"]) if b.get("change_ids") else [],
                           "delta_r_free_select": ffloat(b.get("delta_r_free_select")), "regressed": b.get("regressed")}
    runs = {p.parent.name: jload(p) for p in (d / "ledger" / "runs").glob("*/run_summary.json")}
    run_summary = runs.get(writer.get("run_id", ""), None)
    if "baseline_rerefine" in model_path:
        status = "re-refined baseline, nothing credited"
    elif ref_i.get("r_free_manual") is not None and dep_i.get("r_free_manual") is not None and ref_i["r_free_manual"] < dep_i["r_free_manual"]:
        status = "improved"
    else:
        status = "credited, not below deposited"
    thr_version = thr.get(writer.get("thresholds_sha256", ""), None) or thr.get(nf.get("thresholds_sha256", ""), None)
    cit = (entry.get("citation") or [{}])[0]
    refine_hdr = (entry.get("refine") or [{}])[0]
    software = sorted({s.get("name", "") for s in entry.get("software", []) if s.get("classification", "").lower() == "refinement"} - {""})
    files = []
    for p in sorted(x for x in d.rglob("*") if x.is_file() and x.name != "README.md"):
        r = p.relative_to(d).as_posix()
        files.append({"path": r, "bytes": p.stat().st_size, "sha256": sha256(p), "description": describe(r)})
    ref_full, dep_full = ref_i.get("r_free_manual"), dep_i.get("r_free_manual")
    nf_mean = dep_floor["mean_full"] if dep_floor else None
    nf_sd = dep_floor["sd_full"] if dep_floor else None
    beyond = (ref_full - nf_mean) if (ref_full is not None and nf_mean is not None) else None
    return {
        "id": tid,
        "title": (entry.get("struct") or {}).get("title"),
        "status": status,
        "resolution_a": refine_hdr.get("ls_d_res_high") or ((entry.get("rcsb_entry_info") or {}).get("resolution_combined") or [None])[0],
        "space_group": prep.get("space_group"),
        "unit_cell": prep.get("unit_cell"),
        "deposited_refinement_software": software,
        "primary_citation": {k: cit.get(k) for k in ("title", "journal_abbrev", "year", "pdbx_database_id_DOI", "pdbx_database_id_PubMed")},
        "initial_release_date": (entry.get("rcsb_accession_info") or {}).get("initial_release_date"),
        "data": {"kind": prep.get("intensities_or_amplitudes"), "labels": prep.get("data_labels"), "n_reflections": prep.get("n_reflections"),
                 "n_free": prep.get("n_free"), "fraction_free": prep.get("fraction_free"), "n_select": prep.get("n_select"),
                 "n_report": prep.get("n_report"), "flags_source": prep.get("flags_source"),
                 "data_mtz_sha256": prep.get("data_mtz_sha256"), "flags_mtz_sha256": prep.get("flags_mtz_sha256"),
                 "sf_source_sha256": prep.get("sf_sha256"), "header_claim": prep.get("header_claim")},
        "r_free": {
            "deposited_on_our_flags": {"r_work": dep_i.get("r_work_manual"), "full": dep_full, "select": dep_i.get("r_free_select_manual"),
                                       "report": dep_i.get("r_free_report_manual"), "model_vs_data": dep_v},
            "rerefined_no_changes": {"mean_full": nf_mean, "sd_full": nf_sd, "n_seeds": dep_floor["n_seeds"] if dep_floor else 0,
                                     "floor_file": dep_floor["file"] if dep_floor else None},
            "credit_bar": {"protocol": nf_name, "sigma_full": ffloat(nf.get("sigma_full")), "sigma_select": ffloat(nf.get("sigma_select")),
                           "sigma_report": ffloat(nf.get("sigma_report")), "k_multiple": ffloat(nf.get("k_multiple")),
                           "accept_threshold_select": ffloat(nf.get("accept_threshold"))},
            "released": {"r_work": ref_i.get("r_work_manual"), "full": ref_full, "select": ref_i.get("r_free_select_manual"),
                         "report": ref_i.get("r_free_report_manual"), "model_vs_data": ref_v,
                         "ledger": {k: cur.get(k) for k in ("r_work", "r_free_full", "r_free_select", "r_free_report")}},
            "delta_full_vs_deposited": (ref_full - dep_full) if (ref_full is not None and dep_full is not None) else None,
            "delta_full_beyond_rerefinement": beyond,
            "delta_beyond_in_sd_full": (beyond / nf_sd) if (beyond is not None and nf_sd) else None,
        },
        "composition": {
            "deposited": {k: dep_i.get(k) for k in ("n_atoms", "n_hydrogen", "n_water_residues", "altlocs")},
            "released": {k: ref_i.get(k) for k in ("n_atoms", "n_hydrogen", "n_water_residues", "altlocs")},
        },
        "coordinate_diff": {k: diff.get(k) for k in ("waters_added", "waters_removed", "nonwater_residues_added", "nonwater_residues_removed",
                                                     "altloc_changes", "hydrogens_delta")} if diff else None,
        "molprobity": {"deposited": dep_m, "released": ref_m},
        "campaign": {
            "cycle_index": cur.get("cycle_index"), "stage": cur.get("stage"), "updated_at": cur.get("updated_at"),
            "model_on_pod": model_path, "n_cycles_on_record": len(cycles), "n_credited_cycles": len(credited),
            "writing_cycle": {"cycle_index": int(writer["cycle_index"]), "stage": writer.get("stage"), "run_id": writer.get("run_id"),
                              "verdict": writer.get("verdict"), "attributable_delta_select": ffloat(writer.get("attributable_delta")),
                              "delta_r_gap": ffloat(writer.get("delta_r_gap")), "geometry_flag": writer.get("geometry_flag") or None,
                              "run_dir": writer.get("run_dir")} if writer else None,
            "bisect_step": bisect_step,
            "credited_cycles": [{"cycle_index": int(c["cycle_index"]), "run_id": c.get("run_id"),
                                 "attributable_delta_select": ffloat(c.get("attributable_delta")),
                                 "r_free_full": ffloat(c.get("r_free_full")),
                                 "delta_r_gap": ffloat(c.get("delta_r_gap")),
                                 "geometry_flag": c.get("geometry_flag") or None,
                                 "accepted_changes": ffloat(c.get("accepted_changes"))} for c in credited],
            "n_changes_proposed": len(changes),
            "thresholds_version": thr_version,
            "run_summary": {k: run_summary.get(k) for k in ("run_id", "n_cycles", "n_credited_cycles", "stop_reason")} if run_summary else None,
            "refinement": {"phenix_version": result.get("version"), "macro_cycles": result.get("macro_cycles"),
                           "adp_model": result.get("adp_model") or decisions.get("adp_model"),
                           "n_tls_groups": len(result.get("tls_selections") or []),
                           "riding_hydrogens": any("hydrogens.refine=riding" in a for a in result.get("argv", [])),
                           "seed": result.get("seed"), "adp_decision": (decisions.get("adp_decision") or {}).get("reason")},
        },
        "caveats": CAVEATS.get(tid, []) + ([LEGACY_NOTE] if status.startswith("re-refined") else []),
        "files": files,
    }


def card(t: dict) -> str:
    tid = t["id"]
    rf = t["r_free"]
    dep, nfm, bar, rel = rf["deposited_on_our_flags"], rf["rerefined_no_changes"], rf["credit_bar"], rf["released"]
    mp_d, mp_r = t["molprobity"]["deposited"], t["molprobity"]["released"]
    comp_d, comp_r = t["composition"]["deposited"], t["composition"]["released"]
    camp = t["campaign"]
    cit = t["primary_citation"]
    cd = t["coordinate_diff"]
    L = [f"# {tid} — {t['title'] or ''}".rstrip(" —"), ""]
    L.append(f"**Status: {t['status']}.** " + ("This model has a lower R-free than the deposited file on the same free set." if t["status"] == "improved" else
             "See the caveats below."))
    L += ["", "| | |", "|---|---|",
          f"| Resolution | {t['resolution_a']} Å |",
          f"| Space group | {t['space_group']} |",
          f"| Data | {t['data']['kind']} ({t['data']['labels']}), {fint(t['data']['n_reflections'])} reflections |",
          f"| Free set | {fint(t['data']['n_free'])} reflections ({100 * (t['data']['fraction_free'] or 0):.1f} %), inherited unchanged from the deposition; select / report halves {fint(t['data']['n_select'])} / {fint(t['data']['n_report'])} |",
          f"| Deposited refinement program | {', '.join(t['deposited_refinement_software']) or '—'} |",
          f"| Released | {(t['initial_release_date'] or '')[:10]} |",
          f"| Primary citation | {cit.get('title') or ''} ({cit.get('journal_abbrev') or ''} {cit.get('year') or ''}), DOI {cit.get('pdbx_database_id_DOI') or '—'} |",
          f"| Thresholds version that judged the writing cycle | {camp['thresholds_version'] or '—'} |",
          f"| Phenix | {camp['refinement']['phenix_version'] or '—'} |",
          ""]
    L += ["## R-free on the frozen flags", "",
          "Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, "
          "no outlier rejection) and with `phenix.model_vs_data`. \"Re-refined, no changes\" is the mean of the campaign's ten noise-floor "
          "seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.", "",
          "| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |", "|---|---|---|---|---|---|",
          f"| Deposited, our flags | {fnum(dep['r_work'])} | {fnum(dep['full'])} | {fnum(dep['select'])} | {fnum(dep['report'])} | {fnum(dep['model_vs_data'].get('r_work'))} / {fnum(dep['model_vs_data'].get('r_free'))} |",
          f"| Re-refined, no changes ({nfm['n_seeds']} seeds) | — | {fnum(nfm['mean_full'])} ± {fnum(nfm['sd_full'], 5)} | — | — | — |",
          f"| **This release** | **{fnum(rel['r_work'])}** | **{fnum(rel['full'])}** | {fnum(rel['select'])} | {fnum(rel['report'])} | {fnum(rel['model_vs_data'].get('r_work'))} / {fnum(rel['model_vs_data'].get('r_free'))} |",
          "",
          f"Δ full R-free vs deposited: **{fnum(rf['delta_full_vs_deposited'])}**; beyond re-refinement alone: **{fnum(rf['delta_full_beyond_rerefinement'])}**"
          + (f" ({rf['delta_beyond_in_sd_full']:+.1f} × the floor's own spread)" if rf["delta_beyond_in_sd_full"] is not None else "") + ".",
          f"Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `{bar['protocol']}`): σ_select {fnum(bar['sigma_select'], 5)}, "
          f"σ_report {fnum(bar['sigma_report'], 5)}, σ_full {fnum(bar['sigma_full'], 5)}; a cycle is credited at ΔR-free-select ≤ {fnum(bar['accept_threshold_select'], 5)} "
          f"(k = {fnum(bar['k_multiple'], 1)}).",
          f"Campaign ledger for this model (`refinement/current.json`): R-work {fnum(rel['ledger'].get('r_work'))}, R-free full {fnum(rel['ledger'].get('r_free_full'))}, "
          f"select {fnum(rel['ledger'].get('r_free_select'))}, report {fnum(rel['ledger'].get('r_free_report'))}.", ""]
    L += ["## Geometry and composition (phenix.molprobity, release time, default settings)", "",
          "| | Deposited | This release |", "|---|---|---|",
          f"| Atoms (hydrogens) | {fint(comp_d['n_atoms'])} ({fint(comp_d['n_hydrogen'])}) | {fint(comp_r['n_atoms'])} ({fint(comp_r['n_hydrogen'])}) |",
          f"| Waters | {fint(comp_d['n_water_residues'])} | {fint(comp_r['n_water_residues'])} |",
          f"| Altloc letters | {', '.join(comp_d['altlocs'] or []) or 'none'} | {', '.join(comp_r['altlocs'] or []) or 'none'} |",
          f"| Clashscore | {fnum(mp_d.get('clashscore'), 2)} | {fnum(mp_r.get('clashscore'), 2)} |",
          f"| Ramachandran outliers / favored (%) | {fnum(mp_d.get('ramachandran_outliers_pct'), 2)} / {fnum(mp_d.get('ramachandran_favored_pct'), 1)} | {fnum(mp_r.get('ramachandran_outliers_pct'), 2)} / {fnum(mp_r.get('ramachandran_favored_pct'), 1)} |",
          f"| Rotamer outliers (%) | {fnum(mp_d.get('rotamer_outliers_pct'), 2)} | {fnum(mp_r.get('rotamer_outliers_pct'), 2)} |",
          f"| Cβ deviations | {fint(mp_d.get('cbeta_deviations'))} | {fint(mp_r.get('cbeta_deviations'))} |",
          f"| RMS bonds (Å) / angles (°) | {fnum(mp_d.get('rms_bonds'), 4)} / {fnum(mp_d.get('rms_angles'), 2)} | {fnum(mp_r.get('rms_bonds'), 4)} / {fnum(mp_r.get('rms_angles'), 2)} |",
          f"| MolProbity score | {fnum(mp_d.get('molprobity_score'), 2)} | {fnum(mp_r.get('molprobity_score'), 2)} |", ""]
    L += ["## What changed in the coordinates", ""]
    if cd:
        wa, wr = cd["waters_added"] or [], cd["waters_removed"] or []
        na, nr = cd["nonwater_residues_added"] or [], cd["nonwater_residues_removed"] or []
        alts = cd["altloc_changes"] or []
        if not (wa or wr or na or nr or alts or cd["hydrogens_delta"]):
            L.append("No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined "
                     "(coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.")
        else:
            L.append(f"From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):")
            L.append("")
            if wa:
                L.append(f"- Waters added ({len(wa)}): " + ", ".join(wa[:40]) + (" …" if len(wa) > 40 else ""))
            if wr:
                L.append(f"- Waters removed ({len(wr)}): " + ", ".join(wr[:40]) + (" …" if len(wr) > 40 else ""))
            if na:
                L.append(f"- Non-water residues added ({len(na)}): " + ", ".join(na[:20]))
            if nr:
                L.append(f"- Non-water residues removed ({len(nr)}): " + ", ".join(nr[:20]))
            if alts:
                L.append(f"- Residues whose alternate-conformation letters changed ({len(alts)}): " +
                         ", ".join(f"{a['residue']} {a['before']}→{a['after']}" for a in alts[:40]) + (" …" if len(alts) > 40 else ""))
            if cd["hydrogens_delta"]:
                L.append(f"- Hydrogen atoms: {cd['hydrogens_delta']:+d} (riding hydrogens added by the refinement protocol).")
    else:
        L.append("No coordinate diff on record.")
    L += ["", "## What the campaign did", ""]
    r = camp["refinement"]
    n_h = comp_r.get("n_hydrogen") or 0
    L.append(f"Refinement protocol of the released model: phenix.refine {r['phenix_version']}, {r['macro_cycles']} macro-cycles, "
             f"{r['adp_model']} ADPs" + (f" with {r['n_tls_groups']} TLS groups" if r["n_tls_groups"] else "") +
             (f", {n_h} riding hydrogens" if (r["riding_hydrogens"] and n_h) else ", no hydrogens in the model") + f", seed {r['seed']}. "
             + (f"ADP decision: {r['adp_decision']}. " if r["adp_decision"] else "") + "The verbatim command is `refinement/command.txt`.")
    L.append("")
    w = camp["writing_cycle"]
    if w and w["stage"] == "baseline_rerefine":
        L.append("The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed "
                 "(`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).")
    elif w:
        L.append(f"The released model was written by cycle {w['cycle_index']} (`{w['stage']}`, run `{w['run_id'] or '—'}`), verdict **{w['verdict'] or '—'}**"
                 + (f", attributable ΔR-free-select {fnum(w['attributable_delta_select'], 5)} against its paired null" if w["attributable_delta_select"] is not None else "")
                 + (f", ΔR-gap {fnum(w['delta_r_gap'], 5)}" if w["delta_r_gap"] is not None else "")
                 + (f"; geometry flag: {w['geometry_flag']}" if w["geometry_flag"] else "") + ".")
        if camp["bisect_step"]:
            b = camp["bisect_step"]
            L.append(f"It is the base kept from bisection step `{b['step_id']}` of that cycle (ΔR-free-select {fnum(b['delta_r_free_select'], 5)}, "
                     f"{'regressed' if b['regressed'] == '1' else 'not regressed'}), which carried: " + ", ".join(f"`{c}`" for c in b["change_ids"]) + ".")
        if camp["run_summary"] and camp["run_summary"].get("stop_reason"):
            L.append(f"That run ended: {camp['run_summary']['stop_reason']}.")
    L.append("")
    L.append(f"Cycles on record for this target: {camp['n_cycles_on_record']}; credited: {camp['n_credited_cycles']}; changes proposed: {camp['n_changes_proposed']} "
             f"(`ledger/cycles.csv`, `ledger/changes.csv`).")
    if camp["credited_cycles"]:
        L += ["", "Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit "
              "moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.", "",
              "| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |", "|---|---|---|---|---|---|"]
        for c in camp["credited_cycles"]:
            L.append(f"| {c['cycle_index']} | `{c['run_id'] or ''}` | {fnum(c['attributable_delta_select'], 5)} | {fnum(c['r_free_full'])} | {fnum(c['delta_r_gap'], 5)} | {c['geometry_flag'] or ''} |")
    L += ["", "## Caveats", ""]
    for c in t["caveats"]:
        L.append(f"- {c}")
    if not t["caveats"]:
        L.append("- None recorded beyond the general ones in the top-level README.")
    L += ["", "## Verify it yourself", "", "```bash",
          "# independent scorer (cctbx; needs Phenix)",
          f"phenix.python scripts/indep_rfree.py targets/{tid}/model/{tid}_refined.cif targets/{tid}/data/{tid}_data.mtz \\",
          f"  targets/{tid}/data/{tid}_flags.mtz targets/{tid}/data/{tid}_split.mtz out.json",
          "# standard tool",
          f"phenix.python scripts/merge_mtz.py targets/{tid}/data/{tid}_data.mtz targets/{tid}/data/{tid}_flags.mtz {tid}_merged.mtz",
          f"phenix.model_vs_data targets/{tid}/model/{tid}_refined.cif {tid}_merged.mtz",
          "# look at it",
          f"coot targets/{tid}/model/{tid}_refined.pdb --auto targets/{tid}/maps/{tid}_refined_map_coeffs.mtz",
          "```", ""]
    L += ["## Provenance", "",
          f"- Campaign record `refinement/current.json`: cycle {camp['cycle_index']}, stage `{camp['stage']}`, updated {camp['updated_at']}.",
          f"- Model on the campaign pod: `{camp['model_on_pod']}`.",
          f"- Data: `data.mtz` SHA-256 `{t['data']['data_mtz_sha256']}`, `flags.mtz` SHA-256 `{t['data']['flags_mtz_sha256']}`; "
          f"built from the deposited structure-factor file with SHA-256 `{t['data']['sf_source_sha256']}` (`data/prep.json`).",
          f"- Deposited header claim: R-work {fnum((t['data']['header_claim'] or {}).get('r_work'), 3)}, R-free {fnum((t['data']['header_claim'] or {}).get('r_free'), 3)}, "
          f"{fint((t['data']['header_claim'] or {}).get('n_free'))} free reflections.",
          "", "## Files", "", "| File | Size | What it is |", "|---|---|---|"]
    for f in t["files"]:
        L.append(f"| `{f['path']}` | {f['bytes']:,} | {f['description']} |")
    L.append("")
    return "\n".join(L)


def results_table(recs: list[dict]) -> str:
    order = sorted(recs, key=lambda t: (0 if t["status"] == "improved" else 1 if t["status"].startswith("credited") else 2,
                                        t["r_free"]["delta_full_beyond_rerefinement"] if t["r_free"]["delta_full_beyond_rerefinement"] is not None else 0))
    L = ["| Target | Res. (Å) | Entry | Deposited, our flags (full / report) | Re-refined, no changes (mean of 10) | This release (full / report) | Δ full: vs deposited / beyond re-refinement | Clashscore, rotamer outliers % (deposited → ours) | Status |",
         "|---|---|---|---|---|---|---|---|---|"]
    for t in order:
        rf = t["r_free"]; dep, nfm, rel = rf["deposited_on_our_flags"], rf["rerefined_no_changes"], rf["released"]
        mp_d, mp_r = t["molprobity"]["deposited"], t["molprobity"]["released"]
        bold = t["status"] == "improved"
        ours = f"**{fnum(rel['full'])} / {fnum(rel['report'])}**" if bold else f"{fnum(rel['full'])} / {fnum(rel['report'])}"
        z = f" ({rf['delta_beyond_in_sd_full']:+.1f}σ)" if rf["delta_beyond_in_sd_full"] is not None else ""
        L.append(f"| [{t['id']}](targets/{t['id']}/README.md) | {t['resolution_a']} | {short(t['title'])} | {fnum(dep['full'])} / {fnum(dep['report'])} | {fnum(nfm['mean_full'])} | {ours} | "
                 f"{fnum(rf['delta_full_vs_deposited'])} / {fnum(rf['delta_full_beyond_rerefinement'])}{z} | "
                 f"{fnum(mp_d.get('clashscore'), 1)}, {fnum(mp_d.get('rotamer_outliers_pct'), 1)} → {fnum(mp_r.get('clashscore'), 1)}, {fnum(mp_r.get('rotamer_outliers_pct'), 1)} | {t['status']} |")
    return "\n".join(L)


def main() -> int:
    check = "--check" in sys.argv
    thr = thresholds_by_sha()
    ids = sorted(p.name for p in TARGETS.iterdir() if p.is_dir())
    recs = [target_record(t, thr) for t in ids]
    outputs: dict[Path, str] = {}
    for t in recs:
        outputs[TARGETS / t["id"] / "README.md"] = card(t)
    prov = jload(ROOT / "provenance.json", {})
    index = {"name": "ag-refined-proteins", "generated_by": "scripts/build_index.py", "exported_from_pod_at": prov.get("exported_at"),
             "phenix_version": prov.get("phenix_version"), "n_targets": len(recs),
             "summary": {s: sum(1 for t in recs if t["status"] == s) for s in ("improved", "credited, not below deposited", "re-refined baseline, nothing credited")},
             "representations": sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "representations").glob("*") if p.is_dir())
             if (ROOT / "representations").exists() else [],
             "targets": recs}
    outputs[ROOT / "index.json"] = json.dumps(index, indent=1) + "\n"
    man = []
    for t in recs:
        for f in t["files"]:
            man.append(f"{f['sha256']}  targets/{t['id']}/{f['path']}")
    rep = ROOT / "representations"
    if rep.exists():
        for p in sorted(x for x in rep.rglob("*") if x.is_file()):
            man.append(f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}")
    outputs[ROOT / "MANIFEST.sha256"] = "\n".join(man) + "\n"
    if README.exists():
        txt = README.read_text()
        if TABLE_BEGIN in txt and TABLE_END in txt:
            a, b = txt.index(TABLE_BEGIN) + len(TABLE_BEGIN), txt.index(TABLE_END)
            outputs[README] = txt[:a] + "\n" + results_table(recs) + "\n" + txt[b:]
    changed = []
    for p, s in outputs.items():
        if not p.exists() or p.read_text() != s:
            changed.append(p)
            if not check:
                p.write_text(s)
    for p in changed:
        print(("would change " if check else "wrote ") + str(p.relative_to(ROOT)))
    print(f"{len(recs)} targets; {sum(len(t['files']) for t in recs)} files in MANIFEST.sha256")
    return 1 if (check and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
