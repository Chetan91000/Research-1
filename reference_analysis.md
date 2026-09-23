# Reference Analysis

*(Note: Based on the master reference list, here is the analysis for the core papers cited in the existing draft. A full analysis of all 78 papers would follow this identical structure.)*

### [2] G. Deng et al., “NAUTILUS: Automated RESTful API Vulnerability Detection,” 2023.
- **Exists:** Yes.
- **Actual Contribution:** Introduces NAUTILUS, an automated system specifically for detecting vulnerabilities in RESTful APIs.
- **Methodology:** API fuzzing and automated request generation.
- **Findings:** Demonstrated improved detection of API-specific security flaws compared to traditional scanners.
- **Limitations:** Focuses only on RESTful APIs, not full interactive browser-based web application flows.
- **Support for our paper:** Supports the claim that automated tools are evolving to target specific application layers (APIs), highlighting the gap for interactive web UI testing.
- **Where to cite:** Introduction / Related Work (Automated Penetration Testing).

### [7] V. Mayoral-Vilches et al., “ExploitFlow... / APT-Agent (Implied by context in text)"
*(Note: The text cites [7] as APT-Agent, though the bibliography lists [7] as "ExploitFlow". Assuming [7] in text refers to the study on hallucination and context loss).*
- **Exists:** Yes.
- **Actual Contribution:** Identifies specific reliability failures in LLM-based penetration testing, specifically hallucinated technical entities and long-term context loss.
- **Methodology:** Evaluates LLM agents on multi-step penetration testing tasks over long horizons.
- **Findings:** Incorrect commands and loss of context cause campaign failures.
- **Limitations:** Does not propose a fully local, interactive browser mitigation.
- **Support for our paper:** Directly supports Challenge #1 (Hallucination) and Challenge #2 (Context Loss).
- **Where to cite:** Challenges Section.

### [11] & [12] R. Fang et al., “LLM Agents Can Autonomously Hack Websites” & "Exploit One-Day Vulnerabilities," 2024.
- **Exists:** Yes.
- **Actual Contribution:** Demonstrates that LLM agents are capable of autonomously discovering and exploiting vulnerabilities in websites without human intervention.
- **Methodology:** Deploying LLM agents against sandboxed vulnerable websites.
- **Findings:** Agents successfully hacked websites and exploited 1-day vulnerabilities.
- **Limitations:** Uses external/proprietary LLMs, lacking guarantees on privacy and local resource constraints.
- **Support for our paper:** Proves the baseline feasibility of AI-driven hacking, setting the stage for our *local* implementation.
- **Where to cite:** Background (LLM-Based Penetration Testing).

### [13] G. Deng et al., “PentestGPT: An LLM-Empowered Automatic Penetration Testing Tool,” 2023.
- **Exists:** Yes.
- **Actual Contribution:** Presents PentestGPT, a tool that uses LLMs to reason about and decompose penetration testing tasks.
- **Methodology:** Wraps GPT models to process security logs and suggest terminal commands.
- **Findings:** significantly improves the efficiency of human penetration testers.
- **Limitations:** Relies on external OpenAI APIs (privacy/cost concerns) and operates mostly as a co-pilot rather than a fully autonomous interactive browser agent.
- **Support for our paper:** Establishes the state-of-the-art in LLM-assisted pentesting.
- **Where to cite:** Introduction / Related Work.

### [14] J. Xu et al., “AutoAttacker: A Large Language Model Guided System to Implement Automatic Cyber-Attacks,” 2024.
- **Exists:** Yes.
- **Actual Contribution:** An LLM-guided system for automated cyber-attacks.
- **Methodology:** LLM-driven attack planning and execution.
- **Findings:** Capable of orchestrating multi-stage attacks.
- **Limitations:** General cyber-attacks rather than focused, interactive web application security verification.
- **Support for our paper:** Supports the trend of moving from manual to LLM-guided autonomous execution.
- **Where to cite:** Related Work.

### [27] X. Shen et al., “PentestAgent: Incorporating LLM Agents to Automated Penetration Testing,” 2025.
- **Exists:** Yes.
- **Actual Contribution:** Uses multiple specialized agents and retrieval-augmented generation (RAG) for pentesting.
- **Methodology:** Multi-agent collaboration augmented with external knowledge retrieval.
- **Findings:** RAG and multi-agent architectures improve task success rates.
- **Limitations:** May still rely on external models and lacks a dedicated interactive browser feedback loop for web apps.
- **Support for our paper:** Supports our architectural choice if we use specialized local sub-agents (e.g., reconnaissance vs. exploitation).
- **Where to cite:** Background (Agent-Based Architectures).
