from django.apps import AppConfig
# for ai_model load
import pickle
import joblib
import os
from django.conf import settings


class IrisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris'

    # for ai_model load
    def ready(self):
        # 전역 변수로 모델 로드
        global ml_model
        # model_path = os.path.join(settings.BASE_DIR, 'static/models/iris_model_rfc.pkl')
        model_path = os.path.join(settings.BASE_DIR, 'static/models/iris_model_rfc.joblib')
        with open(model_path, 'rb') as f:
            # self.ml_model = pickle.load(f)
            self.ml_model = joblib.load(f)
        print("AI 모델 로딩 완료!")