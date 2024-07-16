from pylatex import Document, Section, Command,Subsection,Tabularx
from pylatex.utils import NoEscape

doc = Document(documentclass='article',document_options='12pt'  )



doc.preamble.append(Command('usepackage', arguments=['float']))
doc.preamble.append(NoEscape(r"\title{My \LaTeX\ Document}"))
doc.preamble.append(NoEscape (r"\author {xyz person}") )
doc.preamble.append(NoEscape(r"\date{\today}"))

doc.append( NoEscape(r"\maketitle") )
# Add the content
doc.append(NoEscape(r"\tableofcontents"))
sections=["Linear Function","Quadratic Functions","Cubic Functions","High Order Functiona"]
for sec in sections:
    with  doc.create(Section(sec)):
        doc.append(Subsection("Slope Intercept Form"))
        doc.append(Subsection("Standard Form"))
        doc.append(Subsection("Mathematical Notations"))
        doc.append(Subsection("Practical Uses"))



with doc.create(Section("Maths Mode")):

    doc.append(Subsection("Equations/Subscripts/Superscripts"))
    doc.append(NoEscape(r"$$x^2+2+4y^{33}$$"))
    doc.append(NoEscape(r"$$x_1 +x_2+x_{33}$$"))

    doc.append(Subsection("Fraction and Mathermatical Functions"))
    doc.append(NoEscape(r"$$\frac{1}{x+1}$$\\[6pt]"))
    doc.append(NoEscape(r"$$ \sqrt{ \frac{x}{ax+b} }\\[6pt] $$"))
    doc.append(NoEscape(r"$$\frac{\sin \theta}{\cos \theta} \\[6pt]$$"))

    doc.append(Subsection("Brackets"))
    doc.append(NoEscape(r"$$  \left\{  \frac{1} {  \left( 1 + \frac{1}{x}    \right)   }   \right\}$$ \\[6pt]"))
    doc.append(NoEscape(r"$$ a[0] = 3  $$"))


with doc.create(Section("Tables")):
    doc.append(Command("vspace","4pt"))
    doc.append(Subsection("Tables with number"))

    doc.append(NoEscape(r"\begin{tabular}{|c|c|c|c|c|c|}"))
    
    doc.append(NoEscape(r"\hline"))
    
    doc.append(NoEscape(r"x & 1 & 2 & 3 & 4 & 5 \\"))
    doc.append(NoEscape(r"\hline"))
    doc.append(NoEscape(r"f(x) & 1 & 4 & 9 & 16 & 25 \\"))
    doc.append(NoEscape(r"\hline"))
    
    doc.append(NoEscape(r"\end{tabular}"))
    
    doc.append(Subsection("Table with sentences"))
    


#table 2

    with doc.create(Tabularx("|l|p{2in}|")) as table:
        table.add_hline()
        table.add_row(["f(x)","f(x)'"])
        table.add_hline()
        table.add_row(["1","relation between function and its derivative is cubic\\"])
        table.add_hline()



# Generate the .tex file
doc.generate_pdf("main",clean_tex=False)
