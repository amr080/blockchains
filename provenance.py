# Provenance Blockchain Network Endpoints

import requests
import pandas as pd
import json

url = "https://service-explorer.provenance.io/api/v3/utility_token/latest_pricing"
url2 = "https://service-explorer.provenance.io/api/v2/txs/recent?count=10&page=1"
url3 = 'https://service-explorer.provenance.io/api/v2/blocks/recent?count=10&page=1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))  # Pretty-print the JSON data
    df = pd.DataFrame(data)
else:
    print(f"Failed to fetch data: {response.status_code}")
