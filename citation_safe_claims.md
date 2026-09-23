# Verified Citation-Safe Claims for Research Paper

This artifact documents all verified, citation-safe claims ready for inclusion in the IEEE research paper draft (`research/paper_draft_v1.md`). Every statement listed here is grounded directly in the audited literature (`research/citation_grounding_audit.md`) and the actual implementation of **Sentinel Desktop** (`Major Project/`).

---

## 1. Citation-Safe Literature Claims

### A. Automated Penetration Testing & Standards
* **NIST SP 800-115 `[1]`:** NIST Special Publication 800-115 establishes standard technical guidelines for security testing, categorizing assessments into target identification, discovery, vulnerability analysis, and verification phases.
* **NAUTILUS (Deng et al.) `[2]`:** NAUTILUS introduced structured feedback and coverage guidance for automated RESTful API vulnerability detection.

### B. LLM Security Testing & Agents
* **PentestGPT (Deng et al.) `[13]`:** PentestGPT introduced an interactive penetration-testing assistant powered by cloud-hosted LLM APIs that assists human testers with subtask planning and command generation over terminal outputs.
* **Fang et al. `[11]`:** Fang et al. demonstrated that LLM-based agents equipped with web interaction tools can autonomously navigate web applications and execute offensive exploits against target websites.
* **AutoAttacker (Xu et al.) `[14]`:** AutoAttacker demonstrated LLM-guided decision-making for automating cyber-attack execution sequences.
* **PentestAgent (Shen et al.) `[27]`:** PentestAgent combined domain-specific multi-agent roles with Retrieval-Augmented Generation (RAG) to support automated penetration testing phases.

### C. Reliability, Hallucination, & Structured Reasoning
* **Happe & Cito `[50]`:** Happe and Cito demonstrated that LLMs in security testing frequently suffer from technical hallucinations, syntax errors, and non-reproducible outputs when operating over command-line interfaces.
* **Zhang et al. `[15]`:** Zhang et al. showed that uncorrected hallucinations early in a multi-step reasoning chain compound over subsequent iterations, leading to systemic failure chains.
* **SelfCheckGPT (Manakul et al.) `[17]`:** SelfCheckGPT established zero-resource factual consistency detection for LLMs by evaluating stochastic sampling agreement across generated responses.
* **Structured Output (Liu et al.) `[56]`:** Liu et al. demonstrated that enforcing structured output constraints on LLM generations improves formatting compliance and downstream parsing reliability.

---

## 2. Verified Claims Connecting Sentinel Desktop to Literature

1. **Local Privacy Containment:**
   * *Claim:* Sentinel Desktop addresses data confidentiality concerns associated with cloud-hosted security tools (`[11]`, `[13]`) by confining LLM inference strictly to local loopback endpoints (`127.0.0.1:11434`) via `src/advisor/ollama.ts`.
2. **Browser Instrumentation vs. CLI Bias:**
   * *Claim:* Sentinel Desktop addresses terminal/CLI limitations documented in prior LLM pentesting evaluations (`[13]`, `[50]`) by using Chrome DevTools Protocol (`1.3`) to observe dynamic client-side DOM states, console errors, and HTTP header streams.
3. **Structured Response Parsing:**
   * *Claim:* Aligned with structured output research (`[56]`), Sentinel Desktop enforces structured JSON format constraints on local LLM recommendations to prevent unconstrained output drift and ensure reliable evidence mapping.
4. **Citation Grounding Validation:**
   * *Claim:* To address generative hallucination risks in AI-assisted security (`[15]`, `[17]`, `[50]`), Sentinel Desktop implements deterministic citation validation (`parseAndValidateAdvisorResponse`), verifying that all evidence IDs cited in remediation advice exist in the local `evidenceStore`.
5. **Deterministic Vulnerability Verification:**
   * *Claim:* In contrast to systems that report unverified vulnerability hypotheses (`[11]`, `[14]`), Sentinel Desktop implements a closed-loop differential replay engine (`replay.ts`) that computes HTTP header diffs between baseline and re-test evidence streams.

---

## 3. Explicit Claim Boundaries (What CANNOT Be Claimed)

To maintain scientific integrity, the paper **MUST NOT** claim:
* That PentestGPT or Fang et al. evaluated local LLMs (they evaluated cloud APIs).
* That SelfCheckGPT's stochastic sampling algorithm is implemented in Sentinel Desktop (Sentinel uses deterministic evidence ID lookup `citedEvidenceIds.every(...)`).
* That NAUTILUS or NIST SP 800-115 evaluate dynamic client-side DOM reflection.
* That Sentinel Desktop provides formal mathematical verification or symbolic execution (it provides empirical differential replay verification).
* That Sentinel Desktop is an autonomous offensive penetration testing swarm (it is a defensive, interactive application security assistant).
* Empirical performance results for Ollama/Llama 3 (Experiments 4 & 6 were unexecuted due to missing host dependencies).
