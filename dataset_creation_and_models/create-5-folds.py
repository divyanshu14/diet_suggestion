import os
import shutil
import random


BASE_DIR = 'indian-food-dataset-divyanshu'

food_classes = os.listdir(BASE_DIR)

for each_food_class in food_classes:
    food_class_path = os.path.join(BASE_DIR, each_food_class)
    food_images = os.listdir(food_class_path)
    random.shuffle(food_images)

    set1_path_test = os.path.join('sets', 'set1', 'test', each_food_class)
    set1_path_train = os.path.join('sets', 'set1', 'train', each_food_class)
    set2_path_test = os.path.join('sets', 'set2', 'test', each_food_class)
    set2_path_train = os.path.join('sets', 'set2', 'train', each_food_class)
    set3_path_test = os.path.join('sets', 'set3', 'test', each_food_class)
    set3_path_train = os.path.join('sets', 'set3', 'train', each_food_class)
    set4_path_test = os.path.join('sets', 'set4', 'test', each_food_class)
    set4_path_train = os.path.join('sets', 'set4', 'train', each_food_class)
    set5_path_test = os.path.join('sets', 'set5', 'test', each_food_class)
    set5_path_train = os.path.join('sets', 'set5', 'train', each_food_class)

    if not os.path.exists(set1_path_test):
        os.makedirs(set1_path_test)
    if not os.path.exists(set1_path_train):
        os.makedirs(set1_path_train)
    if not os.path.exists(set2_path_test):
        os.makedirs(set2_path_test)
    if not os.path.exists(set2_path_train):
        os.makedirs(set2_path_train)
    if not os.path.exists(set3_path_test):
        os.makedirs(set3_path_test)
    if not os.path.exists(set3_path_train):
        os.makedirs(set3_path_train)
    if not os.path.exists(set4_path_test):
        os.makedirs(set4_path_test)
    if not os.path.exists(set4_path_train):
        os.makedirs(set4_path_train)
    if not os.path.exists(set5_path_test):
        os.makedirs(set5_path_test)
    if not os.path.exists(set5_path_train):
        os.makedirs(set5_path_train)

    # fold1 acts as test set for set1 and so on
    fold1 = food_images[0:100]
    fold2 = food_images[100:200]
    fold3 = food_images[200:300]
    fold4 = food_images[300:400]
    fold5 = food_images[400:500]

    with open('fold-split.txt', 'a+') as f:
        f.write(each_food_class + '\n')
        f.write('\nfold1 images: ')
        for img in fold1:
            f.write(img + ', ')
        f.write('\nfold2 images: ')
        for img in fold2:
            f.write(img + ', ')
        f.write('\nfold3 images: ')
        for img in fold3:
            f.write(img + ', ')
        f.write('\nfold4 images: ')
        for img in fold4:
            f.write(img + ', ')
        f.write('\nfold5 images: ')
        for img in fold5:
            f.write(img + ', ')
        f.write('\n\n\n')

    set1_test = fold1
    for img in set1_test:
        shutil.copy(os.path.join(food_class_path, img), set1_path_test)
    set1_train = fold2 + fold3 + fold4 + fold5
    for img in set1_train:
        shutil.copy(os.path.join(food_class_path, img), set1_path_train)
    set2_test = fold2
    for img in set2_test:
        shutil.copy(os.path.join(food_class_path, img), set2_path_test)
    set2_train = fold1 + fold3 + fold4 + fold5
    for img in set2_train:
        shutil.copy(os.path.join(food_class_path, img), set2_path_train)
    set3_test = fold3
    for img in set3_test:
        shutil.copy(os.path.join(food_class_path, img), set3_path_test)
    set3_train = fold1 + fold2 + fold4 + fold5
    for img in set3_train:
        shutil.copy(os.path.join(food_class_path, img), set3_path_train)
    set4_test = fold4
    for img in set4_test:
        shutil.copy(os.path.join(food_class_path, img), set4_path_test)
    set4_train = fold1 + fold2 + fold3 + fold5
    for img in set4_train:
        shutil.copy(os.path.join(food_class_path, img), set4_path_train)
    set5_test = fold5
    for img in set5_test:
        shutil.copy(os.path.join(food_class_path, img), set5_path_test)
    set5_train = fold1 + fold2 + fold3 + fold4
    for img in set5_train:
        shutil.copy(os.path.join(food_class_path, img), set5_path_train)
