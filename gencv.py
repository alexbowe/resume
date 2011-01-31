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
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-d", "--data", dest="data_file",
		      help="YAML file containing data",
		      metavar="FILE")
    parser.add_option("-t", "--template", dest="template_file",
		      help="Template for output",
		      metavar="FILE")
    mandatory = ['data_file', 'template_file']

    options, args = parser.parse_args()
    
    for m in mandatory:
        if not options.__dict__[m]:
	    parser.print_help()
            parser.error("Mandatory option is missing")
    
    data_file = options.data_file
    template_file = options.template_file
    print yaml2cheetah(data_file, template_file)
