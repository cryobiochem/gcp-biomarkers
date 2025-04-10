# CDC Longevity Biomarkers Pipeline
## An end-to-end mock project for Data Engineering

#### Flow:
1. import.py retrieves CDC NHANES demographics & total cholesterol 2017-2018 datasets, converts XPT to CSV files
2. CSV files are loaded into BigQuery, bucket: gs://bg-nhanes-longevity-data/nhanes_2017_2018.csv
