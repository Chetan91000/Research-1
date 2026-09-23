# Grounded Research-Gap Analysis: Sentinel Desktop Implementation

This document presents a rigorous research-gap analysis aligned strictly with the **actual implementation of Sentinel Desktop** (`Major Project/`), rather than theoretical or unimplemented offensive paper proposals.

---

## 1. Automated Penetration Testing
* **A. Existing Research Demonstrates:** Formal decision models (MDPs/POMDPs) [23], [30] and reinforcement learning (DQN, A3C, GAIL) [24]–[26] can sequence attack actions in static/network target environments.
* **B. Limitations Identified:** Formal decision models struggle with unstructured client-side DOM states and dynamic web runtime events.
* **C. Actual Implementation Provides:** State-machine-driven interactive browser workflow (`stateMachine.ts`, `App.tsx`) enforcing origin locking, user consent onboarding, and structured execution.
* **D. Genuinely Different:** Focuses on deterministic, authorization-bounded interactive application analysis rather than unconstrained network exploration.
* **E. Engineering Choice:** Electron state machine UI orchestration.
* **F. Reasonable Research Contribution:** Workflow framing for permissioned, origin-constrained interactive security inspection.
* **G. Experimental Evidence Required:** Task completion speed and operator navigation efficiency compared to manual proxy setups.
* **H. Do NOT Claim:** Fully autonomous multi-host penetration testing or unguided network attack planning.

---

## 2. LLM-Assisted Penetration Testing
* **A. Existing Research Demonstrates:** LLMs can assist human testers with task decomposition, log parsing, and command recommendations (PentestGPT [13], PenHeal [34]).
* **B. Limitations Identified:** Existing tools function as CLI copilots or cloud-dependent chat advisors without direct programmatic DOM interaction or closed-loop evidence validation.
* **C. Actual Implementation Provides:** Local Ollama AI Advisor (`src/advisor/ollama.ts`) providing grounded explanations and multi-framework defensive code patches for verified session findings.
* **D. Genuinely Different:** LLM is restricted to defensive guidance and evidence-grounded remediation, explicitly disallowing offensive exploit string generation.
* **E. Engineering Choice:** Prompt template formatting and system message guardrails.
* **F. Reasonable Research Contribution:** Evidence-grounded defensive LLM copilot architecture for web vulnerability remediation.
* **G. Experimental Evidence Required:** Developer comprehension metrics and remediation correctness evaluations.
* **H. Do NOT Claim:** Autonomous offensive payload generation or unguided exploitation.

---

## 3. LLM Security Agents
* **A. Existing Research Demonstrates:** Specialized agents and RAG enhance domain knowledge retrieval during security workflows (PentestAgent [27], CAMEL [54]).
* **B. Limitations Identified:** Multi-agent swarms introduce high latency, token consumption, and coordination overhead.
* **C. Actual Implementation Provides:** Single integrated desktop agent engine coordinating live CDP interception, rules, canary probing, replay verification, and local LLM advising.
* **D. Genuinely Different:** Unified single-process architecture coupling dynamic browser instrumentation directly with a local LLM advisor.
* **E. Engineering Choice:** Single-process Electron IPC architecture vs. microservices.
* **F. Reasonable Research Contribution:** Low-overhead unified architecture for browser-grounded AI security inspection.
* **G. Experimental Evidence Required:** Resource footprint and memory benchmarking vs. multi-agent swarms.
* **H. Do NOT Claim:** Autonomous multi-agent offensive swarm capabilities.

---

## 4. Browser-Based Security Testing
* **A. Existing Research Demonstrates:** Dynamic web application testing requires interaction with DOM states and HTTP traffic (OWASP ZAP [48], Nmap [61]).
* **B. Limitations Identified:** Traditional web testing tools operate external to the rendering engine or lack integrated AI reasoning.
* **C. Actual Implementation Provides:** Programmatic Electron `WebContentsView` with attached Chrome DevTools Protocol (`1.3`) capturing DOM mutations, console exceptions, and WebSocket frames (`electron/main.cjs`).
* **D. Genuinely Different:** Native deep browser rendering integration via CDP coupled directly with rule and LLM reasoning pipelines.
* **E. Engineering Choice:** Using Electron `WebContentsView` and CDP debugger protocol APIs.
* **F. Reasonable Research Contribution:** CDP-instrumented browser testing harness for evidence-grounded AI security inspection.
* **G. Experimental Evidence Required:** Coverage of client-side DOM states vs. external proxy crawlers.
* **H. Do NOT Claim:** Novel browser engine or custom browser rendering technology.

---

## 5. Vulnerability Detection
* **A. Existing Research Demonstrates:** Passive pattern matching and active fuzzing detect common web vulnerabilities (NAUTILUS [2], OWASP Top 10 [66]).
* **B. Limitations Identified:** High false-positive rates in static/passive tools; dangerous payload fuzzing in active tools.
* **C. Actual Implementation Provides:** Dual-engine detection combining 11 passive HTTP/DOM rules (`rules.ts`) with active inert canary token reflection probing (`canary.ts`).
* **D. Genuinely Different:** Inert active probing using non-destructive random tokens (`generateCanaryToken`) to detect output encoding weaknesses across 5 DOM/script contexts without executing malicious payloads.
* **E. Engineering Choice:** Rule definitions for CSP, HSTS, CORS, and cookie flags.
* **F. Reasonable Research Contribution:** Inert canary reflection detection mechanism for non-destructive XSS/reflection discovery.
* **G. Experimental Evidence Required:** Detection accuracy and reflection context precision on benchmark applications (e.g., OWASP Benchmark [65], DVWA).
* **H. Do NOT Claim:** Discovery of novel zero-day vulnerability classes or generic fuzzing superiority.

---

## 6. Vulnerability Verification
* **A. Existing Research Demonstrates:** Verification is essential to distinguish true vulnerabilities from static noise (Fang et al. [11], APT-Agent [7]).
* **B. Limitations Identified:** Existing LLM pentesting systems report unverified hypotheses directly to users without validating state changes.
* **C. Actual Implementation Provides:** Replay Comparator Engine (`src/engine/replay.ts`) that executes targeted re-tests, evaluates new evidence streams, and classifies findings as `Fixed`, `Still Present`, or `Not Comparable`.
* **D. Genuinely Different:** Deterministic evidence-comparison loop validating whether a vulnerability persists post-remediation.
* **E. Engineering Choice:** String matching and finding state comparison algorithms.
* **F. Reasonable Research Contribution:** Replay-based verification loop for AI-identified application security findings.
* **G. Experimental Evidence Required:** False-positive reduction rate and verification accuracy on baseline vs. remediated targets.
* **H. Do NOT Claim:** Formal verification or mathematical proof of code safety.

---

## 7. False-Positive Reduction
* **A. Existing Research Demonstrates:** Automated security tools suffer from high false-positive rates, exhausting security engineering resources.
* **B. Limitations Identified:** Passive tools flag missing headers without checking context; LLMs generate hallucinated vulnerabilities [15], [17].
* **C. Actual Implementation Provides:** Multi-stage filtering pipeline combining RFC-compliant rule checks, inert canary context analysis, and replay comparison (`rules.ts`, `canary.ts`, `replay.ts`).
* **D. Genuinely Different:** Replay comparison and header differencing (`computeHeaderDiff`) explicitly remove resolved findings from active reporting.
* **E. Engineering Choice:** Thresholds and severity mappings.
* **F. Reasonable Research Contribution:** Empirical false-positive mitigation strategy integrating passive rules, inert canary probing, and replay verification.
* **G. Experimental Evidence Required:** Comparative false-positive rates against unverified scanner output on OWASP Benchmark.
* **H. Do NOT Claim:** Total elimination of false positives.

---

## 8. Security Evidence Collection
* **A. Existing Research Demonstrates:** Audit trails and evidence logs are critical for security compliance and incident response (NIST [1], PTES [72]).
* **B. Limitations Identified:** Logs are often unstructured, verbose, contain sensitive credentials, or lack cryptographic integrity.
* **C. Actual Implementation Provides:** Structured evidence logging pipeline (`electron/main.cjs`) generating unique event IDs, ISO timestamps, SHA-256 hashes (`computeHash`), automatic sensitive token redaction (`redactSensitiveData`, `redactHeaders`), and rotated storage (`.kilo/archives/`, `evidence.json`).
* **D. Genuinely Different:** Evidence-first design where every finding must reference a cryptographically hashed, redacted evidence record.
* **E. Engineering Choice:** JSON schema design and regex sanitization patterns.
* **F. Reasonable Research Contribution:** Redacted, cryptographically traceable evidence collection model for AI security assistants.
* **G. Experimental Evidence Required:** Redaction accuracy across sensitive header/body formats and storage efficiency.
* **H. Do NOT Claim:** Immutable blockchain storage or forensic-grade hardware attestation.

---

## 9. Evidence-Grounded LLM Reasoning
* **A. Existing Research Demonstrates:** Grounding LLM prompts with domain context reduces output hallucination (RAG [53], Chain-of-Thought [77]).
* **B. Limitations Identified:** Standard LLM security advisors may invent non-existent evidence IDs or cite arbitrary log entries.
* **C. Actual Implementation Provides:** Citation validation engine (`parseAndValidateAdvisorResponse` in `src/advisor/ollama.ts`) checking `isGrounded` by verifying that LLM-cited evidence IDs exist in the active evidence store.
* **D. Genuinely Different:** Post-generation citation validation mechanism that detects and flags ungrounded evidence references.
* **E. Engineering Choice:** Set intersection check (`citedEvidenceIds.every(id => availableIds.has(id))`).
* **F. Reasonable Research Contribution:** Evidence-grounded citation validation method for LLM security advisors.
* **G. Experimental Evidence Required:** Grounding success rate (percentage of responses where `isGrounded === true`) across test runs.
* **H. Do NOT Claim:** Perfect semantic grounding or complete elimination of LLM reasoning mistakes.

---

## 10. Hallucination Mitigation
* **A. Existing Research Demonstrates:** LLMs suffer from technical hallucinations, generating invalid command syntax or incorrect parameters [7], [15], [17].
* **B. Limitations Identified:** Existing security agents rely on prompt instructions alone to suppress hallucinations.
* **C. Actual Implementation Provides:** Three-tier mitigation: (1) Low temperature (0.2) + JSON format constraint in Ollama IPC (`electron/main.cjs`), (2) Offline knowledge base injection (`getOfflineKnowledge`), (3) Fallback deterministic patch generator (`getDefaultDeterministicPatches`).
* **D. Genuinely Different:** Hybrid architecture using offline rule-based knowledge injection combined with deterministic fallback patches when LLM parsing fails.
* **E. Engineering Choice:** Default patch snippets for CWE-79, CWE-614, and Helmet/Express.
* **F. Reasonable Research Contribution:** Hybrid fallback architecture for resilient LLM security advisory systems.
* **G. Experimental Evidence Required:** Parsing failure rate and fallback activation frequency under constrained local models.
* **H. Do NOT Claim:** Complete elimination of LLM hallucination in unconstrained text generation.

---

## 11. Context Management
* **A. Existing Research Demonstrates:** Long-horizon pentesting requires maintaining state across multi-step tasks (APT-Agent [7]).
* **B. Limitations Identified:** Context window limits lead to token truncation, memory degradation, or high API costs.
* **C. Actual Implementation Provides:** Dual-layer state management: in-memory event store (`evidenceStore`) rotated at 1000 items (`rotateEvidenceStoreIfNeeded`), combined with sanitized evidence extraction (`buildQuarantinedPrompt` slicing detail to 300 chars / meta to 400 chars).
* **D. Genuinely Different:** Quarantined, windowed context construction that extracts relevant evidence snippets while preserving strict prompt budget limits.
* **E. Engineering Choice:** Slicing limits (300/400 chars) and 1000-record store cap.
* **F. Reasonable Research Contribution:** Context windowing and evidence quarantine protocol for local LLM security inspection.
* **G. Experimental Evidence Required:** Token utilization and state retention accuracy over long testing sessions.
* **H. Do NOT Claim:** Infinite context window or long-term vector memory database.

---

## 12. Local LLM Execution
* **A. Existing Research Demonstrates:** Running open-weight models locally protects data privacy but introduces resource and latency constraints [5], [6].
* **B. Limitations Identified:** Local 7B/8B models have lower reasoning capacity and smaller context windows than frontier cloud models (e.g., GPT-4o [32]).
* **C. Actual Implementation Provides:** Local Ollama integration (`127.0.0.1:11434`) using `llama3:latest`, enforcing local loopback restriction (`isLoopbackHost`) and HTTP request timeouts (`electron/main.cjs`).
* **D. Genuinely Different:** Fully contained local execution pipeline ensuring no security findings or application telemetry leave the local host.
* **E. Engineering Choice:** HTTP client calls to Ollama REST endpoints.
* **F. Reasonable Research Contribution:** Characterization of local open-weight LLM performance in evidence-grounded security advisory tasks.
* **G. Experimental Evidence Required:** Inference latency, token generation speed, and RAM/VRAM utilization on standard hardware.
* **H. Do NOT Claim:** Performance equivalence to frontier cloud LLMs (e.g., GPT-4).

---

## 13. Privacy-Preserving Security Analysis
* **A. Existing Research Demonstrates:** Cloud-based security tools risk leaking proprietary code, API keys, and vulnerability details to third parties.
* **B. Limitations Identified:** Existing autonomous pentesting agents (Fang et al. [11], PentestGPT [13]) route targets and logs through commercial cloud APIs.
* **C. Actual Implementation Provides:** Privacy-by-design architecture: local LLM, in-memory browser partition (`in-memory-lab`), loopback-only communication, origin locking, and automatic credential redaction.
* **D. Genuinely Different:** Strict zero-cloud-data-leakage architecture for application security inspection.
* **E. Engineering Choice:** Setting `partition: 'in-memory-lab'` and regex redaction rules.
* **F. Reasonable Research Contribution:** Privacy-preserving design pattern for desktop-based AI security inspection tools.
* **G. Experimental Evidence Required:** Verification of zero external network traffic during security inspection runs.
* **H. Do NOT Claim:** Zero-trust cryptographic proof or hardware enclave isolation.

---

## 14. Automated Remediation
* **A. Existing Research Demonstrates:** Automated patching and remediation guidance accelerate vulnerability resolution (PenHeal [34]).
* **B. Limitations Identified:** Automated code modifications can introduce breaking changes or syntax errors if unverified.
* **C. Actual Implementation Provides:** Multi-framework defensive code patch generator (`ollama.ts`) providing tailored code fixes across React, Node.js/Express, Next.js, and Python (FastAPI/Django).
* **D. Genuinely Different:** Multi-framework defensive patch generation coupled with deterministic fallback snippets.
* **E. Engineering Choice:** Framework selection (React, Express, Next.js, FastAPI, Django).
* **F. Reasonable Research Contribution:** Multi-framework defensive remediation template system grounded in verified findings.
* **G. Experimental Evidence Required:** Code patch syntax validity and remediation success rate across frameworks.
* **H. Do NOT Claim:** Fully automated autonomous code refactoring or auto-committing git patches.

---

## 15. Replay-Based Verification
* **A. Existing Research Demonstrates:** Regression testing verifies that reported software defects have been resolved.
* **B. Limitations Identified:** Security tools rarely re-test specific findings against prior baseline evidence automatically.
* **C. Actual Implementation Provides:** `compareReplayEvidence` function (`src/engine/replay.ts`) performing header differencing (`computeHeaderDiff`) and finding re-evaluation against historical baselines.
* **D. Genuinely Different:** Differential evidence replay engine specifically designed for verifying security finding status post-remediation.
* **E. Engineering Choice:** Header diff categorization (`added`, `removed`, `modified`, `unchanged`).
* **F. Reasonable Research Contribution:** Differential replay verification method for web application security findings.
* **G. Experimental Evidence Required:** Replay classification accuracy on baseline vs. remediated application runs.
* **H. Do NOT Claim:** Dynamic binary symbolic execution or formal program verification.

---

## 16. Security Scanner Integration
* **A. Existing Research Demonstrates:** Standard security tools produce structured outputs (SARIF v2.1.0, ZAP JSON) for tool interoperability.
* **B. Limitations Identified:** Raw scanner outputs lack interactive verification and evidence-grounded AI advice.
* **C. Actual Implementation Provides:** Unified ingest engine (`src/engine/ingest.ts`) parsing SARIF v2.1.0 (Nuclei, CodeQL) and OWASP ZAP reports, mapping findings into the internal evidence timeline.
* **D. Genuinely Different:** Harmonizing external scanner findings with live browser CDP evidence and local AI advising.
* **E. Engineering Choice:** JSON schema parsers for SARIF and ZAP formats.
* **F. Reasonable Research Contribution:** Unified evidence-model architecture integrating external scanner findings with live browser inspection.
* **G. Experimental Evidence Required:** Ingestion accuracy and mapping correctness across diverse SARIF/ZAP log files.
* **H. Do NOT Claim:** Replacement of underlying scanner engines (Nuclei, ZAP).

---

## 17. Reproducibility of AI-Assisted Security Testing
* **A. Existing Research Demonstrates:** AI security research suffers from reproducibility issues due to non-deterministic model outputs and unrecorded target environments.
* **B. Limitations Identified:** Cloud API updates and unrecorded browser states prevent exact reproduction of published AI pentesting experiments.
* **C. Actual Implementation Provides:** Evidence-first architecture saving deterministic event logs with SHA-256 hashes (`evidence.json`), fixed Ollama temperature settings (0.2), and automated integration test suites (`tests/engine.test.ts`, `tests/e2e-fixture.test.ts`).
* **D. Genuinely Different:** Audit-grade reproducible security testing framework with hashed evidence chains and local model hosting.
* **E. Engineering Choice:** Using Node.js `crypto` for SHA-256 hashing.
* **F. Reasonable Research Contribution:** Reproducible framework for desktop AI-assisted security inspection research.
* **G. Experimental Evidence Required:** Test suite repeatability across multiple execution runs on fixed target fixtures.
* **H. Do NOT Claim:** Absolute mathematical determinism in stochastic LLM generation.
