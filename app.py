from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

doc = Document()

# Adding a section
with doc.create(Section('A section')):
    doc.append('Some regular text and some ')
    doc.append(italic('italic text. '))

    with doc.create(Subsection('A subsection')):
        doc.append('Also some crazy characters: $$  $&#{}')

# Adding a raw LaTeX command
doc.append(NoEscape(r'\textbf{Bold Text}'))
doc.append(NoEscape(r'$$\sqrt{2}$$'))
# Generating the PDF
doc.generate_pdf('example', clean_tex=False)
