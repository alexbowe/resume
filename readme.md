Stores all resume data (such as degrees, awards, etc) in a YAML file,
and embeds the data in a markdown (maybe LaTeX later) template.

Markdown is used as it is human readable. It also can be compiled to HTML
and LaTeX (for web and pdf versions). A separate LaTeX template may be used
later, as it will allow more control of the style class.

The rationale for doing this is so it is easier to add new awards and workplaces without messing up the rest of the resume. Also, better for storing in Git. Separates data from presentation. Allows targeting (do I want to include my address in the online version?), etc...
