# Final Paper Claim Audit Matrix

This document presents the final self-audit verifying every major contribution, literature claim, implementation claim, numerical result, research gap, and limitation presented in `research/paper_draft_v1.md`. 

Every item has been cross-checked against raw experimental JSON data (`research/results/`), the citation-grounding audit (`research/citation_grounding_audit.md`), source code files (`Major Project/`), and verified literature summaries.

---

## 1. Claim Audit Verification Matrix

| # | Claim Made in Paper | Evidence Source | Supported? | Location in Paper |
|---|---|---|---|---|
| 1 | **Replay Verification Performance:** Replay engine achieved 30/30 correct classifications (15 TP, 15 TN, 0 FP, 0 FN) with 1.12 ms mean latency under local fixture conditions. | `research/results/exp1_replay.json`, `group_a_statistical_analysis.md` | **SUPPORTED** | Abstract, Section VII-A, Table II, Table VI |
| 2 | **Inert Canary Reflection Detection:** Inert canary engine achieved 100% binary reflection detection across 50 trials (40 TP, 10 TN, 0 FP, 0 FN) with 0.26 ms mean latency. | `research/results/exp2_canary.json`, `group_a_statistical_analysis.md` | **SUPPORTED** | Abstract, Section VII-B, Table III, Table VI |
| 3 | **Sequential DOM Scanning Limitation:** In Exp 2, 15 `ATTRIBUTE` reflections were categorized under `HTML_BODY` because sequential string parsing returns the first match. | `research/results/exp2_canary.json`, `src/engine/canary.ts`, `group_a_statistical_analysis.md` | **SUPPORTED** | Abstract, Section VII-B, Section VIII-A, Section IX |
| 4 | **Passive Rule Fidelity:** `CSP_MISSING_CHECK` evaluated 30 response streams with 15 TP, 15 TN, 0 FP, 0 FN, and 0.36 ms mean latency. | `research/results/exp3_rules.json`, `src/engine/rules.ts`, `group_a_statistical_analysis.md` | **SUPPORTED** | Abstract, Section VII-C, Table IV, Table VI |
| 5 | **Scanner Ingestion Accuracy:** 20/20 report files (10 SARIF, 10 ZAP) parsed successfully and mapped 100% to OWASP 2021 `A03:2021-Injection`. | `research/results/exp5_scanner.json`, `src/engine/ingest.ts`, `group_a_statistical_analysis.md` | **SUPPORTED** | Abstract, Section VII-D, Table V, Table VI |
| 6 | **Unexecuted Local LLM Experiments:** Local LLM experiments (Exps 4 & 6) were unexecuted because Ollama was not installed/running on the evaluation host. | Physical execution logs, `group_a_execution_report.md` | **SUPPORTED** | Abstract, Section VII (Note), Section VIII-B, Section IX |
| 7 | **No Invented LLM Metrics:** Zero empirical latency, VRAM, or grounding scores are reported for Ollama models. | `research/paper_draft_v1.md` inspection | **SUPPORTED** | Section VII, Section VIII-B |
| 8 | **PentestGPT Literature Claim:** PentestGPT uses cloud LLM APIs to assist human testers with subtask planning over CLI outputs. | `[13]` Deng et al. (2023), `citation_grounding_audit.md` | **SUPPORTED** | Section I, Section II-B, Section II-E |
| 9 | **Fang et al. Literature Claim:** LLM agents equipped with browser tools can navigate web applications and execute offensive exploits. | `[11]` Fang et al. (2024), `citation_grounding_audit.md` | **SUPPORTED** | Section I, Section II-C, Section II-E |
| 10 | **Happe & Cito Literature Claim:** LLMs in pentesting frequently suffer from technical hallucinations, syntax errors, and CLI bias. | `[50]` Happe & Cito (2023), `citation_grounding_audit.md` | **SUPPORTED** | Section I, Section II-B, Section III |
| 11 | **SelfCheckGPT Literature Claim:** SelfCheckGPT provides zero-resource factual hallucination detection via stochastic sampling consistency. | `[17]` Manakul et al. (2023), `citation_grounding_audit.md` | **SUPPORTED** | Section II-D, Section IV-B |
| 12 | **Liu et al. Literature Claim:** Structured output constraints on LLM generations improve formatting compliance and downstream parsing. | `[56]` Liu et al. (2024), `citation_grounding_audit.md` | **SUPPORTED** | Section II-D, Section IV-B, Section V |
| 13 | **Zhang et al. Literature Claim:** Uncorrected early hallucinations in multi-step reasoning compound over subsequent iterations. | `[15]` Zhang et al. (2023), `citation_grounding_audit.md` | **SUPPORTED** | Section I, Section II-D, Section VIII |
| 14 | **NIST SP 800-115 Claim:** Defines standard technical guidelines for security testing, categorizing target discovery, analysis, and verification. | `[1]` NIST SP 800-115 (2008), `citation_grounding_audit.md` | **SUPPORTED** | Section I, Section II-A, Section III |
| 15 | **Local Host Isolation Implementation:** Local AI module checks `isLoopbackHost` and isolates browser view using `partition: 'in-memory-lab'`. | `electron/main.cjs`, `src/advisor/ollama.ts` | **SUPPORTED** | Section IV-B, Section IV-C, Section V |
| 16 | **Citation Grounding Check Implementation:** Advisor response validation checks `isGrounded = citedEvidenceIds.every(...)`. | `src/advisor/ollama.ts` | **SUPPORTED** | Section IV-B, Section V |
| 17 | **Sensitive Data Redaction Implementation:** Credentials undergo automatic regex redaction (`redactSensitiveData`) before persistence. | `src/engine/evidenceStore.ts` | **SUPPORTED** | Section IV-G |
| 18 | **No Unsupported Superiority Words:** Zero occurrences of "state-of-the-art", "superior", "best", "guarantees", "proves", or "perfect accuracy". | `research/paper_draft_v1.md` full text search | **SUPPORTED** | Entire Document |
| 19 | **No Unevidenced Claims:** Zero claims of formal verification, symbolic execution, autonomous offensive exploitation, or pentest swarms. | `research/paper_draft_v1.md` full text search | **SUPPORTED** | Entire Document |
| 20 | **Evidence-Based Limitations:** Explicitly lists synthetic fixture, loopback latency, sequential DOM scanning, small sample size, and unexecuted LLMs. | `group_a_statistical_analysis.md`, `paper_draft_v1.md` | **SUPPORTED** | Section IX |

---

## 2. Summary of Verification Checkpoints

* **Numerical Consistency:** 100% agreement between Table I–VI values in `paper_draft_v1.md` and `exp1_replay.json`, `exp2_canary.json`, `exp3_rules.json`, `exp5_scanner.json`.
* **Literature Grounding:** 100% compliance with `research/citation_grounding_audit.md` safe wording rules.
* **Codebase Alignment:** All described architecture modules, functions, and parameters exist in `Major Project/`.
* **Scientific Integrity:** Strictly neutral academic tone without unevidenced or overstated claims.
