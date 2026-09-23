# Reference Usage Map for Planned IEEE Paper Structure

This document maps the **10 Core References** (from `research/core_10_references.md`) across all 10 planned sections of the IEEE paper draft (`research/paper_draft_v1.md`).

---

## 1. Comprehensive Section-by-Section Usage Map

| Section | Key Topic / Focus | Core References Applied | Specific Citation Rationale |
|---|---|---|---|
| **I. Introduction** | Web security testing challenges, rise of LLM agents, privacy risks, hallucination, CLI bias | `[1]`, `[11]`, `[13]`, `[14]`, `[15]`, `[50]` | • `[1]` NIST guidelines define standard security testing.<br>• `[13]` PentestGPT & `[14]` AutoAttacker demonstrate LLM pentesting.<br>• `[11]` Fang et al. demonstrate web exploitation agents.<br>• `[50]` Happe & Cito document LLM CLI bias and failure modes.<br>• `[15]` Zhang et al. explain compounding hallucination risks. |
| **II. Background and Related Work** | Systematic literature review across 5 sub-domains | `[1]`, `[2]`, `[11]`, `[13]`, `[14]`, `[15]`, `[17]`, `[27]`, `[50]`, `[56]` | • **II-A (Automated Pentesting):** `[1]` NIST testing guidelines.<br>• **II-B (LLM Security Testing):** `[13]` PentestGPT, `[14]` AutoAttacker, `[50]` Happe & Cito.<br>• **II-C (Security Agents):** `[11]` Fang et al., `[27]` PentestAgent, `[2]` NAUTILUS.<br>• **II-D (Evidence Grounding):** `[15]` Zhang et al. (snowballing), `[17]` SelfCheckGPT, `[56]` Liu et al. (structured output).<br>• **II-E (Research Gap):** Synthesizes limits of `[11]`, `[13]`, `[27]`, `[50]`. |
| **III. Problem Statement & Research Objectives** | Formalizing core research objectives (privacy, DOM observation, active probing, replay verification) | `[1]`, `[11]`, `[13]`, `[50]` | • `[1]` NIST SP 800-115 provides baseline verification taxonomy.<br>• `[50]` Happe & Cito frame the problem of unverified LLM output.<br>• `[13]` PentestGPT & `[11]` Fang et al. motivate fully local execution. |
| **IV. Proposed System** | Architecture of Sentinel Desktop across 7 core modules | `[2]`, `[17]`, `[27]`, `[50]`, `[56]` | • **IV-B (Local AI):** `[56]` Liu et al. (JSON schema constraints), `[17]` SelfCheckGPT (citation grounding verification).<br>• **IV-C (Browser Interaction):** Replaces CLI-only limitation identified in `[50]`.<br>• **IV-D (Security Analysis):** Aligns scanner normalization with structured testing paradigms (`[2]`).<br>• **IV-E (Context Management):** Solves multi-step context degradation highlighted in `[27]`. |
| **V. Implementation** | Concrete code architecture (`src/advisor/ollama.ts`, `canary.ts`, `replay.ts`, `main.cjs`) | `[17]`, `[56]` | • `[56]` Liu et al.: Implemented via structured JSON response parsing.<br>• `[17]` SelfCheckGPT: Implemented via `isGrounded` citation check (`citedEvidenceIds.every(...)`). |
| **VI. Experimental Methodology** | Controlled local fixture setup, independent ground-truth definition, disaggregated metrics | `[1]`, `[2]` | • `[1]` NIST SP 800-115: Grounding verification procedures.<br>• `[2]` NAUTILUS: Structuring repeatable, controlled test conditions and evaluation metrics. |
| **VII. Results** | Empirical evaluation of Group A experiments ($N=130$ trials) | *N/A (Empirical Findings)* | • Reports observed performance metrics for Exp 1, Exp 2, Exp 3, and Exp 5.<br>• Explicitly documents Exps 4 & 6 as blocked due to absent Ollama host. |
| **VIII. Discussion** | Analysis of replay verification, canary probing, scanner ingestion, and LLM limitations | `[11]`, `[13]`, `[15]`, `[17]`, `[27]` | • Compares Sentinel's replay engine against unverified execution in `[11]`, `[13]`, `[27]`.<br>• Discusses hallucination control mechanisms in relation to `[15]` Zhang et al. and `[17]` SelfCheckGPT. |
| **IX. Limitations & Threats to Validity** | Documenting fixture boundaries, sequential DOM scanning, and unexecuted LLM benchmarks | `[11]`, `[27]` | • Acknowledges scale and agent complexity differences compared to cloud-based multi-agent frameworks (`[11]`, `[27]`). |
| **X. Conclusion** | Summary of contributions and future roadmap for local AI benchmarking | `[1]`, `[13]`, `[17]` | • Restates contributions in privacy-preserving local architecture, replay verification, and evidence grounding. |

---

## 2. Supplementary Literature Preservation

While these **10 Core References** form the primary structural spine of the research paper, the remaining 68 references from the master reference list (`[1]–[78]`) remain available in the codebase repository (`research/`) for supplementary context (e.g., RL methods `[24]–[26]`, POMDP models `[23]`, `[30]`, and specific CVE/CWE databases `[60]`, `[66]`).
