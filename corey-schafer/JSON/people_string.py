import json

# Encoders and Decoders for JSON in Python
# https://docs.python.org/3/library/json.html#encoders-and-decoders

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bosuemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''
# load JSON into a python object
data = json.loads(people_string)

for person in data['people']:
  print(type(person))
  print(person['name'])

# print(data['people'])
# print(type(data))
# print(type(data['people']))

# dump a python object into a JSON string

for person in data['people']:
  del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)