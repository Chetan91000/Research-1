# IEEE LaTeX Package for Sentinel Desktop

This directory contains the official IEEE two-column LaTeX conference paper package converted directly from `research/paper_draft_v4.md`.

---

## Directory Structure

```
research/ieee/
├── main.tex                       # Primary IEEE LaTeX manuscript
├── references.bib                 # Verified BibTeX bibliography (32 references)
├── figures/
│   └── system_architecture.pdf    # Vector-style architecture diagram PDF
├── tables/                        # Formatted LaTeX tables embedded in main.tex
├── ieee_conversion_audit.md       # Formatting and evidence-grounding audit report
└── README.md                      # Compilation and package documentation
```

---

## Required LaTeX Distribution & Packages

To compile `main.tex`, ensure you have a standard TeX distribution installed (e.g., **TeX Live**, **MiKTeX**, or **MacTeX**) along with the following standard packages:

* `IEEEtran.cls` (Official IEEE Conference Class)
* `cite` (IEEE citation management)
* `amsmath`, `amssymb`, `amsfonts` (Mathematical equations)
* `graphicx` (PDF figure embedding)
* `booktabs` (High-quality table borders)
* `array` (Table column formatting)
* `url` (Web link and repo formatting)
* `microtype` (Typography optimization)

---

## Compilation Instructions

Run the following command sequence in your shell to produce `main.pdf`:

```bash
cd research/ieee/

# Pass 1: Initial compilation
pdflatex main.tex

# Pass 2: Compile BibTeX citations
bibtex main

# Pass 3 & 4: Resolve cross-references and citation numbers
pdflatex main.tex
pdflatex main.tex
```

---

## Generated Figures & Assets

* **`figures/system_architecture.pdf`**: Clean vector PDF diagram representing the five core modules of Sentinel Desktop (Local LLM Integration, Browser Instrumentation, Security Analysis, Context Management, Replay Comparison) operating strictly over host local loopback (`127.0.0.1`). Generated via Matplotlib vector export.

---

## Bibliography & Metadata Notes

* **BibTeX File:** `references.bib` contains BibTeX entries for all 32 references cited in `paper_draft_v4.md`.
* **Citation Ordering:** Handled dynamically by `\bibliographystyle{IEEEtran}` during compilation. Citation numbers are assigned based on order of appearance in the paper.
* **Unresolved Metadata Items:** As documented in `research/bibliography_verification.md`, several conference proceedings entries ([22], [23], [25], [26], [30], [39], [46], [47], [50], [53], [54], [68], [78]) require explicit page ranges or volume numbers prior to camera-ready IEEE Xplore indexing. No metadata was fabricated.

---

## Assumptions & Layout Adaptations

1. **Author Block:** Configured with an anonymous IEEE author block (`\IEEEauthorblockN{Anonymous Authors}`) for double-blind or initial review.
2. **Table Width Adjustments:** Tables I, III, and V use `\resizebox{\columnwidth}{!}{...}` to ensure exact single-column alignment without overflowing IEEE column margins. Table VI spans two columns via `\begin{table*}[t]`.
3. **Evidence Grounding Guarantee:** The manuscript content, experimental metrics ($N=130$), distinction between canary binary vs. context accuracy, sequential DOM scanning limitation, and non-execution status of Experiments 4 and 6 are strictly preserved without alteration.
