# Sentinel Desktop: A Fully Local, Evidence-Grounded Interactive Application Security Assistant

## Abstract
Web application security testing requires combining domain expertise, structured analysis, and reproducible verification. Recent advancements in Large Language Models (LLMs) have enabled AI-assisted security tools to support reconnaissance, subtask planning, and vulnerability analysis. However, existing LLM-assisted systems predominantly rely on cloud-hosted AI APIs—introducing data confidentiality risks—while suffering from technical hallucinations, CLI-only tooling boundaries, and unverified vulnerability reporting. This paper presents **Sentinel Desktop**, a fully local, privacy-preserving interactive application security assistant. Sentinel Desktop integrates Chrome DevTools Protocol (CDP) browser instrumentation, automated passive security rule evaluation, non-destructive inert canary reflection probing, multi-source security scanner ingestion (SARIF v2.1.0 and OWASP ZAP), deterministic replay verification, and locally hosted LLM remediation advising. By confining execution strictly to on-premises local loopback environments, Sentinel Desktop eliminates third-party telemetry leakage while grounding AI reasoning in cryptographically traceable session evidence. We evaluate the framework across 130 physical trials on a controlled local fixture server. Under the tested conditions, the replay verification engine correctly classified 30/30 baseline vs. re-test trials ($N=30$, mean latency 1.12 ms); the inert canary engine achieved 100.0% binary reflection detection ($N=50$, mean latency 0.26 ms), with exact context classification on `HTML_BODY` (15/15), `SCRIPT_STRING` (10/10), and `NOT_FOUND` (10/10), while identifying a sequential DOM scanning limitation where `ATTRIBUTE` reflections were categorized under `HTML_BODY`; the passive rule engine correctly evaluated `CSP_MISSING_CHECK` across 30 response streams ($N=30$, mean latency 0.36 ms); and external scanner log ingestion achieved 100.0% mapping accuracy to OWASP 2021 categories for the tested report files ($N=20$). The local LLM experiments were not executed during this evaluation because Ollama was not installed or running on the evaluation host. This work establishes an empirical, reproducible foundation for local AI-assisted application security inspection.

## Index Terms
Web Application Security, Large Language Models, Local AI, Browser Automation, Vulnerability Verification, Replay Testing, Evidence Grounding.

---

## I. Introduction

Web application security testing is a fundamental process in software security engineering, designed to identify, assess, and remediate vulnerabilities before deployment [1]. Traditional application security assessments rely on automated scanners combined with manual inspection by security analysts [1], [46], [72]. While automated static and dynamic scanners accelerate initial flaw discovery, comprehensive assessment requires multi-stage reasoning—including target identification, dynamic state analysis, passive configuration checking, and post-analysis verification [1], [72].

Recent advancements in Large Language Models (LLMs) [5] have driven the development of AI-assisted security tools [10], [22]. Systems such as PentestGPT [13] and AutoAttacker [14] demonstrate that LLMs can assist human analysts by guiding task decomposition and recommending testing commands. Furthermore, empirical studies by Fang et al. demonstrate that LLM-based agents equipped with web interaction tools can navigate web applications and execute offensive exploit sequences [11], [12].

Despite these developments, current LLM-assisted security tools face critical operational challenges:
1. **Data Confidentiality & Privacy Risks:** Existing security agents rely primarily on third-party cloud-hosted LLM APIs (e.g., OpenAI GPT-4) [11], [13]. Offloading application source code, HTTP header streams, authentication credentials, or internal endpoints to third-party cloud servers risks compromising proprietary data.
2. **Technical Hallucinations:** Generative language models frequently suffer from technical hallucinations, outputting non-existent command flags, invalid parameter syntax, or fabricated endpoint URLs [7], [15], [50]. Uncorrected early hallucinations compound across multi-step reasoning chains [15].
3. **Unverified Vulnerability Reporting:** Language models often assert vulnerability hypotheses based on surface-level text patterns without confirming actual application state changes through execution feedback [7], [11], [50].
4. **Command-Line Tooling Bias:** Prior interactive tools operate predominantly over command-line interfaces or raw HTTP request strings [13], [50], missing dynamic client-side Document Object Model (DOM) rendered states and browser console context.

To address these challenges, this paper presents **Sentinel Desktop**, a local, evidence-first interactive application security assistant. Sentinel Desktop couples locally deployed open-weight LLMs with real-time interactive browser observation via Chrome DevTools Protocol (CDP), stateful context tracking, non-destructive inert canary reflection probing, and closed-loop differential replay verification.

---

## II. Background and Related Work

### A. Automated Penetration Testing
Automated penetration testing has historically been framed using decision-theoretic models and automated planning. Early frameworks utilized Markov Decision Processes (MDPs) and Partially Observable Markov Decision Processes (POMDPs) [23], [30], [68], [69] to model attack graphs under uncertainty [37], [39], [47]. Subsequent research applied deep reinforcement learning algorithms—including Deep Q-Networks (DQN), Advantage Actor-Critic (A3C), and Generative Adversarial Imitation Learning (GAIL)—to learn dynamic attack policies [24]–[26], [51], [78]. While formal decision models optimize path selection across discrete state spaces, they struggle to model unstructured natural language outputs and client-side DOM interactions in modern web applications.

### B. LLM-Based Security Testing
The integration of LLMs into security testing has shifted focus from formal decision graphs to semantic reasoning. Deng et al. introduced PentestGPT [13], an interactive penetration-testing assistant powered by cloud-hosted LLM APIs that assists human testers with subtask planning and command generation over terminal outputs. Xu et al. proposed AutoAttacker [14], demonstrating LLM-guided decision-making for automating cyber-attack execution sequences across systems. Happe and Cito [50] provided an empirical evaluation of LLMs in security testing, demonstrating that models frequently suffer from technical hallucinations, syntax errors, and non-reproducible outputs when operating over command-line interfaces.

### C. Security Agents
Recent agent architectures decompose complex security workflows into specialized components [38], [54]. Shen et al. introduced PentestAgent [27], combining domain-specific multi-agent roles with Retrieval-Augmented Generation (RAG) [53] to support automated penetration testing phases. In web security, Fang et al. [11] demonstrated that LLM-based agents equipped with web interaction tools can autonomously navigate web applications and execute offensive exploits against target websites. In API security, Deng et al. introduced NAUTILUS [2] for automated RESTful API vulnerability detection using structured feedback and coverage guidance.

### D. Evidence Grounding and Reliability
Reliability remains a central challenge in autonomous LLM deployment [7], [11], [50]. Zhang et al. [15] showed that uncorrected hallucinations early in a multi-step reasoning chain compound over subsequent iterations, leading to systemic failure. To address generative hallucination, prior research such as SelfCheckGPT (Manakul et al. [17]) has explored zero-resource factual consistency detection for LLMs by evaluating stochastic sampling agreement across generated responses. Furthermore, Liu et al. [56] demonstrated that enforcing structured output constraints on LLM generations improves formatting compliance and downstream parsing reliability.

### E. Research Gap
While existing literature explores automated decision models, cloud-backed LLM agents, and API testing, a distinct research gap remains:
1. Prior web testing agents rely on third-party cloud APIs, introducing data confidentiality risks for proprietary software analysis [11], [13].
2. Prior LLM security assistants focus on terminal/CLI inputs rather than dynamic client-side browser DOM states [13], [50].
3. Existing agents frequently report unverified vulnerability hypotheses without validating observable state changes through closed-loop re-testing [11], [14].
4. The feasibility, resource bounds, and context management limits of running these security inspection capabilities using **fully local LLMs** remain uncharacterized.

---

## III. Problem Statement and Research Objectives

### Problem Statement
Current LLM-assisted security testing systems either compromise confidentiality by transmitting sensitive data to cloud services or suffer from technical hallucinations, CLI tooling boundaries, and unverified vulnerability reporting when conducting web application security assessments.

### Research Objectives
1. **Construct a Privacy-Preserving Local Architecture:** Develop an interactive application security assistant powered exclusively by locally hosted LLMs, ensuring strict local loopback execution (`127.0.0.1`).
2. **Integrate Dynamic Browser Instrumentation:** Couple local AI reasoning with live browser automation via Chrome DevTools Protocol (CDP) to observe dynamic DOM states, network events, and console errors.
3. **Implement Non-Destructive Active Probing:** Develop inert canary token reflection probing to identify output encoding weaknesses across DOM contexts without generating weaponized exploit payloads.
4. **Establish Deterministic Vulnerability Verification:** Implement a closed-loop differential replay engine that evaluates re-test evidence streams against baseline findings to verify remediation status.
5. **Enforce Evidence-Grounded AI Reasoning:** Enforce strict citation validation checks ensuring LLM remediation recommendations reference valid session evidence IDs.

---

## IV. Proposed System

```
+-----------------------------------------------------------------------+
|                           Sentinel Desktop                            |
+-----------------------------------------------------------------------+
|                                                                       |
|  +---------------------+                   +-----------------------+  |
|  |   Local AI Layer    |<=================>|  Context Management   |  |
|  | (Ollama 127.0.0.1)  |  Prompts / Plans  |   (Evidence Store)    |  |
|  +----------+----------+                   +-----------+-----------+  |
|             |                                          |              |
|             | Structured JSON                          | State Updates|
|             v                                          v              |
|  +---------------------+                   +-----------------------+  |
|  | Browser Interaction |------------------>|   Security Analysis   |  |
|  | (Electron CDP View) |  Raw Observations | (Rules & Scanner Ingest) |  |
|  +----------+----------+                   +-----------+-----------+  |
|             |                                          |              |
|             | Dynamic Execution                        | Hypotheses   |
|             v                                          v              |
|  +-----------------------------------------------------------------+  |
|  |          Replay Verification & Evidence Collection             |  |
|  |         (Differential Header Diff & Redacted Hashed Logs)       |  |
|  +---------------------------------+-------------------------------+  |
|                                    |                                  |
+------------------------------------|----------------------------------+
                                     v
                        [ Reproducible Evidence Report ]
```

### A. System Architecture
Sentinel Desktop is structured as a modular, closed-loop interactive application security assistant. The system comprises five core modules: Local AI Layer, Browser Interaction Module, Security Analysis Engine, Context Management Engine, and Replay Verification & Evidence Collection Module.

### B. Local AI Layer
The local reasoning module interacts with open-weight language models deployed on host loopback (`127.0.0.1:11434` via Ollama). The module enforces loopback host validation (`isLoopbackHost`), structured JSON format constraints, low temperature ($0.2$), and a 20-second timeout.

### C. Browser Interaction
This module manages an Electron `WebContentsView` attached to Chrome DevTools Protocol (`1.3`). It captures console events (`Runtime.consoleAPICalled`), uncaught exceptions (`Runtime.exceptionThrown`), WebSocket frames, and HTTP request/response header streams (`labSession.webRequest`). Origin locking (`isAllowed`) restricts browser navigation strictly to target origins.

### D. Security Analysis
The analysis engine combines passive security rule evaluation with external scanner log ingestion:
* **Passive Security Rules (`rules.ts`):** Evaluates 11 security misconfiguration rules covering missing CSP, HSTS, X-Content-Type-Options, Anti-Clickjacking (X-Frame-Options/frame-ancestors), Referrer-Policy, Permissions-Policy, CORP/COEP, Permissive CORS with credentials, Cookie hygiene (`__Host-`, `__Secure-`), Mixed Content, and client console errors.
* **Scanner Log Ingestion (`ingest.ts`):** Normalizes external SARIF v2.1.0 logs (Nuclei, CodeQL) and OWASP ZAP JSON reports into the internal evidence format.

### E. Context Management
Maintains an in-memory evidence store (`evidenceStore`) recording `NAV`, `REQ`, `RES`, `RES_DONE`, `ERR`, `CONSOLE`, `CANARY_REFLECT`, `SCANNER_ALERT`, and `AUDIT` records. The engine rotates log archives at 1,000 events (`rotateEvidenceStoreIfNeeded`) to `.kilo/archives/` and persists debounced JSON snapshots to `evidence.json`.

### F. Vulnerability Verification
The Replay Comparator Engine (`replay.ts`) evaluates re-test evidence streams against baseline findings. It computes HTTP header diffs (`computeHeaderDiff`) across `added`, `removed`, `modified`, and `unchanged` states, classifying finding status as `Fixed`, `Still Present`, or `Not Comparable`.

### G. Evidence Collection
Every evidence record is assigned a unique identifier, ISO timestamp, and SHA-256 integrity hash (`computeHash`). Sensitive credentials (Bearer tokens, API keys, passwords, cookies) undergo automatic regex redaction (`redactSensitiveData`, `redactHeaders`) prior to persistence.

---

## V. Implementation

Sentinel Desktop is implemented in TypeScript within an Electron runtime environment:

* **Local Inference Interface (`src/advisor/ollama.ts`):** Constructs quarantined prompts (`buildQuarantinedPrompt`) combining offline CWE/OWASP knowledge (`getOfflineKnowledge`) with sanitized evidence snippets. Enforces citation grounding validation (`parseAndValidateAdvisorResponse`) by checking `isGrounded = citedEvidenceIds.every(id => availableIds.has(id))`.
* **Inert Canary Probing (`src/engine/canary.ts`):** Generates non-destructive random alphanumeric tokens (`generateCanaryToken`), constructs parameterized query URLs (`buildCanaryTargetUrl`), and evaluates DOM reflection contexts (`HTML_BODY`, `ATTRIBUTE`, `SCRIPT`, `SCRIPT_STRING`, `HEADER`).
* **Isolation Sandbox (`electron/main.cjs`):** Configures an isolated `in-memory-lab` partition (`partition: 'in-memory-lab'`). Enforces `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, and denies external popup windows and file downloads.

---

## VI. Experimental Methodology

### A. Experimental Environment
* **Host Platform:** Windows 10/11 x64 (`Windows_NT 10.0.26200`), Node.js `v24.20.0`, Electron runtime.
* **Target Fixture Server:** Local loopback server (`electron/fixtureServer.cjs`) listening on `http://127.0.0.1:4567`.
* **Repository State:** Git commit hash `a3bb957454684b647884ac15ca8ed9d413139a3d`.

### B. Experimental Targets
1. **Local Fixture Routes (`fixtureServer.cjs`):** Provides route `/` (unhardened baseline), `/fixed` (hardened route with security headers), `/search?q=` (parameter reflection in body and attribute), `/search-script?q=` (reflection in script string), and `/api/cors` (permissive CORS).
2. **Scanner Report Fixtures (`tests/fixtures/scanner-reports/`):** Canonical SARIF v2.1.0 logs (Nuclei/CodeQL) and OWASP ZAP JSON reports.

### C. Ground Truth
* **Experiment 1:** Ground truth is derived independently from static HTTP response header definitions in `fixtureServer.cjs` (`/fixed` defines CSP header $\rightarrow$ expected `Fixed`; `/` lacks CSP header $\rightarrow$ expected `Still Present`).
* **Experiment 2:** Ground truth is derived independently from HTML template structures in `fixtureServer.cjs` defining token reflection positions.
* **Experiment 3:** Ground truth is derived independently from OWASP Secure Headers specification (unhardened route `/` requires CSP finding; hardened route `/fixed` requires 0 findings).
* **Experiment 5:** Ground truth is derived independently from official CWE-to-OWASP 2021 lookup tables (`CWE-89` and `CWE-79` map to `A03:2021-Injection`).

### D. Experimental Conditions
Table I details the experimental configuration across the Group A evaluation suite.

#### Table I: Experimental Configuration Matrix

| Exp # | Evaluated Feature / Engine | Target / Condition | Independent Variable | Controlled Variables | Trial Count ($N$) |
| :--- | :--- | :--- | :--- | :--- | ---: |
| **Exp 1** | Replay Verification (`replay.ts`) | `127.0.0.1:4567` (`/` vs `/fixed`) | Remediation status of re-test route | Port 4567, payload structure, network transport | 30 |
| **Exp 2** | Inert Canary Probing (`canary.ts`) | `127.0.0.1:4567` (`/search`, `/search-script`, `/fixed`) | Reflection route & DOM context structure | Token length (16-char), HTTP method (GET) | 50 |
| **Exp 3** | Passive Security Rules (`rules.ts`) | `127.0.0.1:4567` (`/` vs `/fixed`) | Header presence (`Content-Security-Policy`) | Request origin, header case, engine parameters | 30 |
| **Exp 5** | Scanner Ingest (`ingest.ts`) | SARIF v2.1.0 & ZAP JSON files | Report schema format (SARIF vs. ZAP) | Report file path, JSON encoding, rule schema | 20 |

### E. Evaluation Metrics
* **Accuracy:** Ratio of correct classifications to total trials:
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
* **Precision & Recall:**
  $$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}$$
* **F1-Score:**
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **False Positive Rate (FPR) & False Negative Rate (FNR):**
  $$\text{FPR} = \frac{FP}{FP + TN}, \quad \text{FNR} = \frac{FN}{TP + FN}$$
* **Execution Telemetry:** Mean, Median, Standard Deviation, Min, Max, and $P_{95}$ execution times (ms).

### F. Experimental Procedure
Group A non-LLM experiments were executed automatically via `Major Project/tests/run-experiments.ts`. The script started `fixtureServer.cjs` on port 4567, executed 130 trials across Experiments 1, 2, 3, and 5, logged raw trial records to JSON files in `research/results/`, and shut down cleanly.

---

## VII. Results

The Group A experimental evaluation comprised 130 physical trials. Table VI provides a cross-experiment summary of observed metrics.

---

### A. Replay Verification
Under the tested fixture conditions, `compareReplayEvidence` correctly classified 15/15 remediated runs (`/fixed`) as `Fixed` and 15/15 unremediated runs (`/`) as `Still Present` ($N=30$, $TP=15, TN=15, FP=0, FN=0$). Table II details the classification metrics and execution timing for Experiment 1.

#### Table II: Experiment 1 Replay Verification Results

| Metric / Parameter | Observed Value |
| :--- | ---: |
| **Total Trials ($N$)** | 30 |
| **True Positives ($TP$)** | 15 |
| **True Negatives ($TN$)** | 15 |
| **False Positives ($FP$)** | 0 |
| **False Negatives ($FN$)** | 0 |
| **Accuracy** | 1.0000 (100.0%) |
| **Precision** | 1.0000 (100.0%) |
| **Recall** | 1.0000 (100.0%) |
| **F1-Score** | 1.0000 (1.000) |
| **False Positive Rate (FPR)** | 0.0000 (0.0%) |
| **False Negative Rate (FNR)** | 0.0000 (0.0%) |
| **Mean Latency (ms)** | 1.1167 ms |
| **Median Latency (ms)** | 0.5802 ms |
| **Standard Deviation (ms)** | 2.0523 ms |
| **$P_{95}$ Latency (ms)** | 2.2047 ms |

Header differencing (`computeHeaderDiff`) accurately identified added security headers between baseline and re-test response streams. These results apply strictly to the tested local loopback fixture conditions and should not be generalized to arbitrary remote web applications.

---

### B. Inert Canary Reflection
The inert canary evaluation comprised 50 trials across four target conditions. Binary reflection detection achieved 100.0% accuracy ($TP=40, TN=10, FP=0, FN=0$). Table III details the context-level results breakdown.

#### Table III: Experiment 2 Inert Canary Reflection & Context Breakdown

| Target Route | Tested Condition | Trials | Reflection Expected | Reflection Detected | Context Output | Context Accuracy |
| :--- | :--- | ---: | :---: | :---: | :--- | ---: |
| `/search?q=XYZ` | HTML Body Text | 15 | Yes | Yes (15/15) | `HTML_BODY` | 15/15 (100.0%) |
| `/search?q=XYZ` | HTML Tag Attribute | 15 | Yes | Yes (15/15) | `HTML_BODY`* | 0/15 (0.0%)* |
| `/search-script?q=XYZ` | Inline Script String | 10 | Yes | Yes (10/10) | `SCRIPT_STRING` | 10/10 (100.0%) |
| `/fixed` | Unreflected Control | 10 | No | No (10/10) | `NOT_FOUND` | 10/10 (100.0%) |

*\*Note on Attribute Context Behavior:* Route `/search?q=XYZ` reflects parameter `q` into both HTML body text (`<div>Showing results for: XYZ</div>`) and input tag attribute (`<input value="XYZ" />`). The `analyzeDomReflection` function scans the DOM string sequentially from index 0 and returns the first context encountered (`HTML_BODY`). Consequently, multi-context reflections are categorized under their first appearing DOM context. Mean canary execution latency was 0.26 ms ($P_{95} = 0.47$ ms).

---

### C. Passive Security Rules
Experiment 3 evaluated the `CSP_MISSING_CHECK` rule across 30 HTTP response evidence streams (15 from unhardened route `/` and 15 from hardened route `/fixed`). Table IV details the observed performance metrics.

#### Table IV: Experiment 3 Passive Security Rule Results (`CSP_MISSING_CHECK`)

| Metric / Parameter | Observed Value |
| :--- | ---: |
| **Evaluated Rule** | `CSP_MISSING_CHECK` |
| **Total Trials ($N$)** | 30 |
| **True Positives ($TP$)** | 15 |
| **True Negatives ($TN$)** | 15 |
| **False Positives ($FP$)** | 0 |
| **False Negatives ($FN$)** | 0 |
| **Accuracy** | 1.0000 (100.0%) |
| **Precision** | 1.0000 (100.0%) |
| **Recall** | 1.0000 (100.0%) |
| **F1-Score** | 1.0000 (1.000) |
| **Mean Latency (ms)** | 0.3601 ms |
| **$P_{95}$ Latency (ms)** | 0.8157 ms |

Under tested fixture conditions, the rule engine correctly identified missing CSP headers on unhardened responses and cleared hardened responses. These results validate rule execution fidelity for `CSP_MISSING_CHECK` on standard headers, but do not imply general coverage for untested security rules or vulnerability categories.

---

### D. Scanner Log Harmonization
Ingesting 10 SARIF v2.1.0 logs and 10 OWASP ZAP JSON reports yielded 20/20 successful parses ($N=20$). Table V details the scanner log ingestion results.

#### Table V: Experiment 5 External Security Scanner Log Harmonization

| Report Format | Ingested | Parse Success | Rule/CWE Extraction | Target OWASP Mapping | Evidence Records Created | Mean Latency |
| :--- | ---: | ---: | ---: | :--- | ---: | ---: |
| **SARIF v2.1.0 (Nuclei/CodeQL)** | 10 | 10 (100%) | `CWE-89` (100%) | `A03:2021-Injection` (100%) | 10 / 10 | <0.10 ms |
| **OWASP ZAP JSON** | 10 | 10 (100%) | `CWE-79` (100%) | `A03:2021-Injection` (100%) | 10 / 10 | <0.10 ms |

CWE extraction, severity level, location URI, and OWASP Top 10 mappings achieved 100.0% accuracy relative to independent lookup tables. This demonstrates schema parsing compatibility for the tested SARIF and ZAP files, but does not prove universal interoperability with all external scanner formats.

---

### E. Cross-Experiment Performance Summary
Table VI provides an aggregate cross-experiment summary of the physical Group A evaluation.

#### Table VI: Group A Cross-Experiment Summary

| Exp # | Component / Feature | Tested Target / Schema | $N$ | Accuracy | Precision | Recall | F1-Score | Mean Latency |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Exp 1** | Replay Verification | `127.0.0.1:4567` (`/` vs `/fixed`) | 30 | 100.0% | 100.0% | 100.0% | 1.000 | 1.12 ms |
| **Exp 2** | Inert Canary (Binary Detection) | `127.0.0.1:4567` (`/search`, `/fixed`) | 50 | 100.0% | 100.0% | 100.0% | 1.000 | 0.26 ms |
| **Exp 2** | Inert Canary (Exact Context) | `HTML_BODY`, `SCRIPT_STRING`, `ATTRIBUTE` | 50 | 70.0%* | 70.0%* | 70.0%* | 0.700* | 0.26 ms |
| **Exp 3** | Passive Security Rules | `CSP_MISSING_CHECK` on `127.0.0.1:4567` | 30 | 100.0% | 100.0% | 100.0% | 1.000 | 0.36 ms |
| **Exp 5** | Scanner Log Ingestion | SARIF v2.1.0 & OWASP ZAP Reports | 20 | 100.0% | 100.0% | 100.0% | 1.000 | <0.10 ms |

*\*Note for Exp 2 Context Accuracy:* Reflects 35/50 exact context matches due to 15 `ATTRIBUTE` reflections being categorized under `HTML_BODY` via sequential DOM scanning.

---

## VIII. Discussion

### A. Observations vs. Interpretation
1. **Replay Verification:** Under tested fixture conditions, differential evidence replay (`compareReplayEvidence`) accurately identified header additions and classified remediation status. This indicates that automated re-testing against baseline evidence streams can eliminate manual re-inspection for header-based misconfigurations on controlled targets.
2. **Inert Canary Reflection Probing:** Non-destructive randomized tokens (`generateCanaryToken`) successfully detected parameter reflection across HTML body, attribute, and script string contexts without executing malicious XSS attack payloads. However, sequential DOM string parsing means multi-context reflections are attributed to the earliest appearing context in DOM string order.
3. **Passive Rule & Scanner Integration:** Passive rule evaluation and report normalization (SARIF/ZAP) effectively unified static scanner output into a structured evidence model.
4. **Execution Telemetry:** Execution times across core Group A engines remained under 1.2 ms on local loopback, demonstrating low computational overhead for client-side security inspection.

### B. Status of Local LLM Experiments
The local LLM experiments (Experiments 4 and 6) were **not executed** during this evaluation because Ollama was not installed or running on the evaluation host. Consequently, empirical metrics regarding local model inference latency, token generation throughput, GPU VRAM allocation, citation grounding rates (`isGrounded`), and defensive code patch quality remain uncharacterized in this paper and represent essential future work.

---

## IX. Limitations and Threats to Validity

1. **Synthetic Local Fixture Target:** Evaluation was conducted on a controlled local fixture server (`fixtureServer.cjs`). Performance on complex, multi-origin enterprise web applications remains unassessed.
2. **Loopback Latency Bounds:** Measured execution latencies (<1.2 ms mean) reflect local loopback execution without remote network transport latency or packet loss.
3. **Sequential DOM Scanning Limitation:** In Experiment 2, parameter reflections appearing in multiple DOM contexts (e.g., body text and input attribute) are categorized strictly under the first context encountered in DOM string order (`HTML_BODY`).
4. **Limited Rule & Scanner Fixture Scope:** Experiment 3 evaluated `CSP_MISSING_CHECK` only; Experiment 5 evaluated canonical SARIF v2.1.0 and ZAP schemas only.
5. **Absence of LLM Empirical Evaluation:** Local LLM experiments (Experiments 4 and 6) were not executed due to missing host dependencies (Ollama), leaving AI advisor latency, grounding rates, and code patch quality unmeasured.
6. **Sample Size & Target Constraints:** Experiments comprised 130 total physical trials on local loopback targets without live internet routing or multi-model comparisons.

---

## X. Conclusion

This paper presented the design, implementation, and physical Group A evaluation of **Sentinel Desktop**, a fully local interactive application security assistant. By integrating Chrome DevTools Protocol browser instrumentation, passive security rules, non-destructive inert canary reflection probing, multi-scanner report ingestion, and deterministic replay verification, Sentinel Desktop provides a privacy-preserving environment for web application security analysis. Physical evaluation across 130 trials on a controlled fixture server demonstrated 100.0% classification accuracy in replay verification under tested conditions, 100.0% binary reflection detection in canary probing (with an identified sequential DOM scanning limitation for attribute reflections), and 100.0% mapping accuracy in scanner report harmonization. Future work will complete physical benchmarking of locally hosted open-weight LLMs (Experiments 4 and 6) to evaluate local model latency, citation grounding rates, and defensive code remediation quality.

---

## References

[1] National Institute of Standards and Technology (NIST), “Technical Guide to Information Security Testing and Assessment,” Special Publication 800-115, 2008.  
[2] G. Deng et al., “NAUTILUS: Automated RESTful API Vulnerability Detection,” in *Proc. USENIX Security Symp.*, 2023.  
[5] W. X. Zhao et al., “A Survey of Large Language Models,” *arXiv preprint arXiv:2303.18223*, 2023.  
[7] V. Mayoral-Vilches et al., “ExploitFlow, Cyber Security Exploitation Routes for Game Theory and AI Research in Robotics,” *arXiv preprint*, 2023.  
[10] A. Abuadbba et al., “From Promise to Peril: Rethinking Cybersecurity Red and Blue Teaming in the Age of LLMs,” *arXiv preprint*, 2026.  
[11] R. Fang et al., “LLM Agents Can Autonomously Hack Websites,” *arXiv preprint arXiv:2402.06664*, 2024.  
[12] R. Fang et al., “LLM Agents Can Autonomously Exploit One-Day Vulnerabilities,” *arXiv preprint arXiv:2404.08144*, 2024.  
[13] G. Deng et al., “PentestGPT: An LLM-Empowered Automatic Penetration Testing Tool,” in *Proc. USENIX Security Symp.*, 2023.  
[14] J. Xu et al., “AutoAttacker: A Large Language Model Guided System to Implement Automatic Cyber-Attacks,” *arXiv preprint arXiv:2403.01038*, 2024.  
[15] M. Zhang et al., “How Language Model Hallucinations Can Snowball,” *arXiv preprint arXiv:2305.13534*, 2023.  
[17] P. Manakul et al., “SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models,” in *Proc. Conf. Empirical Methods Nat. Lang. Process. (EMNLP)*, 2023.  
[22] S. Moskal et al., “LLMs Killed the Script Kiddie: How Agents Supported by Large Language Models Change the Landscape of Network Threat Testing,” in *Proc. IEEE Conf. Cybersecur. Resilience*, 2023.  
[23] J. Schwartz et al., “POMDP + Information-Decay: Incorporating Defender's Behaviour in Autonomous Penetration Testing,” in *Proc. Int. Conf. Auton. Agents Multiagent Syst. (AAMAS)*, 2020.  
[24] J. Chen et al., “GAIL-PT: An Intelligent Penetration Testing Framework with Generative Adversarial Imitation Learning,” *Comput. Secur.*, 2023.  
[25] N. Becker et al., “Evaluation of Reinforcement Learning for Autonomous Penetration Testing Using A3C, Q-Learning and DQN,” *Comput. Secur.*, 2024.  
[26] Q. Li et al., “A Hierarchical Deep Reinforcement Learning Model with Expert Prior Knowledge for Intelligent Penetration Testing,” *IEEE Trans. Dependable Secure Comput.*, 2023.  
[27] X. Shen et al., “PentestAgent: Incorporating LLM Agents to Automated Penetration Testing,” *arXiv preprint*, 2025.  
[30] C. Sarraute et al., “Penetration Testing == POMDP Solving?,” in *Proc. IEEE CyberSec*, 2013.  
[37] P. Ammann et al., “Scalable, Graph-Based Network Vulnerability Analysis,” in *Proc. ACM CCS*, 2002.  
[38] Significant Gravitas, “AutoGPT,” GitHub Repository, 2024.  
[39] M. S. Boddy et al., “Course of Action Generation for Cyber Security Using Classical Planning,” in *Proc. ICAPS*, 2005.  
[46] M. Denis et al., “Penetration Testing: Concepts, Attack Methods, and Defense Strategies,” in *Proc. IEEE IEMCON*, 2016.  
[47] K. Durkota and V. Lisy, “Computing Optimal Policies for Attack Graphs with Action Failures and Costs,” in *Proc. GameSec*, 2014.  
[50] A. Happe and J. Cito, “Getting Pwn'd by AI: Penetration Testing with Large Language Models,” in *Proc. ACM ESEC/FSE*, 2023.  
[51] Z. Hu et al., “Automated Penetration Testing Using Deep Reinforcement Learning,” *IEEE Access*, 2020.  
[53] P. Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” in *Proc. NeurIPS*, 2020.  
[54] G. Li et al., “CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Model Society,” in *Proc. NeurIPS*, 2023.  
[56] M. X. Liu et al., “We Need Structured Output: Towards User-Centered Constraints on Large Language Model Output,” *arXiv preprint*, 2024.  
[68] C. Sarraute et al., “POMDPs Make Better Hackers: Accounting for Uncertainty in Penetration Testing,” in *Proc. GameSec*, 2012.  
[69] C. Sarraute et al., “An Algorithm to Find Optimal Attack Paths in Nondeterministic Scenarios,” *arXiv preprint*, 2011.  
[72] Penetration Testing Execution Standard (PTES), “PTES Technical Guidelines,” 2024.  
[78] T. Zhou et al., “NIGAP: A New Method for Automated Penetration Testing,” in *Proc. IEEE Access*, 2019.
