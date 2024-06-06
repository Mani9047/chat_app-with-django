from django.shortcuts import render,redirect
from django.http import HttpResponse
from rembg import remove
from PIL import Image
import base64
from io import BytesIO

def show(request):
    show = None
    inputs = None
    if request.method == 'POST' and 'kiko' in request.FILES:
        data = request.FILES['kiko']
        input_image = Image.open(data)
        input_buffer = BytesIO()
        input_image.save(input_buffer, format='PNG')
        input_buffer.seek(0)
        
        output_image = remove(input_image)
        output_buffer = BytesIO()
        output_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)
        
        inputs = base64.b64encode(input_buffer.getvalue()).decode('utf-8')
        show = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
        
        global down
        down = output_buffer.getvalue()
        
        return render(request, 'show.html', {'tem': show, 'dat': inputs})
    return render(request, 'home.html', {'tem': show, 'dat': inputs})

def download(request):
    global down
    response = HttpResponse(down, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="remove.png"'
    return response
