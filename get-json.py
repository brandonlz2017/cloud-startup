import requests, json
import pandas as pd, numpy as np

def special_parser(item):
    if item.isnumeric():
        pass
    else:
        return item



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

location_working = [address for address in list(df['Location']) if address]
location_joined = ' '.join(location_working)
location_elements = location_joined.split()

print(location_elements[:10])

parsed_st_names = []
for street in location_elements:
    if street.isnumeric():
        pass
    else:
        parsed_st_names.append(street)

print(parsed_st_names[:10])



#df['Street Name'] = df['Location'].apply(lambda x: string_splitter(x))


#print(len(df['Street Name'].unique()))

#print(df['Street Name'].head())

#print(len(df))
#print(df['Location'].head())
#print(df.head(5))
#print(df.columns)

