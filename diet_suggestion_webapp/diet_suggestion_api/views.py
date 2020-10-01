#importing necessary libraries
from rest_framework.response import Response
from tensorflow.keras.preprocessing import image
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from PIL import Image
from .apps import DietSuggestionApiConfig
import base64
import numpy as np
import io
import os


class PredictFoodItem(APIView):

    @csrf_exempt
    def get(self, request, format=None):
        example_fpath = os.path.join(settings.BASE_DIR, DietSuggestionApiConfig.name, "configFiles", "example-test-images", "example1.jpg")
        with open(example_fpath, "rb") as imageFile:
            data = base64.b64encode(imageFile.read()).decode()
        return Response({"food_image": data}, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        bin_str_imgdata = base64.b64decode(request.data["food_image"])
        bytes_imgdata = io.BytesIO(bin_str_imgdata)
        test_image = Image.open(bytes_imgdata).convert("RGB").resize(size=(224,224))
        x = image.img_to_array(test_image)
        x /= 255
        x = np.expand_dims(x, axis=0)
        prediction_probs = DietSuggestionApiConfig.food_model.predict(x)
        # print(prediction_probs)
        prediction_classes = prediction_probs.argmax(axis=-1)
        # print(prediction_classes)
        responseData = {
            "food_item": DietSuggestionApiConfig.food_classes[prediction_classes[0]],
            "nutritional_info": DietSuggestionApiConfig.food_nutrients[prediction_classes[0]],
        }
        return Response(responseData, status=status.HTTP_200_OK)
