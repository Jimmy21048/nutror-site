from django.shortcuts import render
from django.core.files.storage import default_storage
from .ml_model import predict_image
from .api_request import nutApi
from django.http import JsonResponse

def homePage(request):
    if request.method == "POST" and request.FILES['image']:
        image_file = request.FILES['image']
        
        file_path = default_storage.save("uploads/" + image_file.name, image_file)
        
        predictions = predict_image(file_path)
        
        item = predictions[0][1]
        prob = float(predictions[0][2]) #prob for probability
        
        nutrients = nutApi(item)
        
        return JsonResponse({'nutrients' : nutrients, 'item' : item, 'prob' : prob})
    
    else :    
        return render(request, 'home.html')