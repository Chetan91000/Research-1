# Core 10 References for Sentinel Desktop Research Paper

This artifact audits the existing reference collection in `research/` and identifies the 10 most relevant references supporting the **Sentinel Desktop** research contribution. 

Each selected reference is classified by its primary **Role** (*FOUNDATIONAL*, *DIRECTLY RELATED*, *METHODOLOGICAL*, or *EVALUATION/BENCHMARK*) and mapped to its technical relevance and corresponding sections in the IEEE paper structure.

---

## 1. Selected Core References Matrix

| # | Reference | Role | Why It Is Relevant | Paper Section(s) Where It Should Be Cited |
|---|---|---|---|---|
| 1 | **G. Deng et al.**, “PentestGPT: An LLM-Empowered Automatic Penetration Testing Tool,” in *Proc. USENIX Security Symp.*, 2023. `[13]` | **DIRECTLY RELATED** | Pioneered task decomposition and guided interactive LLM assistance for penetration testing. Sentinel Desktop directly addresses PentestGPT's reliance on cloud LLMs, lack of dynamic DOM observation, and lack of deterministic verification by providing a fully local, CDP-instrumented interactive assistant. | Section I (Introduction), Section II-B (LLM Security Testing), Section II-E (Research Gap), Section VIII (Discussion) |
| 2 | **R. Fang et al.**, “LLM Agents Can Autonomously Hack Websites,” *arXiv preprint arXiv:2402.06664*, 2024. `[11]` | **DIRECTLY RELATED** | Demonstrated that autonomous LLM agents using tool calls can exploit web application vulnerabilities. Sentinel Desktop builds upon web-testing agent concepts but replaces remote cloud API execution with a local loopback model, non-destructive canary reflection probing, and deterministic replay verification. | Section I (Introduction), Section II-C (Security Agents), Section II-E (Research Gap) |
| 3 | **J. Xu et al.**, “AutoAttacker: A Large Language Model Guided System to Implement Automatic Cyber-Attacks,” *arXiv preprint arXiv:2403.01038*, 2024. `[14]` | **DIRECTLY RELATED** | Formulated an LLM-guided system for automated cyber-attack execution sequences. Serves as a reference point for LLM-driven security testing workflows, contrasting with Sentinel Desktop's defensive, evidence-grounded, and local inspection orientation. | Section I (Introduction), Section II-B (LLM Security Testing), Section II-C (Security Agents) |
| 4 | **X. Shen et al.**, “PentestAgent: Incorporating LLM Agents to Automated Penetration Testing,” *arXiv preprint*, 2025. `[27]` | **DIRECTLY RELATED** | Integrated multi-agent LLM systems with RAG mechanisms for penetration testing tasks. Highlights the operational challenge of context retention over multi-step workflows, which Sentinel Desktop addresses via structured evidence log rotation and citation grounding verification (`isGrounded`). | Section II-C (Security Agents), Section II-E (Research Gap), Section IV-E (Context Management) |
| 5 | **A. Happe and J. Cito**, “Getting Pwn'd by AI: Penetration Testing with Large Language Models,” in *Proc. ACM ESEC/FSE*, 2023. `[50]` | **FOUNDATIONAL** | Provided an early empirical evaluation establishing both the capabilities and severe limitations (hallucinations, non-reproducible outputs, CLI/terminal bias) of LLMs in security testing. Directly motivates Sentinel Desktop's evidence-grounding requirement and browser CDP observation. | Section I (Introduction), Section II-B (LLM Security Testing), Section III (Problem Statement) |
| 6 | **P. Manakul et al.**, “SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models,” in *Proc. Conf. Empirical Methods Nat. Lang. Process. (EMNLP)*, 2023. `[17]` | **METHODOLOGICAL** | Formulated zero-resource techniques to detect LLM hallucinations. Inspires Sentinel Desktop's internal grounding verification interface (`parseAndValidateAdvisorResponse` / `isGrounded`), which verifies that generated remediation advice strictly references valid session evidence IDs. | Section II-D (Evidence Grounding & Reliability), Section IV-B (Local AI Layer), Section V (Implementation) |
| 7 | **G. Deng et al.**, “NAUTILUS: Automated RESTful API Vulnerability Detection,” in *Proc. USENIX Security Symp.*, 2023. `[2]` | **EVALUATION/BENCHMARK** | Established a structured methodology for automated web/API vulnerability detection. Provides an evaluation baseline for dynamic security analysis, comparing with Sentinel Desktop's hybrid browser CDP inspection and multi-scanner ingestion framework. | Section II-C (Security Agents), Section IV-D (Security Analysis), Section VI (Experimental Methodology) |
| 8 | **National Institute of Standards and Technology (NIST)**, “Technical Guide to Information Security Testing and Assessment,” Special Publication 800-115, 2008. `[1]` | **FOUNDATIONAL** | Standard industry reference defining security testing phases, technical assessment methodologies, and vulnerability verification procedures. Provides the foundational process model upon which Sentinel Desktop structures its testing and reporting workflow. | Section I (Introduction), Section II-A (Automated Penetration Testing), Section III (Problem Statement) |
| 9 | **M. X. Liu et al.**, “We Need Structured Output: Towards User-Centered Constraints on Large Language Model Output,” *arXiv preprint*, 2024. `[56]` | **METHODOLOGICAL** | Defined structured output constraints and schema enforcement mechanisms for LLMs. Sentinel Desktop uses structured JSON schema constraints in its local inference handler (`src/advisor/ollama.ts`) to ensure strict system parsing and tool integration without unconstrained output drift. | Section II-D (Evidence Grounding & Reliability), Section IV-B (Local AI Layer), Section V (Implementation) |
| 10 | **M. Zhang et al.**, “How Language Model Hallucinations Can Snowball,” *arXiv preprint arXiv:2305.13534*, 2023. `[15]` | **METHODOLOGICAL** | Analyzed how uncorrected early hallucinations compound into systemic failure chains over multi-step workflows. Sentinel Desktop counters compounding hallucination risks through closed-loop differential replay verification (`replay.ts`) and immutable evidence log hashing (`evidenceStore`). | Section I (Introduction), Section II-D (Evidence Grounding & Reliability), Section VIII (Discussion) |

---

## 2. Rationale & Selection Alignment

### A. Coverage of Key Domain Areas
The selected 10 references cover all core requirements of the Sentinel Desktop research contribution:
1. **Automated Penetration Testing Foundations:** NIST SP 800-115 `[1]`.
2. **LLM Penetration & Security Testing Systems:** PentestGPT `[13]`, Happe & Cito `[50]`, AutoAttacker `[14]`.
3. **LLM Security Agents & Multi-Agent Systems:** Fang et al. `[11]`, PentestAgent `[27]`.
4. **Vulnerability Verification & API Testing:** NAUTILUS `[2]`.
5. **Reliability, Hallucination Mitigation & Evidence Grounding:** SelfCheckGPT `[17]`, Zhang et al. `[15]`, Liu et al. `[56]`.

### B. Grounding Sentinel's Specific Research Gap
Together, these 10 papers establish the four pillars of Sentinel Desktop's research gap:
- **Cloud vs. Local Execution:** Prior systems (`[11]`, `[13]`, `[14]`, `[27]`) rely on cloud AI APIs, whereas Sentinel Desktop operates strictly on local loopback (`127.0.0.1`).
- **CLI vs. DOM Browser Observation:** Prior tools (`[13]`, `[50]`) focus on terminal commands and raw HTTP requests, whereas Sentinel Desktop integrates Chrome DevTools Protocol (`1.3`) browser state tracking.
- **Unverified Claims vs. Replay Verification:** Prior agents (`[11]`, `[14]`) often output unverified vulnerability hypotheses, whereas Sentinel Desktop evaluates closed-loop differential replay (`replay.ts`) and inert canary probing (`canary.ts`).
- **Hallucination Snowballing vs. Citation Validation:** Prior frameworks suffer from compounding reasoning errors (`[15]`), whereas Sentinel Desktop enforces schema constraints (`[56]`) and evidence ID citation validation (`[17]`).
