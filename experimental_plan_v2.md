# Methodologically Grounded Experimental Plan (v2)

This document presents a revised, methodologically rigorous experimental plan for evaluating **Sentinel Desktop** (`Major Project/`). It eliminates assumptions of perfect performance, establishes independent ground-truth labels, separates software validation from research evaluation, and provides exact mathematical metrics.

---

## 1. Ground-Truth Strategy & Benchmark Suitability

### Ground-Truth Establishment Principle
Ground truth must be defined independently of Sentinel's codebase. In our experimental setup, ground truth is established by **controlled target configuration** and **manual expert labeling**:
* **Fixture Server Routes (`electron/fixtureServer.cjs`):** Routes are configured with deterministic, known security states (e.g., Route `/` has 7 known missing headers; Route `/fixed` has 0 missing headers). Ground-truth labels are created *a priori* by inspecting raw HTTP response definitions.
* **Canary Target Routes:** Endpoint `/search?q=XYZ` reflects parameter `q` into HTML Body and Attribute contexts verbatim without entity encoding. Ground-truth label: `Reflected (Unencoded)` in `HTML_BODY` and `ATTRIBUTE`.
* **Remediation Ground Truth:** Code remediation outputs are evaluated against expert defensive standards (OWASP Cheatsheet Series).

### Target Suitability Summary
* **Sentinel Fixture Server (`electron/fixtureServer.cjs`):** **CORE TARGET.** Suitable for controlled baseline/retest evaluations because route states are deterministic, isolated, and independently verified.
* **OWASP Juice Shop / DVWA (Local Docker):** **SUPPORTING TARGET.** Suitable for passive header/CORS analysis; requires manual labeling of actual route headers to establish ground truth.
* **OWASP Benchmark / VulnHub:** **EXCLUDED FROM EXPERIMENTS.** Incompatible architecture (static Java CLI / multi-host OS exploitation); evaluating against them would introduce severe construct invalidity.

---

## 2. Core vs. Supporting vs. Optional Experiment Classification

* **CORE Experiments:** Directly test the primary research questions regarding local interactive security inspection, replay verification, and evidence-grounded AI advice.
* **SUPPORTING Experiments:** Evaluate operational sub-components (passive rule coverage, scanner log ingestion).
* **OPTIONAL Experiments:** Secondary benchmarking (multi-model latency comparison).

---

## 3. Detailed Experimental Specifications

### Experiment 1: Replay Verification Classification & Header Differencing
* **Priority Classification:** **CORE**
* **1. Research Question:** How accurately does the differential replay engine classify vulnerability remediation status (`Fixed` vs. `Still Present`) when re-testing applications under controlled configuration changes?
* **2. Exact System Component Tested:** `src/engine/replay.ts` (`compareReplayEvidence`, `computeHeaderDiff`).
* **3. Scientific Hypothesis:** The replay engine will accurately detect header addition/removal, but classification accuracy will degrade if HTTP response status or routing paths change non-deterministically between baseline and re-test.
* **4. Variables:**
  * **Independent Variable:** Application route state (`Route /` vulnerable baseline vs. `Route /fixed` hardened re-test).
  * **Dependent Variables:** Classification decision (`Fixed`, `Still Present`, `Not Comparable`), Header Diff accuracy.
* **5. Controls:**
  * **Baseline Condition:** Session evidence recorded from `http://127.0.0.1:4567/` (known missing CSP, HSTS, nosniff, frame-ancestors).
  * **Experimental Condition:** Re-test evidence recorded from `http://127.0.0.1:4567/fixed` (known hardened headers).
  * **Control Condition (Unchanged):** Re-test evidence recorded from `http://127.0.0.1:4567/` (unremediated state).
  * **Difference:** Presence/absence of security response headers in raw HTTP responses.
* **6. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs`).
* **7. Vulnerability Types:** Missing CSP (CWE-693), Missing HSTS (CWE-319), Missing X-Content-Type-Options (CWE-116), Insecure Cookie attributes (CWE-614).
* **8. Number of Trials:** 30 automated re-test runs per condition.
* **9. Independent Ground-Truth Strategy:** Ground-truth labels (`FIXED` or `STILL_PRESENT`) are established directly from `fixtureServer.cjs` HTTP response header headers, independent of `compareReplayEvidence`.
* **10. Exact Mathematical Metrics:**
  $$\text{Replay Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
  $$\text{False Positive Rate (FPR)} = \frac{FP}{FP + TN}$$
  $$\text{False Negative Rate (FNR)} = \frac{FN}{TP + FN}$$
  * *True Positive (TP):* Replay engine reports `Fixed` when ground-truth header is present.
  * *True Negative (TN):* Replay engine reports `Still Present` when ground-truth header is missing.
  * *False Positive (FP):* Replay engine reports `Fixed` when ground-truth header is still missing.
  * *False Negative (FN):* Replay engine reports `Still Present` when ground-truth header has been added.
* **11. Data to Record:** `ReplayComparisonResult` JSON objects, raw HTTP headers, independent ground-truth labels.
* **12. Reproducibility Procedure:** Run automated runner passing pre-recorded baseline evidence and newly captured re-test evidence through `compareReplayEvidence`.
* **13. Conclusions & Non-Conclusions:**
  * *Can Conclude:* Whether the differential replay engine correctly identifies added/removed headers and updates finding state.
  * *Cannot Conclude:* That the replay engine guarantees full application safety against unmonitored dynamic side-effects.
* **14. Threats to Validity:**
  * *Construct Validity:* Using HTTP headers as a proxy for total security fix correctness.
  * *Internal Validity:* Timing variations in HTTP response delivery during re-testing.

---

### Experiment 2: Inert Canary Token Reflection Context Detection
* **Priority Classification:** **CORE**
* **1. Research Question:** What is the precision and recall of the inert canary reflection engine in identifying parameter reflection and classifying the exact rendering context (`HTML_BODY`, `ATTRIBUTE`, `SCRIPT_STRING`) without executing malicious code?
* **2. Exact System Component Tested:** `src/engine/canary.ts` (`analyzeDomReflection`, `analyzeHeaderReflection`).
* **3. Scientific Hypothesis:** Inert canary analysis will achieve high precision in `HTML_BODY` and `ATTRIBUTE` contexts, but precision may decline in complex nested JavaScript strings or template literals due to regex slicing limits.
* **4. Variables:**
  * **Independent Variable:** DOM rendering context of the reflected query parameter (`HTML_BODY`, `ATTRIBUTE`, `SCRIPT_STRING`, `UNREFLECTED`).
  * **Dependent Variables:** Reflection detection flag (`isReflected`), Context label match.
* **5. Controls:**
  * **Baseline / Unreflected Control:** Route `/fixed` (does not reflect query parameters).
  * **Experimental Condition:** Route `/search?q=TOKEN` (reflects token into body and input value attribute).
  * **Difference:** Presence of raw unencoded query string token in rendered DOM tree.
* **6. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs`).
* **7. Vulnerability Types:** Reflected XSS / Output Encoding Weakness (CWE-79).
* **8. Number of Trials:** 50 canary injection runs across different token formats.
* **9. Independent Ground-Truth Strategy:** Ground truth is established by manually parsing raw HTML templates in `fixtureServer.cjs` to label exact reflection character offsets and tag contexts.
* **10. Exact Mathematical Metrics:**
  $$\text{Precision}_{\text{context}} = \frac{TP_{\text{context}}}{TP_{\text{context}} + FP_{\text{context}}}$$
  $$\text{Recall}_{\text{context}} = \frac{TP_{\text{context}}}{TP_{\text{context}} + FN_{\text{context}}}$$
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **11. Data to Record:** `ReflectionAnalysis` output objects, ground-truth context labels, raw DOM HTML snippets.
* **12. Reproducibility Procedure:** Execute automated script sending randomized canary tokens (`generateCanaryToken`) to `/search?q=` and analyzing DOM HTML via `analyzeDomReflection`.
* **13. Conclusions & Non-Conclusions:**
  * *Can Conclude:* The precision of inert tokens in identifying reflection contexts without malicious payload execution.
  * *Cannot Conclude:* Exploitability or bypass capability against active Web Application Firewalls (WAFs).
* **14. Threats to Validity:**
  * *External Validity:* Simple mock HTML structure in fixture server vs. complex React/Angular DOM trees in real-world applications.

---

### Experiment 3: Passive Security Rule Coverage & Precision
* **Priority Classification:** **SUPPORTING**
* **1. Research Question:** What is the detection precision and recall of Sentinel's passive HTTP rule engine when evaluated against controlled vulnerable vs. hardened response headers?
* **2. Exact System Component Tested:** `src/engine/rules.ts` (`evaluateEvidenceRules`).
* **3. Scientific Hypothesis:** Passive rules will achieve high recall on standard security header misconfigurations, but may flag false positives on non-standard custom header names.
* **4. Variables:**
  * **Independent Variable:** Response header configuration of target HTTP response.
  * **Dependent Variables:** Detected finding list, severity breakdown, finding title match.
* **5. Controls:**
  * **Baseline / Vulnerable Condition:** Route `/` (missing CSP, HSTS, nosniff, frame-ancestors, insecure cookies).
  * **Control / Hardened Condition:** Route `/fixed` (all standard security headers present).
  * **Difference:** Header presence and attribute values.
* **6. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs`).
* **7. Vulnerability Types:** Security Misconfigurations (OWASP A05:2021 / CWE-693, CWE-319, CWE-116, CWE-1021, CWE-614, CWE-942).
* **8. Number of Trials:** 30 evaluation runs.
* **9. Independent Ground-Truth Strategy:** Independent ground-truth rule checklist derived directly from RFC specifications and OWASP Secure Headers Project.
* **10. Exact Mathematical Metrics:**
  $$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}, \quad \text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **11. Data to Record:** `Finding` arrays, ground-truth checklist flags, raw header objects.
* **12. Reproducibility Procedure:** Pass captured `EvidenceRecord` items directly into `evaluateEvidenceRules`.
* **13. Conclusions & Non-Conclusions:**
  * *Can Conclude:* Rule engine fidelity on standard HTTP response header evaluation.
  * *Cannot Conclude:* Comprehensive protection against application-logic flaws or deep authorization bypasses.
* **14. Threats to Validity:**
  * *Internal Validity:* Case-sensitivity variations in HTTP header key names.

---

## Experiment 4: Disaggregated LLM Evaluation (Grounding, Syntax, Remediation Correctness, Latency)

* **Priority Classification:** **CORE**
* **1. Research Question:** How do local open-weight LLMs perform when evaluated across disaggregated dimensions: (A) Citation Grounding, (B) Remediation Syntax Validity, (C) Defensive Correctness, and (E) Inference Latency?
* **2. Exact System Component Tested:** `src/advisor/ollama.ts` (`buildQuarantinedPrompt`, `parseAndValidateAdvisorResponse`, `getOfflineKnowledge`) and `electron/main.cjs` (`advisor:query`).
* **3. Scientific Hypothesis:** 
  * Evidence citation grounding (`isGrounded`) can be enforced deterministically via validation checks, but code patch defensive correctness will vary depending on model parameter size and CWE complexity.
  * `isGrounded === true` indicates citation integrity, NOT remediation code correctness.
* **4. Variables:**
  * **Independent Variable:** Finding type (CWE-79 XSS, CWE-614 Cookie, CWE-693 CSP) and local model size (e.g., Llama 3 8B vs. Mistral 7B).
  * **Dependent Variables:** 
    * *Metric A:* Citation Grounding Rate (`isGrounded === true`).
    * *Metric B:* Remediation Code Syntax Validity (parsable JavaScript/Python snippet).
    * *Metric C:* Defensive Correctness (evaluated against OWASP Cheatsheet standards).
    * *Metric D:* Response Latency & Throughput (seconds, tokens/sec, VRAM).
* **5. Controls:**
  * **Baseline / Control Condition:** Deterministic fallback patch generator (`getDefaultDeterministicPatches`).
  * **Experimental Condition:** Local LLM generated response (`advisor:query`).
  * **Difference:** Generative LLM output vs. static template fallback.
* **6. Test Application:** Local Ollama API endpoint (`http://127.0.0.1:11434`).
* **7. Vulnerability Types:** CWE-79, CWE-614, CWE-1021, CWE-942.
* **8. Number of Trials:** 30 queries per model.
* **9. Independent Ground-Truth Strategy:** 
  * *Grounding Ground Truth:* Set of actual `id` strings present in the input `EvidenceRecord` array.
  * *Defensive Correctness Ground Truth:* Manual expert review rubric scoring code patches (0 = incorrect/unsafe, 1 = partially secure, 2 = production-ready defensive fix based on OWASP Cheat Sheets).
* **10. Exact Mathematical Metrics:**
  $$\text{Grounding Rate (A)} = \frac{\text{Count}(isGrounded = \text{true})}{N_{\text{total}}} \times 100\%$$
  $$\text{Syntax Validity Rate (B)} = \frac{\text{Count}(\text{Parsable Snippets})}{N_{\text{snippets}}} \times 100\%$$
  $$\text{Defensive Correctness Score (C)} = \frac{\sum \text{Rubric Score}}{2 \times N_{\text{patches}}} \times 100\%$$
  $$\text{Latency Telemetry (E): Mean}, \text{Median}, \text{StdDev}, P_{95} \text{ total generation time (s)}, \text{Tokens/sec}, \text{Peak VRAM (MB)}, \text{Peak RAM (MB)}$$
* **11. Data to Record:** `AdvisorResponse` JSON objects, raw LLM outputs, citation arrays, latency timestamps, GPU memory logs.
* **12. Reproducibility Procedure:** Send fixed quarantined prompts (`buildQuarantinedPrompt`) to Ollama with `temperature: 0.2` and measure telemetry.
* **13. Conclusions & Non-Conclusions:**
  * *Can Conclude:* Local model citation fidelity, schema adherence, and hardware resource utilization.
  * *Cannot Conclude:* That citation grounding implies code patch correctness, or that local 8B models match GPT-4 reasoning depth.
* **14. Threats to Validity:**
  * *Construct Validity:* Equating syntax validity with security patch correctness.
  * *Internal Validity:* GPU thermal throttling affecting latency measurements.

---

### Experiment 5: External Security Scanner Log Harmonization
* **Priority Classification:** **SUPPORTING**
* **1. Research Question:** What is the parsing completeness and CWE-to-OWASP mapping accuracy when normalizing external SARIF v2.1.0 and OWASP ZAP JSON scanner logs into Sentinel's evidence timeline?
* **2. Exact System Component Tested:** `src/engine/ingest.ts` (`parseScannerReport`, `mapCweToOwasp`).
* **3. Scientific Hypothesis:** The ingest engine will reliably extract rule IDs and URIs from standard SARIF v2.1.0 and ZAP reports, but mapping accuracy depends on the presence of explicit CWE tags in rule properties.
* **4. Variables:**
  * **Independent Variable:** Scanner log format (SARIF v2.1.0 from Nuclei/CodeQL vs. OWASP ZAP JSON).
  * **Dependent Variables:** Ingest success rate, OWASP category mapping accuracy, evidence record count.
* **5. Controls:**
  * **Baseline Condition:** Raw unparsed scanner report files.
  * **Experimental Condition:** Parsed `Finding` and `EvidenceRecord` output arrays.
  * **Difference:** Structured ingestion into Sentinel timeline.
* **6. Test Application:** Benchmark scanner export files.
* **7. Vulnerability Types:** SQL Injection (CWE-89), XSS (CWE-79), CSRF (CWE-352), Path Traversal (CWE-22).
* **8. Number of Trials:** 20 report ingestion runs.
* **9. Independent Ground-Truth Strategy:** Ground truth is established by manually mapping scanner alert rule IDs to standard OWASP 2021 categories using official CWE-to-OWASP mapping tables.
* **10. Exact Mathematical Metrics:**
  $$\text{Mapping Accuracy} = \frac{\text{Correct OWASP Categorizations}}{\text{Total Ingested Alerts}} \times 100\%$$
* **11. Data to Record:** Parsed findings, evidence records, ground-truth category labels.
* **12. Reproducibility Procedure:** Pass sample JSON log files into `parseScannerReport`.
* **13. Conclusions & Non-Conclusions:**
  * *Can Conclude:* Ingestion fidelity and schema normalization accuracy for supported scanner formats.
  * *Cannot Conclude:* Security scanner detection efficacy or scanner tool superiority.
* **14. Threats to Validity:**
  * *External Validity:* Proprietary non-standard JSON outputs from un-supported commercial scanners.

---

## 4. Software Validation vs. Empirical Research Matrix

| Activity | Category | Purpose in Project | Belongs in Paper as: |
| :--- | :--- | :--- | :--- |
| **`tests/engine.test.ts` Integration Suite** | **Software Validation** | Verifies code correctness (unit checks, function signatures, parser logic). | Appendix / Implementation Section (Demonstrates software reliability). |
| **Experiment 1 (Replay Classification)** | **Research Evaluation** | Evaluates differential evidence comparison against ground-truth application states. | Section VII: Results (Empirical verification effectiveness). |
| **Experiment 2 (Canary Context Precision)** | **Research Evaluation** | Measures non-destructive reflection context detection precision. | Section VII: Results (Empirical detection accuracy). |
| **Experiment 4 (Disaggregated LLM Analysis)** | **Research Evaluation** | Benchmarks local model grounding, syntax validity, defensive correctness, and latency. | Section VII: Results (Empirical AI performance & resource usage). |
