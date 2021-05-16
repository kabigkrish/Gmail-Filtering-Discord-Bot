from fpdf import FPDF
# save FPDF() class into a 
# variable pdf
def topdf(text):    
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 10)
    
    # create a cell
    pdf.multi_cell(0, 5, txt = str(text),align='L',border=1)
    
    # save the pdf with name .pdf
    pdf.output("gmail.pdf") 