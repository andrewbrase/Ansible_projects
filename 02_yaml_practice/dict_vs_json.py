import json
employee_0= {
    "name":"Martin",
    "Job":"Developer",
    "Age":31,
    "employed":True,
}

print(type(employee_0))
# class dict

# Serializing
json_object = json.dumps(employee_0)
print(json_object)
print(type(json_object))
# class str

# --->
# <class 'dict'>
# {"name": "Martin", "Job": "Developer", "Age": 31, "employed": true}

# <class 'str'>