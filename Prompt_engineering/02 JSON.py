import json

d = {
    "name": "Ariana Grande",
    "age": 11,
    "gender": "Female"
}

print(json.dumps(d))

l = [
    {
        "name": "Ariana Grande",
        "age": 11,
        "gender": "Female"
    },
    {
        "name": "Olivia Rodrigo",
        "age": 12,
        "gender": "Female"
    },
    {
        "name": "Sabrina Carpenter",
        "age": 16,
        "gender": "Female"
    }
]

print(json.dumps(l))

json_str = '{"name": "Ariana Grande", "age": 11, "gender": "Female"}'
json_array_str = '[{"name": "Ariana Grande", "age": 11, "gender": "Female"}, {"name": "Olivia Rodrigo", "age": 12, "gender": "Female"}, {"name": "Sabrina Carpenter", "age": 16, "gender": "Female"}]'


res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))

