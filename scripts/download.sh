#! /usr/bin/env bash

shopt -s nullglob
files=(data/*.parquet)
if [ ${#files[@]} -gt 0 ]; then
    echo "cleaning data directory"
    rm -rI data/*.parquet 
fi

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPTS_DIR="$(dirname "$SCRIPT_PATH")"

# Change to the data directory
cd "$SCRIPTS_DIR"/../data

curl -L --remote-name-all $(curl -L "https://github.com/pypi-data/data/raw/main/links/dataset.txt")