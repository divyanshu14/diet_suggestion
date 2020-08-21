from django.apps import AppConfig
from django.conf import settings
import os
import json

from tensorflow.keras.models import model_from_json


class DietSuggestionApiConfig(AppConfig):
    name = 'diet_suggestion_api'

    @staticmethod
    def load_model_and_weights(json_model_path, model_weights_path):
        with open(json_model_path, "r") as json_file:
            loaded_model_json = json_file.read()
            loaded_model = model_from_json(loaded_model_json)
            loaded_model.load_weights(model_weights_path)
            return loaded_model

    @staticmethod
    def load_classes(classes_path):
        classes = []
        with open(classes_path) as f:
            for one_class in f:
                classes.append(one_class.strip())
        return classes

    @staticmethod
    def load_food_nutrients(food_nutrients_folder_path):
        food_nutrients_dict = []
        all_food_nutrients_files = os.listdir(food_nutrients_folder_path)
        for food_nutrients_file in all_food_nutrients_files:
            food_nutrients_file_fpath = os.path.join(food_nutrients_folder_path, food_nutrients_file)
            with open(food_nutrients_file_fpath) as f:
                food_nutrients_dict.append(json.load(f))
        return food_nutrients_dict

    json_model_path = os.path.join(settings.BASE_DIR, name, 'configFiles', 'output-mobilenetv2', 'set3', 'model.json')
    model_weights_path = os.path.join(settings.BASE_DIR, name, 'configFiles', 'output-mobilenetv2', 'set3', 'model.h5')
    food_model = load_model_and_weights.__func__(json_model_path, model_weights_path)

    food_classes_path = os.path.join(settings.BASE_DIR, name, 'configFiles', 'food_classes.txt')
    food_classes = load_classes.__func__(food_classes_path)

    food_nutrients_folder_path = os.path.join(settings.BASE_DIR, name, 'configFiles', 'indian-food-dataset-divyanshu-nutrients-json')
    food_nutrients = load_food_nutrients.__func__(food_nutrients_folder_path)
