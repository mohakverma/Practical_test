import pandas as pd
import json

#cleaning 
def correct_json_string(json_str):
    corrected = json_str.replace("'", '"')
    corrected = corrected.replace("None", "null")
    corrected = corrected.replace("True", "true")
    corrected = corrected.replace("False", "false")
    return corrected

with open('ubo.json', 'r') as file:
    json_str = file.read()
    corrected_json_str = correct_json_string(json_str)
    data = json.loads(corrected_json_str)

# function to flatten
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# extracting the list of companies
companies = data['results']['companies']

df = pd.DataFrame([flatten_json(company) for company in companies])

print(df)
df.to_csv('ubo.csv', index=False)
