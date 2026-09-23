# Candidate Research Contribution Statements

This document formulates 5 distinct candidate research contribution statements based strictly on the actual implementation of **Sentinel Desktop** (`Major Project/`). 

*Note: Per instruction guidelines, candidate statements are presented without ranking.*

---

## Candidate Statement 1: Privacy-Preserving, Local AI Security Assistant Architecture
* **Proposed Contribution:** Design and implementation of a fully local, privacy-preserving web application security assistant that couples locally hosted open-weight LLMs with an isolated in-memory browser runtime, eliminating third-party cloud data transmission while providing evidence-grounded security analysis.
* **Implementation Evidence:** 
  * `Major Project/electron/main.cjs` (`ipcMain.handle('advisor:query')`, `isLoopbackHost` enforcing `127.0.0.1:11434` Ollama connection).
  * `partition: 'in-memory-lab'` browser isolation with default-deny permission handler.
  * `redactSensitiveData` and `redactHeaders` masking Bearer tokens, API keys, passwords, and cookie values before storage.
* **Relevant Literature:** 
  * Deng et al. (PentestGPT) [13], Xu et al. (AutoAttacker) [14] (cloud-dependent AI security tools).
  * Fang et al. [11], [12] (autonomous web exploitation using commercial APIs).
  * Zhao et al. [5], Liu et al. [6] (LLM deployment paradigms).
* **Experiment Required:** 
  * Network traffic analysis confirming zero outbound telemetry during active inspection runs.
  * Benchmarking local model inference latency, token generation speed, and RAM/VRAM utilization on consumer GPU/CPU hardware.
* **Limitation:** 
  * Local 7B/8B open-weight LLMs possess smaller context windows and lower multi-step reasoning capabilities compared to frontier cloud LLMs (e.g., GPT-4o [32]).
* **Supportability Status:** **SUPPORTABLE** (Implementation exists; hardware benchmarks pending).

---

## Candidate Statement 2: Non-Destructive Vulnerability Inspection via Inert Canary Reflection Probing
* **Proposed Contribution:** An active, non-destructive web security inspection mechanism that injects inert, randomized canary tokens into web parameters and analyzes browser DOM rendering contexts to detect output encoding weaknesses without generating or executing malicious exploit payloads.
* **Implementation Evidence:** 
  * `Major Project/src/engine/canary.ts` (`generateCanaryToken`, `buildCanaryTargetUrl`, `analyzeDomReflection`, `analyzeHeaderReflection`).
  * Context-aware reflection classification across 5 distinct contexts: `HTML_BODY`, `ATTRIBUTE`, `SCRIPT`, `SCRIPT_STRING`, and `HEADER`.
  * `electron/main.cjs:472-499` (`ipcMain.handle('canary:inject')`) executing safe browser navigation and DOM extraction via `executeJavaScript`.
* **Relevant Literature:** 
  * Deng et al. (NAUTILUS) [2] (API vulnerability detection).
  * OWASP Top 10 [66] (A03:2021-Injection / CWE-79 XSS).
  * Zhang et al. [8] (LLM security test generation).
* **Experiment Required:** 
  * Evaluating reflection detection accuracy and context precision against benchmark test suites (e.g., OWASP Benchmark [65], DVWA [76]).
  * Measuring false-positive rate compared to conventional static/passive headers-only scanners.
* **Limitation:** 
  * Inert canary tokens verify unencoded reflection but do not test complex multi-stage payload execution or secondary DOM transformations.
* **Supportability Status:** **SUPPORTABLE** (Implementation and unit test suite in `tests/engine.test.ts` exist; benchmark metrics pending).

---

## Candidate Statement 3: Deterministic Replay Verification and Header Differencing Engine
* **Proposed Contribution:** A differential evidence replay verification engine that automatically re-tests candidate security findings against updated application responses, computing granular HTTP header diffs and determining whether vulnerabilities are resolved (`Fixed`), persistent (`Still Present`), or ungrounded.
* **Implementation Evidence:** 
  * `Major Project/src/engine/replay.ts` (`compareReplayEvidence`, `computeHeaderDiff`).
  * Granular diff tracking for HTTP response headers (`added`, `removed`, `modified`, `unchanged`).
  * Re-evaluation of evidence streams against baseline findings for passive rules, canary reflection tokens, and imported scanner alerts.
* **Relevant Literature:** 
  * Mayoral-Vilches et al. (APT-Agent) [7] (unverified finding failures).
  * Shinn et al. (Reflexion) [71] (verbal reinforcement/feedback loops).
  * PTES Technical Guidelines [72] (re-testing standards).
* **Experiment Required:** 
  * Quantifying false-positive reduction rates and verification accuracy when comparing baseline vs. remediated target application runs.
  * Header diff accuracy validation across diverse web server response types.
* **Limitation:** 
  * Replay verification requires reproducible HTTP/DOM states and may produce `Not Comparable` status if target routing or session state changes significantly.
* **Supportability Status:** **SUPPORTABLE** (Implementation and integration tests in `tests/engine.test.ts` exist; benchmark metrics pending).

---

## Candidate Statement 4: Evidence-Grounded Citation Validation for AI Security Remediations
* **Proposed Contribution:** A grounded citation validation framework for LLM-assisted security advisors that pairs localized model prompts with curated offline knowledge bases and validates that AI-generated citations match cryptographically hashed evidence records stored during the live testing session.
* **Implementation Evidence:** 
  * `Major Project/src/advisor/ollama.ts` (`buildQuarantinedPrompt`, `getOfflineKnowledge`, `parseAndValidateAdvisorResponse`).
  * Grounding validation check: `isGrounded = citedEvidenceIds.every(id => availableIds.has(id))`.
  * Deterministic fallback patch generator (`getDefaultDeterministicPatches`) providing multi-framework fixes (React, Express, Next.js, FastAPI, Django) when parsing fails.
* **Relevant Literature:** 
  * Zhang et al. [15] (Hallucination snowballing).
  * Manakul et al. (SelfCheckGPT) [17] (Black-box hallucination detection).
  * Lewis et al. [53] (Retrieval-Augmented Generation).
  * Liu et al. [56] (Structured output constraints).
* **Experiment Required:** 
  * Measuring the Citation Grounding Rate (`isGrounded === true`) across different open-weight LLMs (e.g., Llama 3 8B, Mistral 7B).
  * Evaluating human developer comprehension and remediation code patch syntax correctness across supported frameworks.
* **Limitation:** 
  * Grounding validation verifies that cited evidence IDs exist in the session store, but does not guarantee the complete semantic accuracy of the LLM's natural language explanation (`whyItMatters`).
* **Supportability Status:** **SUPPORTABLE** (Implementation and test fixtures exist; empirical grounding metrics pending).

---

## Candidate Statement 5: Audit-Traceable, Redacted Evidence Collection Model for AI-Assisted Security Tools
* **Proposed Contribution:** An audit-traceable evidence collection architecture that captures Chrome DevTools Protocol network and browser events, applies automated redaction to sensitive authentication tokens, and generates cryptographically hashed structured event logs for reproducible security research.
* **Implementation Evidence:** 
  * `Major Project/electron/main.cjs` (`addEvidence`, `computeHash`, `redactSensitiveData`, `redactHeaders`, `rotateEvidenceStoreIfNeeded`).
  * `evidence.json` (539 KB recorded session dataset).
  * `Major Project/src/desktop.d.ts` (`EvidenceRecord` type definition).
* **Relevant Literature:** 
  * NIST Special Publication 800-115 [1] (Technical testing documentation).
  * FIRST CVSS / EPSS standards [63], [64].
  * Penetration Testing Execution Standard [72].
* **Experiment Required:** 
  * Benchmarking redaction recall/precision on synthetic request logs containing Bearer tokens, API keys, and custom authorization headers.
  * Storage efficiency and rotation overhead measurements over 10,000+ continuous event logs.
* **Limitation:** 
  * Token redaction relies on pattern-matching heuristics and regular expressions, which could miss non-standard custom authentication header formats if not explicitly configured.
* **Supportability Status:** **SUPPORTABLE** (Implementation and active `evidence.json` log exist; redaction benchmark metrics pending).
