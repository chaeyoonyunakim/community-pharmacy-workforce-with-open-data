"""
purpose:
automate the extraction of the total number of pharmacies in England, using the NHS Business Services Authority (NHSBSA) Open Data Portal API.

data:
Consolidated Pharmaceutical List, which includes NHS pharmacies, appliance contractors, and Local Pharmaceutical Services contractors.
https://opendata.nhsbsa.net/dataset/consolidated-pharmaceutical-list

api documentation:
https://opendata.nhsbsa.net/pages/api

"""

# ----- API ROOT -----
# root url to the api
api_root_path = 'https://opendata.nhsbsa.net/api/3/action/datastore_search'

# ----- DATASET -----
# dataset comes from: https://opendata.nhsbsa.net/dataset/consolidated-pharmaceutical-list
# resource_id for the specified quarter
# dataset can be found in the Open Data Portal:
# https://opendata.nhsbsa.net/dataset/consolidated-pharmaceutical-list/resource/d36c355a-631d-4ddb-bc34-5a0315565e12
resource_id = 'CONSOL_PHARMACY_LIST_202223Q4'

# ----- QUERY PARAMETERS -----
# set 'limit' to 0 to get only the total count and no records
params = {
    'resource_id': resource_id,
    'limit': 0,
}

# ----- API REQUEST -----
api_request = f'{api_root_path}?resource_id={params["resource_id"]}&limit={params["limit"]}'

with urllib.request.urlopen(api_request) as response:
    # Check for a successful response (status code 200)
    if response.status == 200:
        data = response.read().decode('utf-8')
        result = json.loads(data)

# Extract the fiscal year (FY) from the resource_id string
recource_year = resource_id.split('_')[-1][:6]
financial_year = f"{recource_year[:4]}/{recource_year[4:]}"

# Store the query output
total_pharmacies = result['result']['total']
print(f"Total number of pharmacies in {financial_year}: {total_pharmacies}")
