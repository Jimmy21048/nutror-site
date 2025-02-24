from django.shortcuts import render
from django.core.files.storage import default_storage
from .ml_model import predict_image
from .api_request import nutApi
from django.http import JsonResponse

def homePage(request):
    if request.POST.get('text'):
        text = request.POST.get('text')
        
        nutrients = nutApi(text)
        
        return JsonResponse({'nutrients' : nutrients, 'item' : text, 'prob' : 0.99})
    elif request.method == "POST" and request.FILES['image']:
        
        image_file = request.FILES['image']
        
        
        file_path = default_storage.save("uploads/" + image_file.name, image_file)
        # file_path = "uploads/" + image_file.name
        
        predictions = predict_image(file_path)
        
        default_storage.delete(file_path)
        
        item = predictions[0][1]
        prob = float(predictions[0][2]) #prob for probability
        
        nutrients = nutApi(item)
        
        return JsonResponse({'nutrients' : nutrients, 'item' : item, 'prob' : prob})
         
    
    else :    
        return render(request, 'home.html')