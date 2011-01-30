data_file = 'data.yaml'

import yaml

# Load YAML into data dictionary
with open(data_file) as f:
	data = yaml.load(f)

print data['summary']
