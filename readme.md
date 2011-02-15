Stores all resume data (such as degrees, awards, etc) in a YAML file,
and embeds the data in a markdown (maybe LaTeX later) template.

Markdown is used as it is human readable. It also can be compiled to HTML
and LaTeX (for web and pdf versions). A separate LaTeX template may be used
later, as it will allow more control of the style class.

The rationale for doing this is so it is easier to add new awards and workplaces without messing up the rest of the resume. Also, better for storing in Git. Separates data from presentation. Allows targeting (do I want to include my address in the online version?), etc...

TODO
----
 - HAML template (greater control of html layout)
 - LaTeX template for PDF generation
 - highlighting syntax: `!text to be highlighted! text not highlighted`. This will involve
   a commandline switch to turn rich highlighting off for plaintext mode (-p --plaintext).
   The rationale is that * at the start of data in YAML means something else, and it will have
   errors during parsing.
 - private syntax: `private: this value is private`. Private information will be ignored in the
   template. -v --private
 - possibly a way of applying transformations (with s/bla/bla/ syntax in a transformation config,
   or another yaml file, `{pattern: <regex>, transform: bla bla $1}`
