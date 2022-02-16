import requests, json
import pandas as pd, numpy as np
import datetime
from collections import Counter

def special_parser(item):
    if item.isnumeric():
        pass
    else:
        return item



url = requests.get('https://opendata.arcgis.com/datasets/3eeb0a2cbae94b3e8549a8193717a9e1_0.geojson')
crime_codes = pd.read_csv('https://www.arcgis.com/sharing/rest/content/items/e6ca4eadecdc475a961f68bc314e2a86/data')
crime_name_dict = dict(zip(list(crime_codes['CODE']), list(crime_codes['NAME'])))
crime_type_dict = dict(zip(list(crime_codes['CODE']), list(crime_codes['VIO_PROP_CFS'])))
crime_name_long_dict = dict(zip(list(crime_codes['CODE']), list(crime_codes['VIOLENT_CR'])))

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
#df = df.dropna(subset=['CrimeDateTime'])
df.columns = columns


#print(columns)
df = df.sort_values(by='CrimeDateTime')
df = df.reset_index(drop=True)

df['CrimeDateTime'] = pd.to_datetime(df['CrimeDateTime'])
df = df.dropna(subset=['CrimeDateTime'])
df['Year'] = df['CrimeDateTime'].apply(lambda x: int(x.year))

#print(df.iloc[0,:])
#print(len(df))

#counted_list = Counter(list(df['Neighborhood']))
#print(counted_list.most_common(15))


#print(df['CrimeDateTime'].head())
#print(df['CrimeDateTime'][0])
#print(df['CrimeDateTime'][0].year)


df['CrimeCodeName'] = df['CrimeCode'].map(crime_name_dict)
df['CrimeCodeType'] = df['CrimeCode'].map(crime_type_dict)
df['CrimeCodeNameLong'] = df['CrimeCode'].map(crime_name_long_dict)

print(df['CrimeCodeType'].unique())

#print(df.iloc[0,:])

#print(df['Description'].unique())

#print(len(df))

#frequent_address = Counter(list(df['Location']))
#print(frequent_address.most_common(30))


df = df[df['CrimeCodeType']=='VIOLENT']

frequent_hood = Counter(list(df['Neighborhood']))
print(frequent_hood.most_common(15))

frequent_yoy = Counter(list(df['Year']))
print(frequent_yoy.most_common())




#df_working =  df[df['Location']=='1500 RUSSELL ST']
#print(df_working['Description'].unique())

#print(list(df['CrimeCodeNameLong'].unique()))

#print(df.head())


location_working = [address for address in list(df['Location']) if address]
#location_joined = ' '.join(location_working)
#location_joined = location_joined.upper()
#location_elements = location_joined.split()

#print(location_working)

#parsed_st_names = []
#for street in location_elements:
   # if street.isnumeric():
       #pass
    #elif len(street) < 4:
       #pass
    #else:
       #parsed_st_names.append(street)


#d_list = Counter(parsed_st_names)
#print(d_list.most_common(30))

#print(len(np.unique(parsed_st_names)))




#df['Street Name'] = df['Location'].apply(lambda x: string_splitter(x))


#print(len(df['Street Name'].unique()))

#print(df['Street Name'].head())

#print(len(df))
#print(df['Location'].head())
#print(df.head(5))
#print(df.columns)

