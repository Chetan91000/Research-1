# IEEE Content Mapping

This document systematically maps the existing research draft ("Fully Local AI-powered Interactive Application Security Lab") into the finalized IEEE structure.

---

### Title
1. **Existing Content to Move:** "Fully Local AI-powered Interactive Application Security Lab"
2. **Needs Rewriting:** Keep as-is or refine slightly for academic convention.
3. **Missing Content:** None.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

---

### Abstract
1. **Existing Content to Move:** Original Abstract (Page 1).
2. **Needs Rewriting:** Change future tense ("The framework will be evaluated...", "The study aims to investigate...") to present/past tense once experimental evaluation is completed.
3. **Missing Content:** Quantitative summary of experimental findings (e.g., detection rate, verification rate, latency).
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** Confirmation of core components (interactive browser, local LLM, verification engine).
6. **Experimental Evidence Needed:** Quantitative benchmark results.

---

### Index Terms (Keywords)
1. **Existing Content to Move:** Web Application Security, LLM, Local AI, Automated Penetration Testing, Browser Automation, Vulnerability Detection.
2. **Needs Rewriting:** Standardize "LLM" to "Large Language Models".
3. **Missing Content:** None.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

---

### I. Introduction
1. **Existing Content to Move:** Section 1 (Page 1–2).
2. **Needs Rewriting:** Integrate the motivating research scope; clearly delineate human-assisted vs. autonomous testing.
3. **Missing Content:** Explicit summary of primary contributions and paper organization roadmap.
4. **Additional References Needed:** Citations for penetration testing lifecycle (e.g., PTES [72], Denis et al. [46]).
5. **Implementation Evidence Needed:** High-level overview of the proposed local architecture.
6. **Experimental Evidence Needed:** None.

---

### II. Background and Related Work

#### A. Automated Penetration Testing
1. **Existing Content to Move:** Section 2 (Page 3, Paragraph 1) and Section Background A (Page 7).
2. **Needs Rewriting:** Merge duplicated sentences regarding MDPs, POMDPs, and Reinforcement Learning.
3. **Missing Content:** Deeper discussion of why discrete state-transition models fail on modern dynamic web applications.
4. **Additional References Needed:** Schwartz et al. [23], Sarraute et al. [30], [68], [69], Chen et al. [24], Becker et al. [25], Li et al. [26].
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

#### B. LLM-Based Penetration Testing
1. **Existing Content to Move:** Section 2 (Page 3, Paragraph 2) and Section Background B (Page 7).
2. **Needs Rewriting:** Consolidate discussions of PentestGPT and AutoAttacker.
3. **Missing Content:** Distinction between CLI/terminal-based LLM tools and web-application-focused tools.
4. **Additional References Needed:** Deng et al. [13], Xu et al. [14], Huang & Zhu [34], Happe & Cito [50].
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

#### C. LLM Agents for Security
1. **Existing Content to Move:** Section 2 (Page 3, Paragraph 3–5) and Section Background B (Page 7).
2. **Needs Rewriting:** Clarify the role of multi-agent architectures and RAG in security testing.
3. **Missing Content:** Specific discussion on autonomous web browsing agents.
4. **Additional References Needed:** Fang et al. [11], [12], Shen et al. [27], Deng et al. [2], Lewis et al. [53], Li et al. [54].
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

#### D. Reliability and Hallucination
1. **Existing Content to Move:** Section 2 (Page 3–4) and Section Background C (Page 7).
2. **Needs Rewriting:** Distinguish general LLM hallucinations from *technical entity hallucinations* (e.g., non-existent command arguments, invalid exploit payloads).
3. **Missing Content:** Formal explanation of compounding error ("snowballing") in multi-step attack planning.
4. **Additional References Needed:** Mayoral-Vilches et al. [7], Zhang et al. [15], Li et al. [16], Manakul et al. [17], Shinn et al. [71].
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

#### E. Research Gap
1. **Existing Content to Move:** Section 2 (Page 4, Paragraph 2) and Section Background D (Page 7–8).
2. **Needs Rewriting:** Synthesize the gap: lack of fully local, browser-grounded, closed-loop verification frameworks.
3. **Missing Content:** Explicit contrast table comparing existing systems against our proposed system.
4. **Additional References Needed:** Master Reference List comparison.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

---

### III. Problem Statement and Research Objectives
1. **Existing Content to Move:** Section 3 ("Challenge #1 to #6", Page 5–6).
2. **Needs Rewriting:** Formalize the 6 challenges into concrete research objectives.
3. **Missing Content:** Mathematical or formal definition of the verification and context-tracking problem.
4. **Additional References Needed:** OWASP [65], [66], CVSS [43], [63].
5. **Implementation Evidence Needed:** Definition of the operational constraints for local models.
6. **Experimental Evidence Needed:** None.

---

### IV. Proposed System (Architecture, Local LLM, Browser, Security Analysis, Context, Verification, Evidence)
1. **Existing Content to Move:** Conceptual mentions from Abstract and Introduction.
2. **Needs Rewriting:** None (Must be drafted from structural specifications).
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Needs full description of:
   * System block diagram / architecture
   * Prompt design and schema enforcement
   * Browser automation pipeline (DOM extraction, network monitoring)
   * Context memory state machine
   * Verification protocol and artifact logging
4. **Additional References Needed:** Structured output constraints [56], prompt engineering [59], [77].
5. **Implementation Evidence Needed:** Functional system design and interface specifications.
6. **Experimental Evidence Needed:** None.

---

### V. Implementation
1. **Existing Content to Move:** None.
2. **Needs Rewriting:** N/A.
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Specific runtime libraries, model quantization formats, and browser automation engines.
4. **Additional References Needed:** Framework references (e.g., Playwright, Ollama/vLLM).
5. **Implementation Evidence Needed:** Source code repository, configuration scripts.
6. **Experimental Evidence Needed:** None.

---

### VI. Experimental Methodology (Environment, Apps, Baselines, Metrics, Procedure)
1. **Existing Content to Move:** Evaluation metrics mentioned in Abstract (Page 1, Paragraph 2).
2. **Needs Rewriting:** Formalize the test methodology into reproducible protocol steps.
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Exact target application versions, baseline configurations, test case catalogs.
4. **Additional References Needed:** OWASP Juice Shop, DVWA [76], OWASP Benchmark [65].
5. **Implementation Evidence Needed:** Test harness scripts.
6. **Experimental Evidence Needed:** Hardware configuration logs.

---

### VII. Results
1. **Existing Content to Move:** None.
2. **Needs Rewriting:** N/A.
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Detection rates, verification rates, latency benchmarks, memory footprint, comparison tables.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** Benchmark execution logs.
6. **Experimental Evidence Needed:** Physical testbed empirical data.

---

### VIII. Discussion
1. **Existing Content to Move:** None.
2. **Needs Rewriting:** N/A.
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Analysis of local model trade-offs vs. cloud APIs, verification efficacy, false positive mitigation.
4. **Additional References Needed:** Comparative literature values.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** Experimental data analysis.

---

### IX. Limitations and Threats to Validity
1. **Existing Content to Move:** Challenge #5 (Local performance constraints).
2. **Needs Rewriting:** Expand into internal, external, and construct validity threats.
3. **Missing Content:** Analysis of model size constraints, synthetic test target limitations.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** Failure case logs.

---

### X. Conclusion
1. **Existing Content to Move:** None.
2. **Needs Rewriting:** N/A.
3. **Missing Content:** **MISSING IN ORIGINAL TEXT.** Summary of verified contributions and future work.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.

---

### References
1. **Existing Content to Move:** Master Research Reference List ([1]–[78]).
2. **Needs Rewriting:** Fix inline citation mismatches and format into standard IEEE citation format.
3. **Missing Content:** None.
4. **Additional References Needed:** None.
5. **Implementation Evidence Needed:** None.
6. **Experimental Evidence Needed:** None.
