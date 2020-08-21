from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import CSVLogger
import pickle
import os


sets = ["set1"]


for set_folder in sets:

    num_epochs = 100
    num_classes = 29
    img_width, img_height = 224, 224
    train_data_dir = os.path.join("sets", set_folder, "train")
    val_data_dir = os.path.join("sets", set_folder, "test")
    batch_size = 16

    train_datagenerator = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip=True
    )

    val_datagenerator = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagenerator.flow_from_directory(
        train_data_dir,
        target_size=(img_height, img_width),
        class_mode="categorical",
        batch_size=batch_size,
        shuffle=True
    )

    val_generator = val_datagenerator.flow_from_directory(
        val_data_dir,
        target_size=(img_height, img_width),
        class_mode="categorical",
        batch_size=batch_size,
        shuffle=True
    )

    base_model = MobileNetV2(include_top=False, weights="imagenet", input_shape=(img_width, img_height, 3))
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(2048, activation="relu")(x)
    x = Dropout(0.2)(x)
    x = Dense(2048, activation="relu")(x)
    x = Dropout(0.2)(x)
    predictions = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    # all but last 5 layers
    for layer in model.layers[:-5]:
        layer.trainable = False
    # last 5 layers
    for layer in model.layers[-5:]:
        layer.trainable = True

    model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9), loss="categorical_crossentropy", metrics=["accuracy"])

    model.summary()

    output_folder_path = os.path.join("hyperparameter-tuning-mobilenetv2", set_folder)
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    csv_logger_filepath = os.path.join(output_folder_path, "history.log")
    csv_logger = CSVLogger(csv_logger_filepath)

    history = model.fit(train_generator,
                        epochs=num_epochs,
                        validation_data=val_generator,
                        verbose=1,
                        callbacks=[csv_logger]
    )

    # probably won't reach here becuase training would be stopped in between
    history_object_filepath  = os.path.join(output_folder_path, "history_dict")
    with open(history_object_filepath, "wb") as history_object:
        pickle.dump(history.history, history_object)
