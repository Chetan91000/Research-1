# Pre-IEEE Review

This document summarizes the evidence-grounded corrections applied to `research/paper_draft_v1.md` to produce `research/paper_draft_v2.md` and assesses the readiness of the manuscript for IEEE LaTeX conversion.

## Claims Corrected
1. **Privacy Claims Scope:** Overly absolute statements such as "eliminates third-party telemetry leakage" were corrected to "reduces external telemetry leakage" and grounded in "local loopback confinement."
2. **Field-Wide Generalizations:** Unsupported generalizations like "existing security agents rely primarily on..." and "existing LLM-assisted systems predominantly rely..." were corrected to "Several recent security agents rely on..." to avoid dismissing unexamined literature.
3. **Deterministic Scope:** Uses of "deterministic replay verification" were narrowed to "deterministic replay comparison." The text now explicitly avoids implying that the entire system (including LLM generation) is fully deterministic, reserving that trait for the replay engine (`replay.ts`).
4. **Scanner Interoperability:** Experiment 5 reporting was clarified to ensure that 100% mapping accuracy refers *strictly* to the specifically tested SARIF v2.1.0 and OWASP ZAP fixtures, explicitly preventing the implication of universal scanner schema interoperability.

## Claims Removed
- No specific full claims were outright removed, as the previous draft was already tightly constrained by the citation audit. Instead, boundary claims were weakened (see above).
- Removed absolute language regarding privacy and sweeping generalizations of the entire LLM agent field.

## References Retained
The bibliography was fully restructured into three distinct categories without fabricating any metadata:
**A. Core Research References** (9 references directly motivating or contrasting with Sentinel):
- `[2]`, `[11]`, `[13]`, `[14]`, `[15]`, `[17]`, `[27]`, `[50]`, `[56]`. (Note: NIST [1] was moved to Standards).
**B. Standards and Guidelines** (2 references):
- `[1]` NIST SP 800-115, `[72]` PTES Technical Guidelines.
**C. Supporting References** (21 references):
- Included foundational literature on LLMs, POMDP, RL, Attack Graphs, and general LLM capabilities (`[5]`, `[7]`, `[10]`, `[12]`, `[22]`, `[23]`, `[24]`, `[25]`, `[26]`, `[30]`, `[37]`, `[38]`, `[39]`, `[46]`, `[47]`, `[51]`, `[53]`, `[54]`, `[68]`, `[69]`, `[78]`).

## References Removed
- **None.** Every reference included in the bibliography of `paper_draft_v1.md` was verified to be actively cited in the text. No unused references were present to remove.

## Remaining Citation Issues
- **None.** The bibliography precisely reflects the 32 citations used in the text. The 10 core audited papers form the backbone of the research gap, while standards and supplementary RL/POMDP papers provide necessary background context.

## Remaining Technical Issues
- The LLM components (Experiments 4 and 6) remain unexecuted due to the host environment lacking an active Ollama installation. The paper explicitly addresses this, shifting the focus to the deterministic browser instrumentation, canary probing, rules, and replay engines.
- The `ATTRIBUTE` context limitation in inert canary probing (due to sequential DOM string scanning in `analyzeDomReflection`) remains unresolved in code, but is transparently documented in the paper as a limitation.

## Remaining Experimental Limitations
- **Local Loopback Latency:** All execution telemetry reflects local loopback latency (< 1.2 ms mean), which will not represent performance over remote networks.
- **Fixture Scale:** The evaluation relies on a synthetic fixture server (`fixtureServer.cjs`) rather than real-world, multi-origin enterprise applications.
- **Sample Size:** 130 total physical trials.

## Readiness for IEEE LaTeX Conversion
**Yes, the paper is ready for IEEE LaTeX conversion.**
The draft strictly adheres to evidence constraints, avoids hallucinated results, categorizes the literature accurately without metadata fabrication, transparently acknowledges the unexecuted LLM experiments, and maintains an objective, neutral academic tone. No further structural or narrative modifications are required prior to typesetting.
