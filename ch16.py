import json

json_string = '{"name":"Luc", "year":22, "is_good": true, "motivation": null}'
py_json = json.loads(json_string)
print(py_json)