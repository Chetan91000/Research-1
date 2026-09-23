# Citation Grounding Audit

This document performs a rigorous citation-grounding audit for the 10 core references identified in `research/core_10_references.md`. Each reference is evaluated to ensure that all claims made in the research paper draft (`research/paper_draft_v1.md`) and citation maps are strictly supported by empirical evidence from the source literature.

---

## Reference Audits

## Reference [13] (Deng et al., 2023 - PentestGPT)

### Intended Claim
PentestGPT relies on cloud-hosted LLM APIs, operates over CLI/terminal subtask outputs without dynamic browser DOM observation, and functions as an interactive copilot rather than an automated verification engine.

### Source Support
Deng et al. [13] introduced PentestGPT using OpenAI's cloud API endpoints (GPT-3.5/GPT-4) to guide human penetration testers through subtask planning and terminal command interpretation. The paper focuses on interactive attack tree decomposition over command-line interfaces.

### Support Level
- **DIRECTLY SUPPORTED** for cloud API reliance and human-in-the-loop copilot focus over terminal interfaces.
- **PARTIALLY SUPPORTED** for lack of dynamic browser observation (the paper targets general pentesting subtasks and CLI commands rather than browser DOM states).

### Safe Academic Wording
"Deng et al. [13] introduced PentestGPT, an interactive penetration-testing assistant powered by cloud-hosted LLM APIs that assists human testers with subtask planning and command generation over terminal outputs."

### Sentinel Connection
Sentinel Desktop replaces cloud API dependencies with a local loopback LLM interface (`127.0.0.1:11434`) and extends security analysis from terminal text to dynamic browser DOM and network events via Chrome DevTools Protocol (`1.3`).

---

## Reference [11] (Fang et al., 2024 - Autonomous Hack)

### Intended Claim
Autonomous LLM agents can navigate web applications and execute offensive exploits, but their reliance on cloud LLMs introduces data confidentiality risks, and their focus is offensive exploitation rather than non-destructive defensive verification.

### Source Support
Fang et al. [11] demonstrated that LLM-based agents equipped with web browser tools (e.g., Playwright) can autonomously navigate web applications, analyze HTML forms, and execute offensive exploit payloads against target websites.

### Support Level
- **DIRECTLY SUPPORTED** for autonomous web application navigation and offensive exploitation capabilities using LLM agents.
- **PARTIALLY SUPPORTED** for privacy/confidentiality concerns (implied by the use of cloud-hosted GPT-4 APIs for processing web application data).

### Safe Academic Wording
"Fang et al. [11] demonstrated that LLM-based agents equipped with web interaction tools can autonomously navigate web applications and execute offensive exploits against target websites."

### Sentinel Connection
While Fang et al. focus on offensive exploit execution using cloud LLMs, Sentinel Desktop applies browser instrumentation to non-destructive defensive inspection (passive security rules, inert canary reflection probing, and differential replay verification) hosted strictly on local loopback.

---

## Reference [14] (Xu et al., 2024 - AutoAttacker)

### Intended Claim
AutoAttacker demonstrates LLM-guided cyber-attack execution workflows, highlighting the trend toward autonomous decision-making in security testing.

### Source Support
Xu et al. [14] proposed AutoAttacker, establishing that Large Language Models can guide multi-stage cyber-attack planning and execution across system boundaries.

### Support Level
- **DIRECTLY SUPPORTED** for LLM-guided automated cyber-attack decision-making and execution sequences.
- **NOT SUPPORTED** for specific claims regarding browser DOM parsing or client-side web UI testing.

### Safe Academic Wording
"Xu et al. [14] proposed AutoAttacker, demonstrating LLM-guided decision-making for automating cyber-attack execution sequences."

### Sentinel Connection
AutoAttacker targets automated offensive attack execution, whereas Sentinel Desktop focuses on non-destructive application security analysis, evidence collection, and deterministic vulnerability remediation verification.

---

## Reference [27] (Shen et al., 2025 - PentestAgent)

### Intended Claim
PentestAgent utilizes domain-specific multi-agent roles augmented with Retrieval-Augmented Generation (RAG) for penetration testing, highlighting the operational challenge of context retention over multi-step workflows.

### Source Support
Shen et al. [27] introduced PentestAgent, demonstrating that decomposing penetration testing across specialized agents (e.g., reconnaissance, exploitation) combined with RAG improves subtask performance.

### Support Level
- **DIRECTLY SUPPORTED** for multi-agent role decomposition and RAG integration in automated penetration testing.
- **PARTIALLY SUPPORTED** for context retention challenges (context decay is a documented driver for RAG and memory management in multi-step agent architectures).

### Safe Academic Wording
"Shen et al. [27] introduced PentestAgent, combining domain-specific multi-agent roles with Retrieval-Augmented Generation (RAG) to support automated security testing phases."

### Sentinel Connection
Sentinel Desktop addresses context retention in local desktop environments by maintaining a structured event store (`evidenceStore`) with automated log rotation at 1,000 events (`rotateEvidenceStoreIfNeeded`) and offline CWE/OWASP knowledge injection (`src/advisor/ollama.ts`).

---

## Reference [50] (Happe & Cito, 2023 - Getting Pwn'd by AI)

### Intended Claim
LLMs applied to penetration testing suffer from technical hallucinations, invalid syntax, non-reproducible outputs, and reliance on command-line tools.

### Source Support
Happe and Cito [50] empirically evaluated LLMs on security testing tasks, documenting frequent syntax errors, non-existent tool flags, non-reproducible session logs, and operational constraints stemming from CLI-focused tool interactions.

### Support Level
- **DIRECTLY SUPPORTED** for LLM hallucinations in security tasks, output non-reproducibility, and terminal/CLI tool limitations.

### Safe Academic Wording
"Happe and Cito [50] demonstrated that LLMs in security testing frequently suffer from technical hallucinations, syntax errors, and non-reproducible outputs when operating over command-line interfaces."

### Sentinel Connection
Sentinel Desktop addresses CLI limitations through dynamic CDP browser state capturing, and mitigates hallucination and non-reproducibility risks via closed-loop differential replay verification (`replay.ts`) and structured schema validation.

---

## Reference [17] (Manakul et al., 2023 - SelfCheckGPT)

### Intended Claim
SelfCheckGPT provides zero-resource hallucination detection for generative LLMs, serving as related literature on validating model factual consistency.

### Source Support
Manakul et al. [17] developed SelfCheckGPT to detect factual hallucinations in black-box generative LLMs by evaluating consistency across multiple stochastically sampled responses without external knowledge bases.

### Support Level
- **DIRECTLY SUPPORTED** as related research on zero-resource LLM hallucination detection.
- **NOT SUPPORTED** as a direct template for Sentinel Desktop's citation validation (Sentinel uses deterministic evidence ID lookup `citedEvidenceIds.every(...)`, not stochastic sampling consistency).

### Safe Academic Wording
"To address generative hallucination, prior research such as SelfCheckGPT (Manakul et al. [17]) has explored zero-resource factual consistency detection for LLMs."

### Sentinel Connection
Whereas SelfCheckGPT measures stochastic consistency across multiple generated outputs, Sentinel Desktop implements explicit citation grounding validation (`parseAndValidateAdvisorResponse`), verifying that every evidence ID cited in LLM advice exists in the local `evidenceStore`.

---

## Reference [2] (Deng et al., 2023 - NAUTILUS)

### Intended Claim
NAUTILUS establishes structured automated vulnerability detection for RESTful APIs using coverage-guided feedback.

### Source Support
Deng et al. [2] presented NAUTILUS, demonstrating automated vulnerability detection for RESTful API endpoints through structured request generation and execution feedback loops.

### Support Level
- **DIRECTLY SUPPORTED** for automated RESTful API vulnerability detection and feedback-guided testing.
- **NOT SUPPORTED** for client-side web browser UI or DOM-based testing (NAUTILUS focuses specifically on REST APIs).

### Safe Academic Wording
"Deng et al. [2] introduced NAUTILUS for automated RESTful API vulnerability detection using structured feedback and coverage guidance."

### Sentinel Connection
Sentinel Desktop complements API-focused testing tools like NAUTILUS by targeting client-side web application behavior, combining browser CDP state tracking, passive security rule evaluation, and scanner report harmonization (SARIF/ZAP).

---

## Reference [1] (NIST, 2008 - SP 800-115)

### Intended Claim
NIST SP 800-115 establishes standard technical guidelines for security testing, categorizing assessments into target identification, discovery, vulnerability analysis, and verification phases.

### Source Support
NIST SP 800-115 [1] provides formal guidelines and technical definitions for information security testing, assessment, and verification methodologies.

### Support Level
- **DIRECTLY SUPPORTED** for standard security testing phases, process definitions, and verification principles.

### Safe Academic Wording
"NIST Special Publication 800-115 [1] establishes standard technical guidelines for security testing, categorizing assessments into target identification, discovery, vulnerability analysis, and verification phases."

### Sentinel Connection
Sentinel Desktop structures its interactive security workflow to align with NIST SP 800-115 phases, linking target observation, passive security rule analysis, and replay verification into a unified evidence model.

---

## Reference [56] (Liu et al., 2024 - Structured Output)

### Intended Claim
Enforcing structured output constraints on LLM generations improves parsing reliability and downstream system integration.

### Source Support
Liu et al. [56] investigated user-centered output constraints on LLMs, demonstrating that schema enforcement (such as JSON or typed templates) significantly improves output adherence and structural validity for downstream applications.

### Support Level
- **DIRECTLY SUPPORTED** for structured output constraints improving LLM compliance and parsing reliability.

### Safe Academic Wording
"Liu et al. [56] demonstrated that enforcing structured output constraints on LLM generations improves formatting compliance and downstream parsing reliability."

### Sentinel Connection
Sentinel Desktop implements structured JSON schema constraints in `src/advisor/ollama.ts` to ensure local LLM advice can be parsed and mapped deterministically to internal evidence records.

---

## Reference [15] (Zhang et al., 2023 - Hallucination Snowballing)

### Intended Claim
Early uncorrected hallucinations in an LLM reasoning sequence compound over multi-step tasks, leading to systemic failure chains.

### Source Support
Zhang et al. [15] demonstrated that when an LLM produces an early hallucination in a multi-step reasoning sequence, subsequent generation steps tend to build upon the false premise, compounding the error rate over time.

### Support Level
- **DIRECTLY SUPPORTED** for compounding hallucination errors over multi-step LLM reasoning chains.
- **PARTIALLY SUPPORTED** as a theoretical motivation for closed-loop verification (the paper evaluates general reasoning tasks, not security replay testing specifically).

### Safe Academic Wording
"Zhang et al. [15] showed that uncorrected hallucinations early in a multi-step reasoning chain compound over subsequent iterations, leading to systemic failure."

### Sentinel Connection
Sentinel Desktop mitigates compounding hallucination risks by decoupling LLM suggestion generation from verification, validating remediation status through deterministic differential replay (`replay.ts`) rather than relying on unverified LLM self-assessment.

---

## Audit of Claims in `citation_mapping.md` to Adjust

1. **PentestGPT (`[13]`) Browser Claims:**
   - *Adjustment:* Weaken claim that PentestGPT "lacks browser interaction". Frame accurately as: "PentestGPT operates over CLI/terminal inputs rather than client-side browser DOM states."
2. **SelfCheckGPT (`[17]`) Grounding Claims:**
   - *Adjustment:* Remove claim that Sentinel's citation grounding is "inspired by SelfCheckGPT's algorithm". Frame accurately as: "While SelfCheckGPT evaluates stochastic sampling consistency, Sentinel Desktop enforces deterministic evidence ID citation checks."
3. **NAUTILUS (`[2]`) Scope Claims:**
   - *Adjustment:* Clarify that NAUTILUS evaluates RESTful APIs, whereas Sentinel Desktop evaluates dynamic client-side web application behavior via CDP.

---

## Final Citation Grounding Summary Table

| Ref | Intended Claim | Source Supports It? | Safe Academic Wording | Paper Section |
|---|---|---|---|---|
| **`[13]`** | PentestGPT relies on cloud APIs & CLI outputs for guided pentesting copilot. | **DIRECTLY SUPPORTED** | "Deng et al. [13] introduced PentestGPT, an interactive penetration-testing assistant powered by cloud-hosted LLM APIs that assists human testers with subtask planning and command generation over terminal outputs." | Section I, Section II-B, Section II-E |
| **`[11]`** | Autonomous LLM agents can navigate websites and execute offensive exploits. | **DIRECTLY SUPPORTED** | "Fang et al. [11] demonstrated that LLM-based agents equipped with web interaction tools can autonomously navigate web applications and execute offensive exploits against target websites." | Section I, Section II-C, Section II-E |
| **`[14]`** | AutoAttacker models LLM-guided attack execution loops. | **DIRECTLY SUPPORTED** | "Xu et al. [14] proposed AutoAttacker, demonstrating LLM-guided decision-making for automating cyber-attack execution sequences." | Section I, Section II-B, Section II-C |
| **`[27]`** | PentestAgent combines multi-agent roles and RAG for pentesting. | **DIRECTLY SUPPORTED** | "Shen et al. [27] introduced PentestAgent, combining domain-specific multi-agent roles with Retrieval-Augmented Generation (RAG) to support automated security testing phases." | Section II-C, Section II-E, Section IV-E |
| **`[50]`** | LLMs in pentesting suffer from hallucinations, non-reproducible outputs, and CLI bias. | **DIRECTLY SUPPORTED** | "Happe and Cito [50] demonstrated that LLMs in security testing frequently suffer from technical hallucinations, syntax errors, and non-reproducible outputs when operating over command-line interfaces." | Section I, Section II-B, Section III |
| **`[17]`** | SelfCheckGPT provides zero-resource factual hallucination detection. | **DIRECTLY SUPPORTED** (as related work) | "To address generative hallucination, prior research such as SelfCheckGPT (Manakul et al. [17]) has explored zero-resource factual consistency detection for LLMs." | Section II-D, Section IV-B, Section V |
| **`[2]`** | NAUTILUS automates REST API vulnerability detection via coverage feedback. | **DIRECTLY SUPPORTED** | "Deng et al. [2] introduced NAUTILUS for automated RESTful API vulnerability detection using structured feedback and coverage guidance." | Section II-C, Section IV-D, Section VI |
| **`[1]`** | NIST SP 800-115 defines standard security testing phases & assessment guidelines. | **DIRECTLY SUPPORTED** | "NIST Special Publication 800-115 [1] establishes standard technical guidelines for security testing, categorizing assessments into target identification, discovery, vulnerability analysis, and verification phases." | Section I, Section II-A, Section III |
| **`[56]`** | Enforcing structured output constraints on LLMs improves parsing reliability. | **DIRECTLY SUPPORTED** | "Liu et al. [56] demonstrated that enforcing structured output constraints on LLM generations improves formatting compliance and downstream parsing reliability." | Section II-D, Section IV-B, Section V |
| **`[15]`** | Uncorrected hallucinations compound into systemic failure over multi-step tasks. | **DIRECTLY SUPPORTED** | "Zhang et al. [15] showed that uncorrected hallucinations early in a multi-step reasoning chain compound over subsequent iterations, leading to systemic failure." | Section I, Section II-D, Section VIII |
