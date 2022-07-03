import json

# JSON string
customer = '{"id":"09", ' \
           '"name": "Nitin", ' \
           '"department":"Finance"}'

# Convert string to Python dict
customer_dict = json.loads(customer)
print(customer_dict)
print(customer_dict['name'])

# Getting data from Json File
f = open('demo_json.json' )

record = json.load(f)

# Iterating through the json
# list
for i in record['employee_details']:
    print(i)