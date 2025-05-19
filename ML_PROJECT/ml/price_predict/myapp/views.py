from django.shortcuts import render,redirect
import json
import pickle
from django.http import HttpResponse
import numpy as np

with open (r"C:\Users\Admin\Desktop\ml\bengalore_homeprice_model","rb") as f:
    model=pickle.load(f)

import json

with open(r"C:\Users\Admin\Desktop\ml\columns.json",'r') as f:
    data=json.load(f)['data_columns']

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def predict_price(request):

        if request.method == 'POST':
            try:
                

                sqft = float(request.POST.get('sqft', 0))
                bath = int(request.POST.get('bath', 0))
                bhk = int(request.POST.get('bhk', 0))
                location = request.POST.get('location', '').lower()

          

                try:
                    loc_index = data.index(location)
                except ValueError:
                    loc_index = -1

                x = np.zeros(len(data))
                x[0] = sqft
                x[1] = bath
                x[2] = bhk
                if loc_index >= 0:
                    x[loc_index] = 1

                price = model.predict([x])[0]

                # Return the prediction result

                if price < 0:
                    price="There is no house in this location" 
                    return render(request, 'home.html', {'prediction': price})
                
                else:
                    price = round(price, 2)
                    return render(request, 'home.html', {'prediction': price})


            except Exception as e:
                return HttpResponse(f"Error in prediction: {str(e)}")
        else:
            return HttpResponse("Invalid request method.")
