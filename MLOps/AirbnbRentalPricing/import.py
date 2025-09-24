import pandas as pd
from sqlalchemy import create_engine

csv_file = 'AB_NYC_2019.csv'
df = pd.read_csv(csv_file)

print(f"Read {len(df)} rows and {len(df.columns)} columns from {csv_file}")

db_user = 'admin'
db_password = 'admin123'
db_host = 'localhost'
db_port = '5432'
db_name = 'testdb'
table_name = 'airbnb_nyc'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Successfully inserted into '{table_name}' table in '{db_name}' database.")