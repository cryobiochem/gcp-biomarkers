# CDC Longevity Biomarkers Pipeline: NHANES Dataset 2017-2018

This personal project envisioned the creation of a data engineering pipeline. The data aspect of the prototype is very simple, with basic ingestion, data transformation and orchestration; the focus was the seamless integration of all different building blocks.
The image below represents the high-level overview of the tech stack used for this project.


#### Flow:
1. import.py retrieves CDC NHANES demographics & total cholesterol 2017-2018 datasets, converts XPT to CSV files
2. CSV files are loaded into BigQuery, bucket: gs://bg-nhanes-longevity-data/nhanes_2017_2018.csv
