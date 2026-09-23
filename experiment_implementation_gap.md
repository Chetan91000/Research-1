# Experiment Implementation Gap Analysis

This document analyzes the gap between the existing codebase (`Major Project/`) and the execution requirements of the planned experiments outlined in `experimental_plan.md`.

---

## 1. Summary of Execution Readiness

| Experiment | Target | Feasibility Classification | Code Modification Required | Execution Script Required |
| :--- | :--- | :--- | :--- | :--- |
| **Exp 1: Replay Verification Accuracy** | Local Fixture Server | **CAN RUN NOW** | **None** | Automated Node runner calling `compareReplayEvidence` on test fixtures. |
| **Exp 2: Inert Canary Reflection Precision** | Local Fixture Server (`/search`) | **CAN RUN NOW** | **None** | Automated script invoking `analyzeDomReflection` across generated tokens. |
| **Exp 3: Passive Rule Detection Coverage** | Local Fixture Server (`/` vs. `/fixed`) | **CAN RUN NOW** | **None** | Automated script evaluating `evaluateEvidenceRules` on fixture responses. |
| **Exp 4: Scanner Log Harmonization** | SARIF & ZAP Log Files | **CAN RUN NOW** | **None** | Automated script passing sample SARIF/ZAP JSON files to `parseScannerReport`. |
| **Exp 5: AI Citation Grounding & Remediation** | Local Ollama (`llama3:latest`) | **CAN RUN NOW** | **None** | Script executing `advisor:query` IPC handler with real evidence from `evidence.json`. |
| **Exp 6: Local Model Latency & Memory** | Local Ollama (`llama3:latest`) | **CAN RUN NOW** | **None** | Performance harness logging execution timestamps and GPU VRAM footprint. |
| **Exp 7 (Future): OWASP Juice Shop / DVWA** | Local Docker Containers | **REQUIRES MINOR IMPLEMENTATION** | Minor parameter handling extensions in `canary.ts` for form POST inputs. | Standalone Docker test harness. |
| **Exp 8 (Future): SAST/DAST Benchmarks** | OWASP Benchmark | **NOT CURRENTLY FEASIBLE** | Major architectural overhaul to convert desktop app to CLI batch runner. | N/A |

---

## 2. Minimal Automation Test Harness Needed

No application source code changes are required in `Major Project/src` or `Major Project/electron` to execute Experiments 1 through 6. All core engines (`rules.ts`, `canary.ts`, `replay.ts`, `ingest.ts`, `ollama.ts`, `main.cjs`) are already fully implemented, exported, and verified by `tests/engine.test.ts`.

To execute the experiments and record paper-ready metrics without manually clicking through the GUI, a lightweight experimental runner script can be added under `Major Project/tests/run-experiments.mjs`.

### Proposed Experimental Runner Tasks:
1. **Fixture Server Control:** Programmatically launch `electron/fixtureServer.cjs` on port 4567.
2. **Batch Data Collection:** Iterate through 50+ automated trials per experiment.
3. **CSV/JSON Metrics Export:** Export structured metric files (`results_exp1_replay.json`, `results_exp2_canary.json`, `results_exp5_advisor.json`) to `research/results/` containing:
   * Classification accuracy percentages
   * Precision, recall, and F1-scores
   * False-positive / false-negative counts
   * Inference latency (seconds) and token throughput (tokens/sec)
   * Grounding verification boolean flags (`isGrounded`)

---

## 3. Recommended Action Plan for Results Stage

1. **Step 1:** Create `Major Project/tests/run-experiments.mjs` (or extend `tests/engine.test.ts`) to execute Experiments 1–6 automated trials.
2. **Step 2:** Start local Ollama instance (`ollama serve`) hosting `llama3:latest`.
3. **Step 3:** Run the automated experiment suite to collect empirical metrics.
4. **Step 4:** Populate Section VII (Results) and Section VIII (Discussion) of the IEEE research paper (`research/improved_paper.md`) with the gathered empirical data, tables, and latency charts.
