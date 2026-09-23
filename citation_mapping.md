# Master Citation Mapping & In-Text Alignment

This document synchronizes the in-text citations from the existing research draft with the official **Fully Local AI Master Reference List ([1]–[78])**.

---

## 1. Mapped In-Text Citations

| In-Text Citation in Draft | Paper Referenced in Text | Correct Index in Master Reference List | Verified Bibliographic Entry |
| :--- | :--- | :--- | :--- |
| `[1]` | NIST Guide | `[1]` | National Institute of Standards and Technology, “Technical Guide to Information Security Testing and Assessment,” 2008. |
| `[2]` | NAUTILUS | `[2]` | G. Deng et al., “NAUTILUS: Automated RESTful API Vulnerability Detection,” 2023. |
| `[3]` in Intro / `[13]` in Body | PentestGPT | `[13]` | G. Deng et al., “PentestGPT: An LLM-Empowered Automatic Penetration Testing Tool,” 2023. *(Note: [3] in master list is Jiang et al. Red Teaming)* |
| `[4]` in Intro / `[14]` in Body | AutoAttacker | `[14]` | J. Xu et al., “AutoAttacker: A Large Language Model Guided System to Implement Automatic Cyber-Attacks,” 2024. *(Note: [4] in master list is Abu-Dabaseh Overview)* |
| `[5]` in Intro / `[11]` in Body | Fang et al. (Autonomous Hack) | `[11]` | R. Fang et al., “LLM Agents Can Autonomously Hack Websites,” 2024. *(Note: [5] in master list is Zhao et al. LLM Survey)* |
| `[6]` in Intro / `[27]` in Body | PentestAgent | `[27]` | X. Shen et al., “PentestAgent: Incorporating LLM Agents to Automated Penetration Testing,” 2025. *(Note: [6] in master list is Liu et al. ChatGPT Summary)* |
| `[7]` in Intro / `[7]` in Body | APT-Agent | `[7]` | V. Mayoral-Vilches et al., “ExploitFlow...” *(Note: Text references APT-Agent as [7])* |
| `[8]` | LLM Security Tests | `[8]` | Y. Zhang et al., “How Well Does LLM Generate Security Tests?,” 2023. |
| `[10]` | Red/Blue Teaming LLM | `[10]` | A. Abuadbba et al., “From Promise to Peril: Rethinking Cybersecurity Red and Blue Teaming in the Age of LLMs,” 2026. |
| `[12]` | Fang et al. (One-Day Exploits)| `[12]` | R. Fang et al., “LLM Agents Can Autonomously Exploit One-Day Vulnerabilities,” 2024. |
| `[23]` | POMDP Information-Decay | `[23]` | J. Schwartz et al., “POMDP + Information-Decay: Incorporating Defender's Behaviour in Autonomous Penetration Testing,” 2020. |
| `[24]`–`[26]` | Reinforcement Learning Pentest | `[24]`–`[26]` | Chen et al. [24], Becker et al. [25], Li et al. [26]. |
| `[30]` | POMDP Solving | `[30]` | C. Sarraute et al., “Penetration Testing == POMDP Solving?,” 2013. |
| `[49]` | HackTheBox | `[49]` | HackTheBox, “HackTheBox: Hacking Training for the Best,” 2024. |
| `[50]` | Getting Pwn'd by AI | `[50]` | A. Happe and J. Cito, “Getting Pwn'd by AI: Penetration Testing with Large Language Models,” 2023. |

---

## 2. Strategic Citations to Inject to Strengthen Gaps

| Section / Topic | Claim Needing Citation | Recommended Citation from Master List |
| :--- | :--- | :--- |
| **I. Introduction** | Penetration testing standard methodologies | `[72]` PTES Technical Guidelines; `[46]` Denis et al., Concepts & Strategies |
| **II-A. Background** | Attack graph modeling & automated planning | `[37]` Ammann et al.; `[39]` Boddy et al.; `[47]` Durkota & Lisy |
| **II-C. Agents** | Multi-agent architectures & RAG mechanisms | `[53]` Lewis et al. (RAG); `[54]` Li et al. (CAMEL Agents); `[38]` AutoGPT |
| **II-D. Hallucinations** | Hallucination snowballing & detection | `[15]` Zhang et al. (Snowballing); `[16]` Li et al. (Drowzee); `[17]` Manakul et al. (SelfCheckGPT) |
| **III. Problem Statement** | Ground-truth vulnerability benchmarks | `[65]` OWASP Benchmark; `[66]` OWASP Top 10; `[43]` CVSS Calculator |
| **IV. Proposed System** | Structured LLM constraints & prompting | `[56]` Liu et al. (Structured Output); `[77]` Wei et al. (Chain-of-Thought) |
