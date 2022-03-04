import json
with open('/Applications/docs/lessons/PP2/4/4week/json/sample-data.json', 'r') as f:
  data = json.load(f)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

print(data['imdata'][0]['l1PhysIf']['attributes']['dn']+"                              inherit   9150 ")
print(data['imdata'][1]['l1PhysIf']['attributes']['dn']+"                              inherit   9150 ")
print(data['imdata'][2]['l1PhysIf']['attributes']['dn']+"                              inherit   9150 ")
