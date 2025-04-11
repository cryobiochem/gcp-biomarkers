# CDC Longevity Biomarkers Pipeline: NHANES Dataset 2017-2018

This personal project envisioned the creation of a data engineering pipeline. The data aspect of the prototype is very simple, with basic ingestion, data transformation and orchestration; the focus was the seamless integration of all different building blocks.
The image below represents the high-level overview of the tech stack used for this project.

---
![image](https://github.com/user-attachments/assets/2a18d219-0db3-491e-9c2d-1632b1f805bd)

---

## Flow:
### 1. import.py retrieves CDC NHANES demographics & total cholesterol 2017-2018 datasets, converts XPT to CSV files.
```python
# This file import the CDC NHANES dataset and converts XPT files to CSV to be
# further ingested in GCP.

import pandas as pd
import pyreadstat

df_demo, _ = pyreadstat.read_xport('raw/DEMO_J.xpt.txt') # DEMOGRAPHICS File: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.htm
df_chol, _ = pyreadstat.read_xport('raw/TCHOL_J.xpt.txt') # CHOLESTEROL File: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/TCHOL_J.htm

# SEQN is the unique participant identifier
df = pd.merge(df_demo, df_chol, on="SEQN")
df.to_csv("nhanes_2017_2018.csv", index=False)
```

### 2. CSV files are uploaded to a Cloud Storage bucket.
```bash
gs://bg-nhanes-longevity-data/nhanes_2017_2018.csv
```

### 3. The CS bucket is loaded into BigQuery.
   
### 4. In a WSL2 Ubuntu containerized development workspace, running Docker and VSCode on Ubuntu 22.04, three transformation DBT models were created.
- The `stg_health_data.sql` model retrieves relevant data from the raw source.
- The `int_biomarkers_enriched.sql` view asserts a categorical descriptor to cholesterol levels based on quantitative data.
- The `fct_longevity_summary.sql` view is a factual aggregate of average age and cholesterol levels for analytics.
![image](https://github.com/user-attachments/assets/aece4edb-d3b6-4030-a08b-9d4dea8bb9ff)

### 5. To circumvent Cloud Composer costs, Apache Airflow was used locally to orchestrate the ETL pipeline described above.
![image](https://github.com/user-attachments/assets/b739cd76-ad9b-403a-8a45-458c63038f62)

### 6. Quick analytics was done in Google Sheets, to circumvent the paid costs of Looker Studio. 
It directly consumes from BigQuery data and updates on the go.
![image](https://github.com/user-attachments/assets/692f211b-daf7-4701-8453-63c46a3bbad1)

<sub>Bruno M. Guerreiro 2025 | cryobiochem </sub>
