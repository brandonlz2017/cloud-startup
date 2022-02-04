import requests, json
import pandas as pd

url = requests.get('https://opendata.arcgis.com/datasets/3eeb0a2cbae94b3e8549a8193717a9e1_0.geojson')
crime_codes = pd.read_csv('https://www.arcgis.com/sharing/rest/content/items/e6ca4eadecdc475a961f68bc314e2a86/data')
crime_name_dict = dict(zip(list(crime_codes['CODE']), list(crime_codes['NAME'])))
crime_type_dict = dict(zip(list(crime_codes['CODE']), list(crime_codes['VIO_PROP_CFS'])))

text = url.text

data = json.loads(text)
data = data['features']
columns = list(data[0]['properties'].keys())

temp_array = []
for row in range(len(data)):
    row_working = list(data[row]['properties'].values())
    temp_array.append(row_working)

df = pd.DataFrame(temp_array)
df = df.drop([16], axis=1)
df.columns = columns

df['CrimeCodeName'] = df['CrimeCode'].map(crime_name_dict)
df['CrimeCodeType'] = df['CrimeCode'].map(crime_type_dict)


#print(df.head())

philly_url = requests.get('https://opendata.arcgis.com/datasets/abe39f44c8af4bfb8bfb2ec7d233d920_0.geojson')
https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/INCIDENTS_PART1_PART2/FeatureServer/0/query?f=json&where=(DISPATCH_DATE_TIME%20%3E%3D%20TIMESTAMP%20'1-01-2015%208%3A48%3A53'%20AND%20DISPATCH_DATE_TIME%20%3C%3D%20TIMESTAMP%20'1-11-2022%201%3A15%3A00')&outFields=*
philly_text = philly_url.text
data_philly = json.loads(philly_text)
data_philly = data_philly['features']


print(data_philly[:5])


"Hello"
