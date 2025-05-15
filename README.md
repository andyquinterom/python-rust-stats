# Stats of Rust usage in Python

This is the source to some analysis which I run every so often when producing content for various talks I've given.

## Attribution

Dataset is from https://py-code.org/datasets#metadata

Original credit for the analysis from Seth Michael Larson, https://fosstodon.org/@sethmlarson/111382964885780823

## Contents

`scripts/` directory contains the source files for downloading and running the analysis.

`output/` directory contains the results of analysis as CSV files:
  - `projects.csv` contains a list of projects uploaded each day to PyPI which contained native code
  - `uploads.csv` is an aggregation which counts the number of projects by language by month
  - `new_projects.csv` is a filtered view which counts each project only once ever

## Usage

Run the scripts in the following order to complete the full pipeline:

```bash
scripts/download.sh  # does what you expect
scripts/build_projects.py  # initial costly analysis to aggregate the data to a per-project level
scripts/aggregate.py  # builds the final content
```