import requests, json

url = requests.get('https://opendata.arcgis.com/datasets/3eeb0a2cbae94b3e8549a8193717a9e1_0.geojson')

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

print(df.head())    
    
    

