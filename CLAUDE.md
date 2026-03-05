# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MkDocs Material documentation site for a book. Content is mathematical with LaTeX (MathJax) and includes Python example scripts.

## Build Commands

```bash
# Local development server with live reload
mkdocs serve

# Build static site (used in CI with --strict)
mkdocs build
mkdocs build --strict

# Install dependencies
pip install -r requirements.txt
```

## Deployment

GitHub Actions (`.github/workflows/deploy-mkdocs.yml`) auto-deploys to GitHub Pages on push to `main`. Build uses `--strict` mode, so all warnings are errors.

## Repository Structure

- `mkdocs.yml` — Site config and full navigation tree
- `docs/` — All content
  - `docs/chNN/` — Chapter directories
    - Markdown files organized by topic subsections
    - `codes/` — Python example scripts
  - `docs/index.md` — Home page
  - `docs/stylesheets/extra.css` — Custom CSS
  - `docs/javascripts/mathjax.js` — MathJax configuration

## Navigation Structure in mkdocs.yml

The nav is organized as: **Parts → Chapters → Sections → Pages**. Each chapter typically has numbered subsections and a final Python Examples section.

## Content Conventions

- **Math**: Use MathJax with `$...$` (inline) and `$$...$$` (display). Display math blocks must be surrounded by empty lines (blank line, then `$$...$$`, then blank line) for proper rendering
- **Python files**: Educational style with docstrings, section dividers (`# ===`), and `if __name__ == "__main__":` pattern
- **Code attribution prefixes**: `grzelak_`, `cantaro86_`, `qfn_`, `quantpie_` indicate adapted examples from external sources
- **Markdown extensions available**: admonition, details, attr_list, md_in_html, superfences, arithmatex
