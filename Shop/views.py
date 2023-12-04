from django.shortcuts import render, redirect
from Shop.models import Order, ColorPrice, BlackAndWhitePrice, Sales
from .forms import OrderForm
import fitz  # PyMuPDF library for PDF
from docx import Document  # python-docx library for DOCX

# Create your views here.
def Home(request):
    black_and_white_price = BlackAndWhitePrice.objects.first()
    color_price = ColorPrice.objects.first()

    if black_and_white_price and color_price:
        BLACK_WHITE_SP = black_and_white_price.Single_Page_Cost
        BLACK_WHITE_DP = black_and_white_price.Double_Page_Cost
        COLOR_SP = color_price.Single_Page_Cost
        COLOR_DP = color_price.Double_Page_Cost

        Prices = {
            "BlackWhiteSP": BLACK_WHITE_SP,
            "BlackWhiteDP": BLACK_WHITE_DP,
            "ColorSP": COLOR_SP,
            "ColorDP": COLOR_DP
        }
        return render(request, "index.html", {"Prices": Prices})
    else:
        # Handle the case when the objects are not found in the database
        return render(request, "error.html", {"message": "Prices not found in the database"})


def checkout(request):     
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():   
            filename = request.FILES['UploadFile'].name            
            name = form.cleaned_data['name'],
            orientation = form.cleaned_data['orientation'],
            color_type = form.cleaned_data['ColorType'],
            upload_file = form.cleaned_data['UploadFile']
            form.save()
            if filename.endswith(".pdf") or filename.endswith(".docx"):
                FilePath = get_file_path(name,filename)
                PagesCount = count_pages(FilePath)
            
                orien = orientation[0]
                color = color_type[0]
                Amount = calculate_cost(PagesCount,color,orien)
            
                CostToPay = Sales.objects.create(Order_amount = Amount)
                CostToPay.save()
            else:
                return render(request, "checkout.html",
                          {"name": name,
                           "orientation": orientation,
                           "color_type": color_type,
                           "upload_file": upload_file,
                           "filename":filename,
                           })
                   
            return render(request, "checkout.html",
                          {"name": name,
                           "orientation": orientation,
                           "color_type": color_type,
                           "upload_file": upload_file,
                           "filename":filename,
                           'PageCount':PagesCount,
                           'Amount':Amount})

        else:
            error = "Submission failed! Resubmit your details correctly"
            return redirect("/",{"error":error})
    else:
        form = OrderForm() 
    return render(request, 'failed.html')



#Functions

def count_pages(file_path):
   
    if file_path.endswith('.pdf'):
        return count_pdf_pages(file_path)
    elif file_path.endswith('.docx'):
        return count_docx_pages(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats: PDF, DOCX")

def count_pdf_pages(file_path):
    
    pdf_document = fitz.open(file_path)
    num_pages = int(pdf_document.page_count)
    pdf_document.close()
    return num_pages

def count_docx_pages(file_path):
    doc = Document(file_path)
    num_pages = len(doc.element.xpath('//w:sectPr'))
    return num_pages

def get_file_path(name,filename):
    if " " in filename:
        file_name = filename.replace(" ", "_")
        return f'print_files/{name[0]}/{file_name}'
    else:
        return f'print_files/{name[0]}/{filename}'

def calculate_cost(PageCount, color, orientation):
    black_and_white_price = BlackAndWhitePrice.objects.first()
    color_price = ColorPrice.objects.first()

    if black_and_white_price and color_price:
        BLACK_WHITE_SP = black_and_white_price.Single_Page_Cost
        BLACK_WHITE_DP = black_and_white_price.Double_Page_Cost
        COLOR_SP = color_price.Single_Page_Cost
        COLOR_DP = color_price.Double_Page_Cost
    
    if(color == "B&W"):
        
        if(orientation == "Single"):
            Price =BLACK_WHITE_SP
            cost = PageCount*Price
            return cost
        else:
            Price =BLACK_WHITE_DP 
            cost = PageCount*Price
            return cost
    
    elif(color == "Color"):
        
        if(orientation == "Single"):
            Price = COLOR_SP
            cost = PageCount*Price
            return cost
        else:
            Price = COLOR_DP
            cost = PageCount*Price
            return cost
        

        
   