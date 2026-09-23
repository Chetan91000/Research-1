# Detailed Experimental Plan for IEEE Results Validation

This document establishes the experimental methodology required to gather concrete empirical results for the IEEE research paper. All planned experiments are grounded in the actual codebase capabilities of **Sentinel Desktop** (`Major Project/`).

---

## Benchmark & Target Applicability Assessment

Before detailing individual experiments, we critically evaluate candidate targets:

| Target Benchmark | Current Compatibility Status | Justification & Interaction Capability |
| :--- | :--- | :--- |
| **Sentinel Local Fixture Server (`electron/fixtureServer.cjs`)** | **CAN RUN NOW** | **Fully Compatible.** Built-in local HTTP server running at `http://127.0.0.1:4567` with controllable routes (`/`, `/fixed`, `/search?q=`, `/api/cors`). Perfectly matches Sentinel's origin locking, CDP network interception, canary reflection analysis, and replay verification engine. |
| **OWASP Juice Shop / DVWA (Local Docker)** | **REQUIRES MINOR IMPLEMENTATION** | **Partially Compatible.** Web applications running on local loopback (`http://127.0.0.1:3000`) can be origin-locked and inspected for passive rules, headers, and CORS. However, automated form-submit canary probing requires minor script extensions beyond URL query parameter injection. |
| **OWASP Benchmark v1.2** | **NOT CURRENTLY FEASIBLE** | **Incompatible.** OWASP Benchmark is a static suite of thousands of Java Servlets designed for SAST/DAST CLI tools. Sentinel is a real-time browser desktop application analyzing dynamic HTTP/DOM states, not a headless SAST/DAST CLI runner. |
| **VulnHub / HackTheBox VMs** | **NOT CURRENTLY FEASIBLE** | **Incompatible.** VulnHub targets require multi-host network reconnaissance, port scanning (Nmap), service exploitation, and privilege escalation. Sentinel is strictly bounded to single-origin web application HTTP/DOM inspection and explicitly forbids network brute force or OS exploitation. |

---

## Experiment 1: Replay Verification & Header Differencing Accuracy

* **Classification:** **CAN RUN NOW**
* **1. Research Question:** Can the `compareReplayEvidence` engine accurately classify security findings as `Fixed`, `Still Present`, or `Not Comparable` when comparing baseline responses against remediated application runs?
* **2. Exact System Component Tested:** `src/engine/replay.ts` (`compareReplayEvidence`, `computeHeaderDiff`) and `src/engine/rules.ts`.
* **3. Hypothesis:** The Replay Engine will achieve 100% classification accuracy and zero false positives when evaluating baseline vulnerable headers against hardened headers on controllable HTTP routes.
* **4. Independent Variable:** Application state (`Vulnerable Baseline` vs. `Remediated Hardened Route`).
* **5. Dependent Variables:** Replay finding classification (`Fixed`, `Still Present`, `Not Comparable`), Header Diff status (`added`, `removed`, `modified`, `unchanged`).
* **6. Baseline/Control Condition:** Baseline response from `http://127.0.0.1:4567/` (missing CSP, HSTS, nosniff, frame-ancestors).
* **7. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs`).
* **8. Vulnerability Types:** Missing CSP (CWE-693), Missing HSTS (CWE-319), Missing X-Content-Type-Options (CWE-116), Missing Anti-Clickjacking (CWE-1021), Cookie attribute weaknesses (CWE-614).
* **9. Number of Trials:** 50 automated replay trials.
* **10. Exact Measurements:** Count of correctly classified findings; count of correctly identified added/modified HTTP headers.
* **11. Data to Record:** JSON output of `ReplayComparisonResult` objects, `headerDiff` arrays, SHA-256 evidence hashes.
* **12. Accuracy Calculation:** Accuracy = $(\text{Correct Classifications} / \text{Total Replay Runs}) \times 100\%$.
* **13. False Positives / False Negatives Calculation:**
  * False Positive = Replay classifies a persistent vulnerability as `Fixed`.
  * False Negative = Replay classifies a successfully remediated vulnerability as `Still Present`.
* **14. Reproducibility Procedure:** Execute automated script running `compareReplayEvidence(baselineFinding, [baselineEv], [retestEv])` using fixtures defined in `tests/engine.test.ts`.
* **15. Threats to Validity:** Changes in network latency or HTTP response body formatting causing non-deterministic matching; mitigated by using deterministic local loopback fixture server.

---

## Experiment 2: Non-Destructive Inert Canary Reflection & Context Precision

* **Classification:** **CAN RUN NOW**
* **1. Research Question:** How accurately can the Canary Engine detect unencoded reflection and identify the exact DOM/script rendering context without executing malicious scripts?
* **2. Exact System Component Tested:** `src/engine/canary.ts` (`generateCanaryToken`, `analyzeDomReflection`, `analyzeHeaderReflection`) and `electron/main.cjs` (`canary:inject`).
* **3. Hypothesis:** The inert canary analyzer will achieve high context-classification precision across HTML Body, Tag Attribute, and Inline Script contexts.
* **4. Independent Variable:** Injection context in rendered HTML (`HTML_BODY`, `ATTRIBUTE`, `SCRIPT`, `SCRIPT_STRING`, `HEADER`).
* **5. Dependent Variables:** Reflection detection (`isReflected`), Context precision (`context`), Canary finding severity assignment.
* **6. Baseline/Control Condition:** Hardened non-reflecting route (`/fixed`) vs. reflecting route (`/search?q=`).
* **7. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs` route `/search`).
* **8. Vulnerability Types:** Reflected XSS / Output Encoding Weaknesses (CWE-79 / OWASP A03:2021-Injection).
* **9. Number of Trials:** 100 injection trials across varying parameter configurations.
* **10. Exact Measurements:** Reflection detection rate, context classification accuracy matrix (Confusion Matrix across `HTML_BODY`, `ATTRIBUTE`, `SCRIPT_STRING`, `NOT_FOUND`).
* **11. Data to Record:** `ReflectionAnalysis` objects, DOM HTML snippets, injected tokens, evidence records.
* **12. Accuracy Calculation:** Context Accuracy = $(\text{Correctly Classified Contexts} / \text{Total Reflected Trials}) \times 100\%$.
* **13. False Positives / False Negatives Calculation:**
  * False Positive = Canary reports reflection in a non-reflecting DOM response.
  * False Negative = Canary fails to report a parameter reflected verbatim in HTML/script tags.
* **14. Reproducibility Procedure:** Run automated canary injection loop querying `/search?q=TOKEN` on `127.0.0.1:4567` and evaluate via `analyzeDomReflection(domHtml, token)`.
* **15. Threats to Validity:** Complex client-side JavaScript frameworks altering DOM rendering post-load; mitigated by using CDP execution wait (`webContents.executeJavaScript`).

---

## Experiment 3: Passive Security Rule Coverage & False-Positive Audit

* **Classification:** **CAN RUN NOW**
* **1. Research Question:** What is the rule detection coverage and false-positive frequency of Sentinel's passive security engine across vulnerable vs. hardened web responses?
* **2. Exact System Component Tested:** `src/engine/rules.ts` (`evaluateEvidenceRules`).
* **3. Hypothesis:** The passive rule engine will reliably flag all 11 security misconfiguration checks on unhardened routes while producing 0 high-severity false positives on fully compliant HTTPS responses.
* **4. Independent Variable:** Response header configuration (Unhardened `/` vs. RFC 6265bis compliant `/fixed`).
* **5. Dependent Variables:** Number of generated findings, severity distribution (High, Medium, Low, Info), finding title accuracy.
* **6. Baseline/Control Condition:** Response evidence from unhardened `http://127.0.0.1:4567/` vs. hardened `http://127.0.0.1:4567/fixed`.
* **7. Test Application:** Local Fixture Server (`electron/fixtureServer.cjs`).
* **8. Vulnerability Types:** Security Misconfigurations (OWASP A05:2021 / CWE-693, CWE-319, CWE-116, CWE-1021, CWE-614, CWE-942, CWE-311).
* **9. Number of Trials:** 50 evaluation runs.
* **10. Exact Measurements:** Total findings per route, precision, recall, F1-score.
* **11. Data to Record:** Array of `Finding` objects, evidence metadata, set-cookie headers.
* **12. Accuracy Calculation:** $\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$, $\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$.
* **13. False Positives / False Negatives Calculation:**
  * False Positive = Rule flags a missing header when the header is present and valid.
  * False Negative = Rule fails to flag a missing security header or insecure cookie flag.
* **14. Reproducibility Procedure:** Execute `evaluateEvidenceRules([evidenceRecord])` across fixture records defined in `tests/engine.test.ts`.
* **15. Threats to Validity:** Case-sensitivity variations in HTTP response headers; mitigated by `getHeaderValues` case-insensitive matching.

---

## Experiment 4: External Security Scanner Log Harmonization

* **Classification:** **CAN RUN NOW**
* **1. Research Question:** Can the ingest engine accurately normalize diverse SARIF v2.1.0 (Nuclei/CodeQL) and OWASP ZAP JSON reports into Sentinel's internal evidence timeline?
* **2. Exact System Component Tested:** `src/engine/ingest.ts` (`parseScannerReport`, `mapCweToOwasp`).
* **3. Hypothesis:** The ingest engine will parse 100% of valid SARIF v2.1.0 and OWASP ZAP report alerts, mapping CWE identifiers to their correct OWASP Top 10 categories.
* **4. Independent Variable:** External scanner report format (SARIF v2.1.0 vs. OWASP ZAP JSON).
* **5. Dependent Variables:** Number of imported findings, evidence record creation (`SCANNER_ALERT`), CWE-to-OWASP mapping accuracy.
* **6. Baseline/Control Condition:** Standard SARIF v2.1.0 and ZAP JSON sample files.
* **7. Test Application:** Synthetic log files and benchmark scanner outputs.
* **8. Vulnerability Types:** SQL Injection (CWE-89), XSS (CWE-79), CSRF (CWE-352), Broken Access Control (CWE-942).
* **9. Number of Trials:** 30 log ingestion runs across varying scanner formats.
* **10. Exact Measurements:** Ingestion success rate, CWE/OWASP mapping accuracy, evidence record creation count.
* **11. Data to Record:** Parsed `Finding` arrays, `EvidenceRecord` arrays, execution logs.
* **12. Accuracy Calculation:** Mapping Accuracy = $(\text{Correct OWASP Mappings} / \text{Total Ingested Alerts}) \times 100\%$.
* **13. False Positives / False Negatives Calculation:**
  * False Positive = Scanner alert imported with corrupted severity or incorrect CWE mapping.
  * False Negative = Ingest engine fails to parse a valid result in a supported SARIF/ZAP schema.
* **14. Reproducibility Procedure:** Pass sample JSON strings into `parseScannerReport(rawJson, filename)` as verified in `tests/engine.test.ts`.
* **15. Threats to Validity:** Non-standard vendor extensions in SARIF schema; mitigated by fallback property checks in `ingest.ts`.

---

## Experiment 5: AI Advisor Evidence Citation Grounding & Remediation Accuracy

* **Classification:** **CAN RUN NOW** (Requires local Ollama instance running `llama3:latest`)
* **1. Research Question:** What is the citation grounding rate (`isGrounded === true`) and multi-framework remediation code accuracy of the local Ollama AI Advisor when querying verified findings?
* **2. Exact System Component Tested:** `src/advisor/ollama.ts` (`buildQuarantinedPrompt`, `parseAndValidateAdvisorResponse`, `getOfflineKnowledge`) and `electron/main.cjs` (`advisor:query`).
* **3. Hypothesis:** The evidence citation validation check will successfully filter hallucinated evidence IDs, achieving 100% grounding verification while providing valid remediation code patches across supported frameworks.
* **4. Independent Variable:** Finding type (CWE-79 XSS, CWE-614 Cookie Security, CWE-693 Header Misconfiguration) and LLM model (Llama 3 8B local).
* **5. Dependent Variables:** Grounding status (`isGrounded`), cited evidence ID validity, code patch count, framework coverage.
* **6. Baseline/Control Condition:** Deterministic fallback patch generator (`getDefaultDeterministicPatches`).
* **7. Test Application:** Local Ollama model endpoint (`http://127.0.0.1:11434`) queried with real session evidence from `evidence.json`.
* **8. Vulnerability Types:** CWE-79, CWE-614, CWE-1021, CWE-942.
* **9. Number of Trials:** 30 model query trials.
* **10. Exact Measurements:** Citation Grounding Rate, LLM response latency (s), code patch syntax validity rate.
* **11. Data to Record:** `AdvisorResponse` objects, raw JSON LLM outputs, cited evidence ID arrays, `isGrounded` boolean flags.
* **12. Accuracy Calculation:** Citation Grounding Rate = $(\text{Trials with } isGrounded = true / \text{Total Advisor Runs}) \times 100\%$.
* **13. False Positives / False Negatives Calculation:**
  * False Positive (Ungrounded Citation): LLM cites an evidence ID that does NOT exist in the evidence store.
  * False Negative (Missed Grounding): Grounding validator flags a valid citation due to string formatting mismatch.
* **14. Reproducibility Procedure:** Send standardized quarantined prompts (`buildQuarantinedPrompt`) to local Ollama with `temperature: 0.2` and evaluate via `parseAndValidateAdvisorResponse`.
* **15. Threats to Validity:** Stochastic variability in LLM generation; mitigated by setting temperature to 0.2 and enforcing strict JSON format constraints.

---

## Experiment 6: Local AI Model Latency, Throughput & Memory Characterization

* **Classification:** **CAN RUN NOW** (Requires local Ollama instance)
* **1. Research Question:** What are the computational requirements (VRAM, RAM, inference latency, throughput) of executing evidence-grounded security advisory queries using local open-weight LLMs?
* **2. Exact System Component Tested:** `electron/main.cjs` (`advisor:query`, `ollama:status`) and Ollama local backend.
* **3. Hypothesis:** Local 7B/8B parameter models can process evidence prompts and generate structured JSON remediations in under 15 seconds per query on consumer GPU hardware.
* **4. Independent Variable:** Local model parameter size (e.g., Llama 3 8B vs. Mistral 7B) and prompt token length.
* **5. Dependent Variables:** First-token latency (s), total generation time (s), tokens per second (t/s), peak GPU VRAM utilization (MB), peak System RAM (MB).
* **6. Baseline/Control Condition:** Idle system resource baseline.
* **7. Test Application:** Local Ollama runtime hosting quantized models.
* **8. Vulnerability Types:** Multi-finding security summaries.
* **9. Number of Trials:** 20 benchmark runs per model.
* **10. Exact Measurements:** Seconds to complete JSON response, GPU VRAM allocated during inference.
* **11. Data to Record:** Timestamps, prompt lengths, response token counts, resource consumption logs.
* **12. Accuracy Calculation:** N/A (Performance Benchmarking). Mean and standard deviation calculated for latency and throughput.
* **13. False Positives / False Negatives Calculation:** N/A (Performance Benchmarking). Timeouts (>20s) recorded as execution failures.
* **14. Reproducibility Procedure:** Query local Ollama API via `ipcMain.handle('advisor:query')` with fixed prompt inputs while monitoring system hardware telemetry.
* **15. Threats to Validity:** Background OS process interference; mitigated by running benchmarks on an isolated, quiet workstation.
