from django.shortcuts import render
from django.core.files.storage import default_storage
from .ml_model import predict_image
from .api_request import nutApi
from .nutrients import nutrientsList

def homePage(request):
    return render(request, 'home.html')

def classify(request):
    if request.method == "POST" and request.FILES['image']:
        image_file = request.FILES['image']
        
        file_path = default_storage.save("uploads/" + image_file.name, image_file)
        
        predictions = predict_image(file_path)
        
        item = predictions[0][1]
        
        nutrients = nutApi(item)
        
        
        return render(request, 'home.html', { "predictions" : predictions, "image_ulr" : file_path, "nutrients" : nutrients })
    return render(request, 'home.html')