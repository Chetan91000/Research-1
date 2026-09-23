# Experiment Readiness Audit

## Overall Status
**READY WITH MINOR CHANGES**

The core rule, canary, replay, and ingestion engines under `Major Project/` are fully implemented, functional, and verified by existing integration test suites. To begin execution, minor runner automation scripts, test fixture route additions, and local Ollama service activation are required.

---

## Experiment 1: Replay Verification & Header Differencing

### Status
**READY WITH MINOR CHANGES**

### What Is Ready
* `src/engine/replay.ts` contains `compareReplayEvidence` and `computeHeaderDiff`.
* `electron/fixtureServer.cjs` provides controllable target routes `/` (vulnerable baseline) and `/fixed` (hardened remediated route).
* `tests/engine.test.ts` validates `compareReplayEvidence` and `computeHeaderDiff` data structures.

### What Is Missing
* Standalone automation script (`tests/run-experiments.mjs`) to execute 30+ trials per route condition, log `ReplayComparisonResult` JSON files, and calculate confusion matrices.

### Implementation Evidence
* `Major Project/src/engine/replay.ts:57-177`
* `Major Project/electron/fixtureServer.cjs:17-82`
* `Major Project/tests/engine.test.ts:204-243`

### Ground-Truth Verification
* **Ground Truth Definition:** `http://127.0.0.1:4567/` is independently defined as `STILL_PRESENT` (missing CSP, HSTS, X-Content-Type-Options, frame-ancestors). `http://127.0.0.1:4567/fixed` is independently defined as `FIXED` (all 7 headers present).
* **Independence:** Ground truth is established *a priori* by inspecting HTTP response headers defined in `fixtureServer.cjs`, completely independent of Sentinel's replay comparator logic.

### Data Collection Readiness
* Evidence records capture raw HTTP response headers (`meta.headers`).
* `compareReplayEvidence` outputs structured `headerDiff` arrays (`added`, `removed`, `modified`, `unchanged`) and status strings (`Fixed`, `Still Present`, `Not Comparable`).

### Required Changes Before Execution
1. Create automated test runner `tests/run-experiments.mjs`.
2. Configure script to execute baseline captures on `/` followed by re-test captures on `/fixed` and `/`.

### Expected Artifacts
* `research/results/exp1_replay_results.json`
* `research/results/exp1_confusion_matrix.json`

---

## Experiment 2: Inert Canary Reflection Context Precision

### Status
**READY WITH MINOR CHANGES**

### What Is Ready
* `src/engine/canary.ts` contains `generateCanaryToken`, `analyzeDomReflection`, and `analyzeHeaderReflection`.
* `electron/fixtureServer.cjs` route `/search?q=` reflects parameter `q` into `HTML_BODY` and `ATTRIBUTE` contexts.
* Route `/fixed` provides a non-reflecting negative control condition.

### What Is Missing
* Inline script reflection route (e.g., `/search-script?q=`) in `fixtureServer.cjs` to cover `SCRIPT` and `SCRIPT_STRING` contexts.
* Automated test script to log `ReflectionAnalysis` outputs into a multi-class confusion matrix.

### Implementation Evidence
* `Major Project/src/engine/canary.ts:41-89`
* `Major Project/electron/fixtureServer.cjs:40-56`
* `Major Project/tests/engine.test.ts:118-134`

### Ground-Truth Verification
* **Ground Truth Definition:** Independent HTML string templates in `fixtureServer.cjs` define exact token reflection boundaries (`HTML_BODY`, `ATTRIBUTE`, `SCRIPT_STRING`, `UNREFLECTED`).
* **Independence:** Ground truth is established by inspecting the static HTML source of the mock routes prior to token injection. Canary injection does not modify target HTML structure outside the query parameter string.

### Data Collection Readiness
* `analyzeDomReflection` outputs `isReflected` (boolean), `context` (enum), and `snippet` (string).

### Required Changes Before Execution
1. Add route `/search-script` to `fixtureServer.cjs` containing `<script>const search = "TOKEN";</script>`.
2. Add automated confusion matrix calculation logic to `tests/run-experiments.mjs`.

### Expected Artifacts
* `research/results/exp2_canary_reflection.json`
* `research/results/exp2_context_confusion_matrix.json`

---

## Experiment 3: Passive Security Rule Coverage

### Status
**READY WITH MINOR CHANGES**

### What Is Ready
* `src/engine/rules.ts` contains `evaluateEvidenceRules` implementing 11 passive checks.
* `electron/fixtureServer.cjs` provides unhardened (`/`) and hardened (`/fixed`) routes.

### What Is Missing
* Script to iterate evidence records across 30 trials per condition and calculate precision, recall, and F1-score against independent ground-truth checklists.

### Implementation Evidence
* `Major Project/src/engine/rules.ts:24-290`
* `Major Project/tests/engine.test.ts:26-80`

### Ground-Truth Verification
* **Ground Truth Definition:** Independent checklist derived from OWASP Secure Headers Project and RFC specifications mapped to `/` (7 missing headers) and `/fixed` (0 missing headers).
* **Independence:** Ground truth is derived from web security specifications, not from `evaluateEvidenceRules`.

### Data Collection Readiness
* `evaluateEvidenceRules` returns an array of structured `Finding` objects (`id`, `severity`, `title`, `owasp`, `cwe`, `evidence`).

### Required Changes Before Execution
1. Add rule evaluation runner to `tests/run-experiments.mjs`.

### Expected Artifacts
* `research/results/exp3_rule_coverage.json`
* `research/results/exp3_precision_recall.json`

---

## Experiment 4: Local LLM Disaggregated Evaluation

### Status
**BLOCKED**

### What Is Ready
* `src/advisor/ollama.ts` contains `buildQuarantinedPrompt`, `parseAndValidateAdvisorResponse`, and `getOfflineKnowledge`.
* `electron/main.cjs:502-564` handles local Ollama queries and status checks over loopback (`127.0.0.1:11434`).
* `evidence.json` provides real session evidence inputs.

### What Is Missing
* **Local Software Dependency:** Ollama application is not currently installed/running on the system host.
* **Model Download:** Model tag `llama3:latest` (or `llama3:8b`) must be pulled locally.
* **Hardware Telemetry Harness:** Script to log GPU VRAM usage (`nvidia-smi` or OS process telemetry) and RAM footprint during inference.
* **Human Evaluation Rubric:** Scoring rubric for Remediation Defensive Correctness (C) and Applicability (D).

### Implementation Evidence
* `Major Project/src/advisor/ollama.ts:61-157`
* `Major Project/electron/main.cjs:502-564`

### Ground-Truth Verification
* **Citation Grounding (A):** Ground truth is the set of actual evidence IDs present in input `EvidenceRecord` arrays. `isGrounded` checks `citedEvidenceIds.every(id => availableIds.has(id))`.
* **Syntax Validity (B):** Ground truth established by attempting JS/Python AST parsing on extracted code blocks.
* **Defensive Correctness (C):** Ground truth established by human expert scoring (0–2 scale) against OWASP Cheat Sheet Series guidelines.

### Data Collection Readiness
* Response text, `isGrounded` boolean, and cited evidence IDs are captured automatically.
* **Telemetry Gap:** First-token latency, tokens/sec, and GPU VRAM/RAM telemetry require an external process wrapper.

### Required Changes Before Execution
1. Install Ollama and pull model `llama3:latest`.
2. Start Ollama service on `http://127.0.0.1:11434`.
3. Create telemetry logging wrapper for GPU VRAM and RAM.
4. Add Ollama batch runner to `tests/run-experiments.mjs`.

### Expected Artifacts
* `research/results/exp4_llm_disaggregated.json`
* `research/results/exp4_telemetry_latency.csv`

---

## Experiment 5: External Security Scanner Log Harmonization

### Status
**READY WITH MINOR CHANGES**

### What Is Ready
* `src/engine/ingest.ts` contains `parseScannerReport` supporting SARIF v2.1.0 and OWASP ZAP JSON schemas.
* `tests/engine.test.ts:145-202` verifies ingestion parsing.

### What Is Missing
* Dedicated fixture directory `tests/fixtures/scanner-reports/` containing sample SARIF and OWASP ZAP report files with independently verified ground-truth OWASP labels.

### Implementation Evidence
* `Major Project/src/engine/ingest.ts:99-239`
* `Major Project/tests/engine.test.ts:145-202`

### Ground-Truth Verification
* **Ground Truth Definition:** Ground truth is established by manually mapping official scanner rule IDs (e.g., `CWE-89`, `CWE-79`, `CWE-352`) to OWASP 2021 categories using official FIRST/OWASP lookup tables.
* **Independence:** Ground truth is derived from OWASP taxonomy documentation, independent of `mapCweToOwasp`.

### Data Collection Readiness
* `parseScannerReport` returns `{ findings, records }` containing normalized `owasp` and `cwe` fields.

### Required Changes Before Execution
1. Save canonical SARIF v2.1.0 and OWASP ZAP JSON test logs to `tests/fixtures/scanner-reports/`.
2. Add ingestion accuracy evaluation loop to `tests/run-experiments.mjs`.

### Expected Artifacts
* `research/results/exp5_scanner_ingest.json`

---

## Experiment 6: Multi-Model Performance Comparison

### Status
**BLOCKED**

### What Is Ready
* `electron/main.cjs:502-515` accepts dynamic `model` parameters.

### What Is Missing
* Ollama service running locally.
* Multiple models pulled (e.g., `llama3:8b`, `mistral:7b`).
* Telemetry harness for comparative VRAM/RAM logging.

### Implementation Evidence
* `Major Project/electron/main.cjs:502-515`

### Ground-Truth Verification
* Same ground-truth strategy as Experiment 4.

### Data Collection Readiness
* Response strings and generation times captured; hardware VRAM/RAM logging missing.

### Required Changes Before Execution
1. Install Ollama and pull `llama3:8b` and `mistral:7b`.
2. Wire VRAM/RAM telemetry logger.

### Expected Artifacts
* `research/results/exp6_multimodel_comparison.json`

---

## Cross-Experiment Issues

1. **Missing Automation Runner:** All core engine functions exist, but they currently run via unit tests (`engine.test.ts`). A dedicated batch runner script (`tests/run-experiments.mjs`) is needed to execute multiple trials and save JSON metric outputs to `research/results/`.
2. **Missing Local Ollama Service:** Ollama is not installed/running on the current Windows host. Experiments 4 and 6 are blocked until Ollama is active on `127.0.0.1:11434`.
3. **Missing Hardware Telemetry Logger:** No built-in Node.js function logs GPU VRAM or system RAM utilization during inference. An external OS process monitor script (e.g., using `nvidia-smi` logging) must accompany LLM experiments.
4. **Missing Inline Script Reflection Route:** `fixtureServer.cjs` contains HTML Body and Attribute reflection routes, but lacks an inline `<script>` tag reflection route to test all 4 canary contexts in a live server environment.

---

## Execution Dependencies

```
[Prerequisite 1: Install Ollama & Pull Llama3]
                    │
                    ▼
[Prerequisite 2: Update fixtureServer.cjs (/search-script)]
                    │
                    ▼
[Prerequisite 3: Create tests/run-experiments.mjs & Results Dir]
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
[Group A: Core Engine]    [Group B: LLM & Hardware]
(Exps 1, 2, 3, 5)          (Exps 4, 6)
       │                         │
       └────────────┬────────────┘
                    ▼
     [Populate IEEE Paper Results]
```

1. **Prerequisite 1:** Install Ollama on the local machine and pull model tag `llama3:latest`.
2. **Prerequisite 2:** Add route `/search-script` to `electron/fixtureServer.cjs` to enable `SCRIPT_STRING` canary context testing.
3. **Prerequisite 3:** Create `tests/run-experiments.mjs` and directory `research/results/`.
4. **Group A Execution (Exps 1, 2, 3, 5):** Run core engine experiments (Replay, Canary, Rules, Scanner Ingest) using the local fixture server.
5. **Group B Execution (Exps 4, 6):** Run LLM experiments (Citation grounding, syntax validity, defensive correctness, latency, VRAM) with hardware telemetry logger active.
6. **Data Synthesis:** Tabulate JSON artifacts into IEEE paper tables for Section VII (Results).

---

## Pre-Registration Checklist

* **Target System:** Sentinel Desktop (`sentinel-desktop` v0.1.0)
* **Git Commit Hash:** `HEAD` (Workspace state at execution time)
* **Fixture Server Version:** `electron/fixtureServer.cjs` (Port 4567)
* **Primary LLM Model / Tag:** `llama3:latest` (Ollama 127.0.0.1:11434)
* **Comparative LLM Model / Tag:** `mistral:7b`
* **Ollama Temperature Setting:** `0.2`
* **Format Constraint:** `json`
* **Trial Counts:**
  * Experiment 1 (Replay): 30 trials per route condition
  * Experiment 2 (Canary): 50 trials across 4 contexts
  * Experiment 3 (Rules): 30 trials per condition
  * Experiment 4 (LLM Evaluation): 30 queries
  * Experiment 5 (Scanner Ingest): 20 report files
* **Random Seed:** Fixed seed for token generator during testing
* **Hardware Configuration:** Windows Host, Dedicated GPU VRAM (Monitored via `nvidia-smi`)
* **Software Versions:** Node.js v18+, Electron latest, Ollama latest
* **Metric Definitions:** Precision, Recall, F1-Score, Replay Accuracy, FPR, FNR, Grounding Rate (A), Syntax Validity Rate (B), Defensive Correctness Score (C), Mean/Median/P95 Latency (E), Tokens/sec, Peak VRAM (MB).
* **Ground-Truth Definitions:** Independent HTTP header definitions, static HTML template offsets, OWASP 2021 mapping tables, OWASP Cheat Sheet defensive rubric.
* **Data Schema:** JSON arrays saved to `research/results/exp*.json`
* **Stopping Rules:** 30 trials completed per experiment condition; 20s request timeout for LLM queries.

---

## Final Gate

### Question:
**"Can the CORE experiments be executed without changing the research methodology?"**

### Answer:
**YES.**

The core research methodology—evaluating evidence-grounded local AI, non-destructive canary probing, and replay verification—remains completely unchanged. To begin execution, we only need to:
1. Start the local Ollama service (`127.0.0.1:11434`).
2. Add an inline script reflection route to `fixtureServer.cjs`.
3. Create the automated experiment runner script (`tests/run-experiments.mjs`).
