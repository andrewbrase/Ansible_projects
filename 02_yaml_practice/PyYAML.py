# PyYAML is a YAML parser for Python
# >pip install pyyaml

import yaml
# reading a YAML file
with open('PyYAML.yml') as f:
    yaml_contents = yaml.load_all(f, Loader=yaml.FullLoader)
    for yaml_content in yaml_contents:  
        for key, value in yaml_content.items():
            print(f"{key}: {value}")

