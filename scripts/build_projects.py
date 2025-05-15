#! /usr/bin/env -S uv run

# /// script
# dependencies = [
#   "duckdb",
# ]
# ///


import duckdb

QUERY = """
SELECT DISTINCT
-- We're bucketing our data by date and extension --
-- Handy to have both day and month buckets for analysis.
datetrunc('month', uploaded_on) AS month,
datetrunc('day', uploaded_on) AS day,
CASE
WHEN regexp_matches(path, '\\.rs$') THEN 'Rust'
WHEN regexp_matches(path, '\\.pyx$') THEN 'Cython'
ELSE 'C/C++'
END AS lang,
project_name,
FROM 'data/*.parquet'
WHERE (
-- Our regex for matching files we care about --
regexp_matches(path, '\\.(c|cc|cpp|cxx|h|hpp|rs|pyx)$')

-- Filter out test files and whole virtual environments --
-- embedded in Python distributions. --
AND NOT regexp_matches(path, '(^|/)test(|s|ing)')
AND NOT contains(path, '/site-packages/')
)
ORDER by day ASC, project_name ASC
"""

cursor = duckdb.connect()
job = f"COPY ({QUERY}) TO 'output/projects.csv' (HEADER, DELIMITER ',');"
cursor.execute(job)
