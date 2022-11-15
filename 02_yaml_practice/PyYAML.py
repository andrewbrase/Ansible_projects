# PyYAML is a YAML parser for Python
# >pip install pyyaml

import yaml
# reading a YAML file

# open the file as f
print("\n\n")
with open('PyYAML.yml') as f:
    # use the load_all function - it becomes a python dictionary
    yaml_contents = yaml.load_all(f, Loader=yaml.FullLoader)
    # for every item in that dictionary -
    for yaml_content in yaml_contents:
        # seperate the keys and values
        for key, value in yaml_content.items():
            # print the key and value
            print(f"{key}: {value}")
    print("\n\n")

# name: Martin
# job: Developer
# employed: True
# foods: ['Apple', 'Orange', 'Strawberry', 'Mango']
# languages: {'Python': 'good', 'Javascript': 'good', 'Rust': 'good'}
# education: 4 GCSEs
# 3 A-Levels
# BSc in the IoT

# The REVERSE of this is converting this python dictionary into a YAML format
# we achieve that using the dump() function

# this method will serialize a Python object into
# a YAML stream, where the Python obect could
# be a dictionary

cardict = {
    'a_list': ["this", "is", "a", "list"], 
    "car": {
        "brand": "Ford",
        "model": "mustang",
        "year": 1964
    },
    "factories": {
        "building_01": "Illinois",
        "building_02": "Michigan",
        "building_03": "Wisconsin"
    }
}


print(yaml.dump(cardict))
print(type(yaml.dump(cardict)))

# a_list:
# - this
# - is
# - a
# - list
# car:
#   brand: Ford
#   model: mustang
#   year: 1964
# factories:
#   building_01: Illinois
#   building_02: Michigan
#   building_03: Wisconsin

# <class 'str'>