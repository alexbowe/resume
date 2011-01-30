default_data_file = 'data.yaml'
default_template_file = 'template.md'

import yaml
from Cheetah.Template import Template

def yaml2cheetah(data_file, template_file):
    # Load YAML into data dictionary
    with open(data_file) as f:
        data = yaml.load(f)
	
    # Load template
    with open(template_file) as f:
        template = f.read()
	
    return Template(template, searchList=[data])

if __name__ == '__main__':
	print yaml2cheetah(default_data_file, default_template_file)
