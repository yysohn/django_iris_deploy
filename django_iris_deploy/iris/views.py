from django.shortcuts import render
from django.shortcuts import render
import numpy as np
from django import forms
from django.apps import apps
import pickle

# Create your views here.
def iris_home(request):
    context={}
    # context={'data':"hello"}
    return render(request, 'iris_home.html', context)

# predict 처리하는 함수 정의
class IrisForm(forms.Form):
    sepal_length = forms.FloatField(label='sepal_length', required=True)
    sepal_width = forms.FloatField(label='sepal_width', required=True)
    petal_length = forms.FloatField(label='petal_length', required=True)
    petal_width = forms.FloatField(label='petal_width', required=True)

def predict(request):
    # pickle 모델 로드
    if request.method == 'POST':
        form = IrisForm(request.POST)

        if form.is_valid() :    
            sepal_length = form.cleaned_data['sepal_length']
            sepal_width = form.cleaned_data['sepal_width']
            petal_length = form.cleaned_data['petal_length']
            petal_width = form.cleaned_data['petal_width']
            iris_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            print(iris_data)
            # 모델 로딩하기
            # with open('static/models/iris_model_rfc.pkl', 'rb') as f:
            #     model = pickle.load(f)

            # 로딩된 모델 사용하기
            iris_config = apps.get_app_config('iris')
            model = iris_config.ml_model

            pred = model.predict(iris_data)
            context={'predict':pred}
        
    return render(request, 'predict.html', context)   