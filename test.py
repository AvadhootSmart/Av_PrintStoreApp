import fitz  # PyMuPDF library for PDF
from docx import Document  # python-docx library for DOCX

def count_pages(file_path):
    """
    Count the number of pages in a PDF or DOCX file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        int: Number of pages in the file.
    """
    if file_path.endswith('.pdf'):
        return count_pdf_pages(file_path)
    elif file_path.endswith('.docx'):
        return count_docx_pages(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats: PDF, DOCX")

def count_pdf_pages(file_path):
    """
    Count the number of pages in a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        int: Number of pages in the PDF.
    """
    pdf_document = fitz.open(file_path)
    num_pages = pdf_document.page_count
    pdf_document.close()
    return num_pages

def count_docx_pages(file_path):
    """
    Count the number of pages in a DOCX file.

    Args:
        file_path (str): Path to the DOCX file.

    Returns:
        int: Number of pages in the DOCX.
    """
    doc = Document(file_path)
    num_pages = len(doc.element.xpath('//w:sectPr'))
    return num_pages

# Example usage:
pdf_file_path = './print_files/Avadhoot/Dsa_Assignment_4.pdf'
docx_file_path = './print_files/Avadhoot/Assignment_5new.docx'

num_pdf_pages = count_pages(pdf_file_path)
num_docx_pages = count_pages(docx_file_path)

print(f"Number of pages in PDF: {num_pdf_pages}")
print(f"Number of pages in DOCX: {num_docx_pages}")


# def calculate_cost(PageCount, color, orientation):
    
#     if(color == "B&W"):
        
#         if(orientation == "Single"):
#             Price = 5
#             cost = PageCount*Price
#             return cost
#         else:
#             Price = 2
#             cost = PageCount*Price
#             return cost
    
#     elif(color == "Color"):
        
#         if(orientation == "Single"):
#             Price = 10
#             cost = PageCount*Price
#             return cost
#         else:
#             Price = 5
#             cost = PageCount*Price
#             return cost
        
        
# cost = calculate_cost(10,"Color","Single") 
# print(cost)
            
        
   