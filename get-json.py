import requests, json

url = requests.get('https://opendata.arcgis.com/datasets/3eeb0a2cbae94b3e8549a8193717a9e1_0.geojson')

text = url.text

data = json.loads(text)
data = data['features']

temp_array = []
for row in range(len(data)):
    row_working = data[row]['properties']
    temp_array.append(row_working)

print(temp_array[:5)    
    
    

#print(data['features'][0]['properties'])
