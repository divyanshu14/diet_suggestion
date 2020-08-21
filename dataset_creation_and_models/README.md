This folder contains all the essential files for creation of dataset, making 5 folds, finding hyperparameters (based on experimentation) and finally training the models.

You must have python 3.6.8 installed with all the requirements as specified in the README.md of diet_suggestion_webapp. Here is the description of files in this folder:

1. create-dataset.py - create dataset by downloading 500 images per class using bing_image_downloader for each class specified in download-dataset-query-strings.txt and to note down the sources, instead of simply running <b>python create-dataset.py</b> you must use the command <b>python create-dataset.py > dataset-creation-sources.txt</b> and all the sources will get noted in dataset-creation-sources.txt file in the same directory

2. create-5-folds.py - randomly divide the dataset in indian-food-dataset-divyanshu folder into 5 folds and then create 5 folders (set1, set2, set3, set4, set5) where each folder has 1 fold as hold out (test set) and other 4 folds as training set

3. find-hyperparameters-<model_name>-keras-gpu.py - Train the model to find hyperparameters suitable for the <model_name> model

4. model-<model_name>-keras-gpu.py - train the <model_name> model for all the 5 sets and save the results

5. predict-food.py - simple file to use a model to predict the food (change the json model path and model weights path and image path so as to use your own model to predict your own image)

6. read-nutrients.py - read copy pasted nutritional information data saved in indian-food-dataset-divyanshu-nutrients folder and convert it into json serializable format data which will be saved in indian-food-dataset-divyanshu-nutrients-json folder, which can be used to generate response in our webapp

7. dataset-creation-sources.txt - contains the source names from where each image has been downloaded for the dataset used in our application

8. download-dataset-query-strings.txt - each line in this file specifies what query string you want to search for in the bing search to create the dataset (currently contains 29 india food item names)

9. fold-split.txt - for the dataset created by us, this file notes how the random 5 folds were created (if you create new folds, since folds are created randomly you might get new values in this file)

10. nutrients-website.txt - contains links to the web sources from where nutritional information as present in the files of indian-food-dataset-divyanshu-nutrients folder were taken

Also note that the folders output-<model_name> contain the output of training <model_name> model done by us. Due to github size limits, model.json and model.h5 files have not been uploaded but the output scores that we got have been recorded.
