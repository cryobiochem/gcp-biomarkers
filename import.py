# This file import the CDC NHANES dataset and converts XPT files to CSV to be
# further ingested in GCP.

import pandas as pd
import pyreadstat

df_demo, _ = pyreadstat.read_xport('raw/DEMO_J.xpt.txt') # DEMOGRAPHICS File: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.htm
df_chol, _ = pyreadstat.read_xport('raw/TCHOL_J.xpt.txt') # CHOLESTEROL File: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/TCHOL_J.htm

# SEQN is the unique participant identifier
df = pd.merge(df_demo, df_chol, on="SEQN")
df.to_csv("nhanes_2017_2018.csv", index=False)