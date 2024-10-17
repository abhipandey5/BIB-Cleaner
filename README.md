# Bib Cleaner Tool

Bib Cleaner Tool is a simple Python utility to detect and remove redundant (duplicate) entries in a `.bib` file used in LaTeX. It scans your `.bib` file for duplicate entries (based on titles) and creates a new `.bib` file containing only unique references.

## Features

- Detects duplicate references in `.bib` files based on titles.
- Cleans and saves a new, non-redundant `.bib` file.
- Easily customizable to match duplicates based on other fields (e.g., authors, DOI, etc.).

## Requirements

- Python 3.x
- `bibtexparser` library (for reading and writing `.bib` files)

## Installation

First, install the required Python package:

```bash
pip install bibtexparser
