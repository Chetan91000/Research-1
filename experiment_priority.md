# Experiment Priority & Research Dependency Matrix

This document categorizes all planned experiments into **CORE**, **SUPPORTING**, or **OPTIONAL** priorities based strictly on their relationship to the central research questions of the IEEE paper.

---

## Experiment Priority Matrix

| Experiment | Priority | Why | Evidence Provided | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| **Exp 1: Replay Verification Classification & Header Differencing** | **CORE** | Directly evaluates the central research contribution: deterministic closed-loop verification of remediated application findings. | Replay classification accuracy, FPR, FNR, header diff correctness. | Local Fixture Server (`fixtureServer.cjs`), `replay.ts`, `rules.ts`. |
| **Exp 2: Inert Canary Token Reflection Context Detection** | **CORE** | Evaluates active non-destructive inspection capability without generating malicious exploit payloads. | Reflection detection rate, context classification precision/recall (HTML_BODY, ATTRIBUTE, SCRIPT_STRING). | Local Fixture Server (`/search`), `canary.ts`, CDP browser execution. |
| **Exp 4: Disaggregated LLM Evaluation (Grounding, Correctness, Latency)** | **CORE** | Directly evaluates the local LLM advisor's citation grounding, defensive code quality, and hardware resource consumption. | Citation Grounding Rate (`isGrounded`), syntax validity rate, defensive correctness score, mean/median/$P_{95}$ latency, tokens/sec, peak VRAM/RAM. | Local Ollama instance (`llama3:latest`), `ollama.ts`, system telemetry tools. |
| **Exp 3: Passive Security Rule Coverage & Precision** | **SUPPORTING** | Validates baseline HTTP header and cookie flag inspection rules that feed evidence into the verification and advisor modules. | Precision, recall, and F1-score across standard OWASP security header misconfigurations. | Local Fixture Server (`/` vs. `/fixed`), `rules.ts`. |
| **Exp 5: External Security Scanner Log Harmonization** | **SUPPORTING** | Demonstrates multi-source tool interoperability by normalizing external scanner alerts into the evidence timeline. | Log ingestion completeness, CWE-to-OWASP mapping accuracy. | SARIF v2.1.0 and ZAP JSON benchmark logs, `ingest.ts`. |
| **Exp 6 (Multi-Model): Local LLM Model Comparison** | **OPTIONAL** | Compares performance across multiple local open-weight model architectures (e.g., Llama 3 8B vs. Mistral 7B). | Comparative inference latency, grounding rates, and memory utilization across model families. | Multiple Ollama model tags installed locally (`llama3`, `mistral`). |

---

## Rationale for Priority Classifications

1. **CORE Experiments (Exps 1, 2, 4):** These three experiments form the empirical core of the IEEE Results section. They directly validate the paper's three main technical claims: deterministic replay verification, non-destructive inert canary inspection, and evidence-grounded local LLM advising.
2. **SUPPORTING Experiments (Exps 3, 5):** These experiments validate foundational pipeline mechanisms (passive rules and scanner ingestion) that support the core engines but do not represent the primary research contribution on their own.
3. **OPTIONAL Experiments (Exp 6):** Comparative benchmarking across multiple model families adds secondary depth to the Discussion section, but is not strictly required to validate the core framework.
