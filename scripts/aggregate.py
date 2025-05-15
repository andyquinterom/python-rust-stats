#! /usr/bin/env -S uv run

# /// script
# dependencies = [
#   "duckdb",
# ]
# ///


import duckdb

QUERY = """
SELECT
month,
lang,
COUNT(DISTINCT project_name) AS num_projects
FROM 'output/projects.csv'
GROUP BY month, lang
ORDER BY month DESC
"""

cursor = duckdb.connect()
job = f"COPY ({QUERY}) TO 'output/uploads.csv' (HEADER, DELIMITER ',');"
cursor.execute(job)

QUERY = """
WITH release_dates as (
  SELECT
  project_name,
  lang,
  min(month) as first_date,
  FROM 'output/projects.csv'
  GROUP BY project_name, lang
)
SELECT
first_date,
SUM(CASE when lang = 'Rust' then 1 else 0 end) as 'Rust',
SUM(CASE when lang = 'Cython' then 1 else 0 end) as 'Cython',
SUM(CASE when lang = 'C/C++' then 1 else 0 end) as 'C/C++',
COUNT(*) as total
FROM release_dates
GROUP BY first_date
ORDER BY first_date DESC
"""

job = f"COPY ({QUERY}) TO 'output/new_projects.csv' (HEADER, DELIMITER ',');"
cursor.execute(job)
