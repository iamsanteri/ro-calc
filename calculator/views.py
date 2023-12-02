from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import PredictionForm
from django.views import View
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import joblib
import numpy as np
import sklearn

# Load the model and the encoders
model = joblib.load('jupyter/model.pkl')
encoder = joblib.load("jupyter/encoder.pkl")
le = joblib.load("jupyter/le.pkl")

def process_user_input(user_input):
    # Convert user input into DataFrame
    # Encode the data with the same encoders used during model training
    data_encoded = encoder.transform(data)
    return data_encoded

def index(request): 
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = pd.DataFrame(form.cleaned_data, index=[0])
            data = data.rename(columns={
                'feature1': 'Favorite Color',
                'feature2': 'Favorite Music Genre',
                'feature3': 'Favorite Beverage',
                'feature4': 'Favorite Soft Drink'
            })
            data_encoded = encoder.transform(data)
            prediction = model.predict(data_encoded)
            prediction = le.inverse_transform(prediction)
            return render(request, 'index.html', {'form': form, 'prediction': prediction})
        return render(request, 'index.html', {'form': form})    
    else:
        form = PredictionForm()
        return render(request, 'index.html', {'form': form})


# Step 9: Create an API endpoint
class PredictView(View):
    def post(self, request):
        data = request.POST
        prediction = model.predict([data])
        return JsonResponse({'prediction': prediction.tolist()})