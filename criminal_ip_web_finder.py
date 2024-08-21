import requests

print('\033[35m'+"Welcom to web server ip finder (using CIP API)"+ '\033[0m')
searchkey = raw_input('\033[92m'+"Enter Product Name (ex:Apache): "+ '\033[0m')
offset = raw_input('\033[92m'+"Enter Offset (multiples of 10): "+ '\033[0m')
url = "https://api.criminalip.io/v1/banner/search?query=product%3A{}&offset={}".format(searchkey, offset)
payload={}
headers = {"x-api-key" : raw_input('\033[92m'+"Write your CIP API key: "+ '\033[0m')}

response = requests.request("GET", url, headers=headers, data=payload)
output = response.json()
if response.status_code == 200:
    try:
        def filter_results(output):
            filtered_results = []
            results = output['data']['result']
            for result in results:
                    filtered_results.append({
                        'ip_address': result.get('ip_address'),
                        'name': result.get('org_name')
                    })
            return filtered_results
        filtered_results = filter_results(output)
        for item in filtered_results:
                print("IP Address: {}, Name: {}".format('\033[94m'+item['ip_address']+ '\033[0m', '\033[94m'+item['name']+ '\033[0m'))
    except ValueError as e:
         print('\033[91m'+"Error parsing JSON: {}".format(e)+ '\033[0m')
    except KeyError as e:
         print('\033[91m'+"Key Error: {}".format(e)+ '\033[0m')
else:
     print("Failed to retrieve Data: {}".format(response.status_code)+ '\033[0m')