data_file = 'data.yaml'
template_file = 'template.md'

import yaml
from Cheetah.Template import Template

# Load YAML into data dictionary
with open(data_file) as f:
    data = yaml.load(f)

# Load template
with open(template_file) as f:
    template = f.read()

t = Template(template, searchList=[data])

print t
