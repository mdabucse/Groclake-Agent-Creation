import pandas as pd
import numpy as np
import json
data = pd.read_csv(r'A:\Projects\Flight-Ticket\try\data\airport_data.csv')
json_data = {
    
}
for i in range(len(data)):
    json_data[data['municipality'][i]] = data['iata_code'][i]
print(json)
output_file = r'A:\Projects\Flight-Ticket\try\data\airport_data.json'
with open(output_file, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f"JSON data saved to {output_file}")

