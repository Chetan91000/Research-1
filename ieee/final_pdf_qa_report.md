# IEEE PDF Compilation & Visual QA Report

**Target File:** `research/ieee/main.tex`  
**Date:** 2026-09-23  

---

## A. Compiler Environment
* **TeX Distribution:** MiKTeX (Version 25.12)
* **Compiler Engine:** `pdflatex`
* **BibTeX Engine:** `bibtex`

## B. Compilation Commands
```powershell
$miktex = "C:\Users\Aayush20\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
& "$miktex\pdflatex.exe" -interaction=nonstopmode main.tex
& "$miktex\bibtex.exe" main
& "$miktex\pdflatex.exe" -interaction=nonstopmode main.tex
& "$miktex\pdflatex.exe" -interaction=nonstopmode main.tex
```

## C. Compilation Result
* **Status:** **PASS** (Successfully generated `main.pdf`)

## D. Page Count
* **7 pages** (Confirmed via log output `Output written on main.pdf (7 pages, 268445 bytes).`)

## E. LaTeX Warnings/Errors
* **Errors:** None
* **Overfull \hbox:** 0 (Both the 77.1644pt and 8.79729pt overflows were successfully eliminated).
* **Underfull \hbox:** Minor formatting underfulls exist (expected behavior with strict IEEE column alignment), but no structural errors exist.

## F. BibTeX Warnings/Errors
* **Warnings/Errors:** None

## G. Citation/Reference Check
* **Status:** **PASS**
* All 32 references resolved flawlessly. Zero "undefined citation" or "undefined reference" warnings in the compilation log.

## H. Table Inspection
* **Status:** **PASS**
* All tables fit correctly within their respective columns.
* **Table VI (Group A Cross-Experiment Summary):** The two-column width overflow (77.1644pt) was eliminated utilizing a robust `\resizebox{\textwidth}{!}{...}` wrap. The table retains all numerical results, the Exp 2 `70.0%` value, and the ATTRIBUTE limitation note safely within the IEEE margins.

## I. Equation Inspection
* **Status:** **PASS**
* Equations (1) through (4) format natively within the single-column boundaries without overflow.

## J. Figure Inspection
* **Status:** **PASS**
* `figures/system_architecture.pdf` is properly imported and sized. No "missing figure" errors reported in the compiler log.

## K. Page-by-Page Visual QA
* **IEEE Columns:** Two-column constraints strictly observed.
* **Whitespace/Page Breaks:** No awkward orphaned headings or massive whitespace gaps.
* **Text/Code Overflows:** The Git commit hash at the Experimental Environment section was cleanly broken using `\allowbreak` to ensure it does not bleed into the adjacent column.
* **Captions:** Captions properly aligned with tables and figures per IEEEtran defaults.
* **Raw Markdown:** None. Completely converted to LaTeX.

## L. Problems Found
* **Initial Overflow Errors:** The Git commit hash overflowed its column by 8.79729pt, and Table VI overflowed by 77.1644pt.

## M. Corrections Made
1. **Hash Overflow:** Replaced the continuous 40-character `\texttt` block with `\texttt{a3bb957454684b64}\allowbreak\texttt{7884ac15ca8ed9d413139a3d}` to permit clean column wrapping.
2. **Table VI Overflow:** Wrapped the `tabular` environment inside `\resizebox{\textwidth}{!}{...}` to scale the table gracefully into the available two-column width.
* *Note: No research claims, numerical results, citations, or methodology were altered during formatting corrections.*

## N. Final Submission Status

| Component | Status Classification |
|---|---|
| Compiler Setup | **PASS** |
| LaTeX Compilation | **PASS** |
| Cross-Referencing | **PASS** |
| Box Formatting | **PASS** |
| Visual QA | **PASS** |

**IEEE PDF passed final technical and visual QA.**
