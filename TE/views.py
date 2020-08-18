from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from PIL import Image
import pytesseract
from .forms import reqData
def index(request):
	return render(request,'TE/index.html')
def wintext(request):
    return render(request, 'TE/WinText.html')
def about(request):
    return render(request, 'TE/About.html')
def get_text(request):
    # check to see if this is a post request
    if request.method == "POST":
        try:
            lang=request.POST['lang']    
        except:
            return render(request,'TE/WinText.html')
            # check to see if an image was uploaded
        if request.FILES.get("image", None) is not None:
            image = request.FILES["image"]
        try:
            img = Image.open(image)
            pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
            result = pytesseract.image_to_string(img, lang=lang)
            result= result.replace('\n\n','\n')
            context={
            'result':result,
            }
        except:
            return render(request, 'TE/WinText.html')
    return render(request, 'TE/WinText.html', context)
