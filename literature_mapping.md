# Detailed Literature Mapping

*(Note: The full text of the 78 reference papers is not available in the workspace. The following analysis is derived strictly from the paper titles/metadata provided in the Master Reference List and the contextual summaries provided in the existing research draft. I have explicitly marked fields that cannot be reliably extracted without the full text as "Not available from metadata alone".)*

---

## 1. LLM-Based Penetration Testing & Agents

### [13] G. Deng et al., “PentestGPT: An LLM-Empowered Automatic Penetration Testing Tool,” 2023.
- **Research Problem:** Manual penetration testing is labor-intensive, and traditional automated tools lack complex reasoning.
- **Proposed Approach:** Using LLMs (GPT models) to guide human testers by reasoning and decomposing tasks.
- **Architecture / Model:** LLM-empowered task decomposition module and reasoning engine (inferred from title/context).
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Can assist with security reasoning and automated attack execution (per existing draft).
- **Limitations:** Relies on external AI (implied by our draft's motivation for local AI).
- **Relevance:** Foundational baseline for LLM-assisted penetration testing.

### [27] X. Shen et al., “PentestAgent: Incorporating LLM Agents to Automated Penetration Testing,” 2025.
- **Research Problem:** Automating penetration testing through intelligent agents.
- **Proposed Approach:** Incorporating specialized LLM agents using retrieval-augmented generation (RAG).
- **Architecture / Model:** Multiple specialized agents utilizing RAG for domain knowledge (per existing draft).
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** RAG and specialized agents improve automated testing capabilities.
- **Limitations:** Not available from metadata alone.
- **Relevance:** Directly supports the architectural choice of agent-based testing (Priority #1, #4, #7).

### [11] R. Fang et al., “LLM Agents Can Autonomously Hack Websites,” 2024.
### [12] R. Fang et al., “LLM Agents Can Autonomously Exploit One-Day Vulnerabilities,” 2024.
- **Research Problem:** Assessing whether LLM agents can independently exploit real-world web vulnerabilities.
- **Proposed Approach:** Autonomous deployment of LLM agents against web targets.
- **Architecture / Model:** LLM autonomous agents.
- **Datasets / Environments:** Websites and One-Day vulnerabilities.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** LLM agents can autonomously hack websites and exploit selected vulnerabilities (per existing draft).
- **Limitations:** Not available from metadata alone.
- **Relevance:** Proves the viability of autonomous web exploitation (Priority #2, #3, #4).

### [14] J. Xu et al., “AutoAttacker: A Large Language Model Guided System to Implement Automatic Cyber-Attacks,” 2024.
- **Research Problem:** Automating the implementation of cyber-attacks.
- **Proposed Approach:** An LLM-guided system for attack execution.
- **Architecture / Model:** LLM-guided attack system.
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Can implement automated cyber-attacks under LLM guidance (per existing draft).
- **Limitations:** Not available from metadata alone.
- **Relevance:** Core literature for automated attack planning (Priority #10).

---

## 2. Hallucination, Reliability, & Contextual Memory

### [7] V. Mayoral-Vilches et al., “ExploitFlow, Cyber Security Exploitation Routes for Game Theory and AI Research in Robotics,” 2023. *(Note: Cited as APT-Agent in draft context)*
- **Research Problem:** Reliability challenges in automated penetration testing, specifically hallucination and memory loss.
- **Proposed Approach:** Investigating the impact of technical hallucination and context loss on long-horizon tasks.
- **Architecture / Model:** Not available from metadata alone.
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Incorrect commands/identifiers and loss of previous info cause multi-step failures (per existing draft).
- **Limitations:** Not available from metadata alone.
- **Relevance:** Highly relevant for defining the problem gap (Priority #5, #6).

### [15] M. Zhang et al., “How Language Model Hallucinations Can Snowball,” 2023.
- **Research Problem:** Hallucinations cascading or "snowballing" during multi-step reasoning.
- **Proposed Approach:** Analyzing hallucination propagation.
- **Architecture / Model:** General LLMs.
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Not available from metadata alone (title implies hallucinations worsen over multi-step tasks).
- **Limitations:** Not available from metadata alone.
- **Relevance:** Supports our Challenge #1 (technical hallucination in multi-stage attacks) (Priority #5).

---

## 3. Browser/Web Application Security & APIs

### [2] G. Deng et al., “NAUTILUS: Automated RESTful API Vulnerability Detection,” 2023.
- **Research Problem:** Automated detection of vulnerabilities in RESTful APIs.
- **Proposed Approach:** NAUTILUS automated detection framework.
- **Architecture / Model:** Not available from metadata alone.
- **Datasets / Environments:** RESTful APIs.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Addresses automated RESTful API vulnerability detection (per existing draft).
- **Limitations:** Not available from metadata alone.
- **Relevance:** Related work for application-layer automated security (Priority #3).

---

## 4. Traditional Automated Penetration Testing Foundations

### [23] J. Schwartz et al., “POMDP + Information-Decay: Incorporating Defender's Behaviour in Autonomous Penetration Testing,” 2020.
### [30] C. Sarraute et al., “Penetration Testing == POMDP Solving?,” 2013.
- **Research Problem:** Formalizing penetration testing decision-making under uncertainty.
- **Proposed Approach:** Modeling penetration testing as Partially Observable Markov Decision Processes (POMDPs).
- **Architecture / Model:** POMDPs.
- **Datasets / Environments:** Not available from metadata alone.
- **Evaluation Methodology:** Not available from metadata alone.
- **Metrics:** Not available from metadata alone.
- **Major Findings:** Penetration testing can be modeled as a sequence of decisions using formal planning (per existing draft).
- **Limitations:** Lacks the dynamic reasoning capabilities of modern LLMs.
- **Relevance:** Foundational baseline for automated penetration testing workflows (Priority #10).
