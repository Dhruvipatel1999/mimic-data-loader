import pandas as pd
import gzip

# Path to the ADMISSIONS.csv.gz file
file_path = "D:/mimic-iii-clinical-database-1.4/mimic-iii-clinical-database-1.4/ADMISSIONS.csv.gz"

# Load the gzip file using pandas
with gzip.open(file_path, 'rt') as f:
    df = pd.read_csv(f)

# Print first 5 rows
print(df.head())
