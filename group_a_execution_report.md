# Group A Execution Report

This document records the physical execution results of the non-LLM Group A experiments for **Sentinel Desktop** (`Major Project/`).

---

## 1. Experiments Attempted
* **Experiment 1:** Replay Verification & Header Differencing (`exp1_replay.json`)
* **Experiment 2:** Inert Canary Reflection Context Precision (`exp2_canary.json`)
* **Experiment 3:** Passive Security Rule Coverage (`exp3_rules.json`)
* **Experiment 5:** External Security Scanner Log Harmonization (`exp5_scanner.json`)

---

## 2. Experiments Successfully Completed
* **Experiment 1:** Completed (30 trials).
* **Experiment 2:** Completed (50 trials).
* **Experiment 3:** Completed (30 trials).
* **Experiment 5:** Completed (20 trials).

---

## 3. Experiments Blocked
* **Experiment 4 (Disaggregated Local LLM Evaluation):** **BLOCKED.** Local Ollama service is not installed/running on the system host (`127.0.0.1:11434`).
* **Experiment 6 (Multi-Model Comparison):** **BLOCKED.** Local Ollama service is not installed/running on the system host (`127.0.0.1:11434`).

---

## 4. Exact Trial Counts Completed

| Experiment | Target Fixture / Source | Planned Trials | Completed Trials | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Experiment 1** | Local Fixture Server (`/` vs. `/fixed`) | 30 | 30 | 100% Complete |
| **Experiment 2** | Local Fixture Server (`/search`, `/search-script`, `/fixed`) | 50 | 50 | 100% Complete |
| **Experiment 3** | Local Fixture Server (`/` vs. `/fixed`) | 30 | 30 | 100% Complete |
| **Experiment 5** | SARIF v2.1.0 & OWASP ZAP Fixture Files | 20 | 20 | 100% Complete |
| **Total** | | **130** | **130** | **100% Group A Complete** |

---

## 5. Generated Artifact Paths

All raw observations, trial records, metadata, and aggregate summaries have been exported to JSON artifacts:

* **Experiment Metadata:** [research/results/experiment_metadata.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/experiment_metadata.json)
* **Group A Aggregate Summary:** [research/results/group_a_summary.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/group_a_summary.json)
* **Experiment 1 Raw & Aggregate Data:** [research/results/exp1_replay.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/exp1_replay.json)
* **Experiment 2 Raw & Aggregate Data:** [research/results/exp2_canary.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/exp2_canary.json)
* **Experiment 3 Raw & Aggregate Data:** [research/results/exp3_rules.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/exp3_rules.json)
* **Experiment 5 Raw & Aggregate Data:** [research/results/exp5_scanner.json](file:///c:/Users/Aayush20/Desktop/Researchpp/research/results/exp5_scanner.json)

---

## 6. Environment Information

* **Git Commit Hash:** `a3bb957454684b647884ac15ca8ed9d413139a3d`
* **Project Version:** `sentinel-desktop v0.1.0`
* **Node.js Version:** `v24.20.0`
* **Operating System:** `Windows_NT 10.0.26200 (x64, win32)`
* **Fixture Server Endpoint:** `http://127.0.0.1:4567` (`electron/fixtureServer.cjs`)
* **Execution Runner Script:** `Major Project/tests/run-experiments.ts` (Executed via `npx tsx`)

---

## 7. Deviations from Preregistered Methodology

* **Fixture Route Extension (Approved):** Added route `/search-script?q=` to `electron/fixtureServer.cjs` to satisfy the preregistered condition for testing inline `<script>` context reflection in Experiment 2. (This change was explicitly approved under Rule 10).
* **No Unplanned Deviations:** All trial counts, target routes, independent ground-truth definitions, and metric calculation formulas executed strictly as registered.

---

## 8. Failures & Exceptions

* **System Errors / Crashes:** 0 execution errors recorded across all 130 trials.
* **Network Timeouts:** 0 timeouts observed on local loopback fixture queries.

---

## 9. Threats to Validity Discovered During Execution

* **Internal Validity (Loopback Determinism):** Executing trials on a local loopback HTTP fixture server yields near-zero network jitter (mean execution times: Exp 1 ~1.7ms, Exp 2 ~0.9ms, Exp 3 ~0.3ms, Exp 5 ~0.08ms). Real-world network latency against remote targets will introduce variable network transport delays.
* **External Validity (Fixture Complexity):** The synthetic fixture server uses static HTML strings and simple script tags. Complex modern Single Page Applications (SPAs) with heavy client-side state hydration could introduce DOM parsing edge cases not present in the local fixture.
