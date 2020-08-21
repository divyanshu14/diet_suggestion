import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing import image
import numpy as np

# output-mobilenetv2
# output-resnet50v2
# output-vgg16
# output-xception

# 19, 6, 7, 11, 11, 11, 13, 14, 14, 24, 24, 15, 28, 28, 25

json_model_path = os.path.join("output-mobilenetv2", "set3", "model.json")
weights_path = os.path.join("output-mobilenetv2", "set3", "model.h5")

# load json and create model
json_file = open(json_model_path, "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights(weights_path)
print("Loaded model from disk")

for i in range(1, 16):
    test_image_path = os.path.join("example-test-images", "example" + str(i) + ".jpg")
    test_image = image.load_img(test_image_path, target_size=(224, 224))
    # predict on image
    x = image.img_to_array(test_image)
    x /= 255
    x = np.expand_dims(x, axis=0)
    prediction_probs = loaded_model.predict(x)
    # print(prediction_probs)
    prediction_classes = prediction_probs.argmax(axis=-1)
    print(prediction_classes)
