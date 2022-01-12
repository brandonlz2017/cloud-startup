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


print(df.head())

philly_url = pd.read_csv('https://phl.carto.com/api/v2/sql?filename=incidents_part1_part2&amp;format=csv&amp;q=SELECT%20*%20,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20incidents_part1_part2%20WHERE%20dispatch_date_time%20%3E=%20%272021-01-01%27%20AND%20dispatch_date_time%20%3C%20%272022-01-01%27')
print(philly_url.head())


