MD_TEMPLATE = template.md
YAML_DATA = data.yaml
GENCV = python gencv.py
MD = markdown

#resume.txt : ... with flag that doesnt execute special formatting?

all : resume.md resume.html

resume.md : $(MD_TEMPLATE) $(YAML_DATA)
	$(GENCV) -t $(MD_TEMPLATE) -d $(YAML_DATA) > resume.md

resume.html : resume.md
	$(MD) resume.md > resume.html

#resume.tex : ...
#resume.pdf : resume.tex ...

clean :
	rm -f resume.md resume.html
