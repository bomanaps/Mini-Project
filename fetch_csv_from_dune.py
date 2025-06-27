import os
import dotenv
from dune_client.client import DuneClient
from dune_client.query import QueryBase

dotenv.load_dotenv()
dune = DuneClient.from_env()

QUERY_ID = 5354328 

query = QueryBase(
    name="Any Name",  
    query_id=QUERY_ID,
    params=[],         
)

print(f"Fetching results for Dune Query ID {QUERY_ID}...")
csv_result = dune.run_query_csv(query)

CSV_PATH = "data/stablecoin_cusd.csv"
os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
with open(CSV_PATH, "w", encoding="utf-8") as f:
    f.write(str(csv_result))

print(f"✅ CSV saved to {CSV_PATH}")
