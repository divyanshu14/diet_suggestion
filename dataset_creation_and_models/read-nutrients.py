import os
import json

BASE_DIR = "indian-food-dataset-divyanshu-nutrients"
files = os.listdir(BASE_DIR)

for each_file in files:
    with open(os.path.join(BASE_DIR, each_file)) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        new_serving_size_lines = []
        whole_food_info = []
        i = 0
        for i in range(len(lines)):
            if lines[i] == "Nutrition Facts":
                new_serving_size_lines.append(i)
        for new_serving in new_serving_size_lines:
            serving_size = lines[new_serving+1][13:]
            calories = lines[new_serving+4][9:lines[new_serving+4].find("Calories from Fat")]
            calories_from_fat = lines[new_serving+4][lines[new_serving+4].find("Calories from Fat")+18:]
            total_fat = lines[new_serving+7][10:lines[new_serving+7].rfind("g")+1]
            total_fat_percent = lines[new_serving+7][lines[new_serving+7].rfind("g")+1:]
            saturated_fat = lines[new_serving+8][14:lines[new_serving+8].rfind("g")+1]
            saturated_fat_percent = lines[new_serving+8][lines[new_serving+8].rfind("g")+1:]
            trans_fat = lines[new_serving+9][10:]
            cholesterol = lines[new_serving+10][12:lines[new_serving+10].rfind("g")+1]
            cholesterol_percent = lines[new_serving+10][lines[new_serving+10].rfind("g")+1:]
            sodium = lines[new_serving+11][7:lines[new_serving+11].rfind("g")+1]
            sodium_percent = lines[new_serving+11][lines[new_serving+11].rfind("g")+1:]
            potassium = lines[new_serving+12][10:lines[new_serving+12].rfind("g")+1]
            potassium_percent = lines[new_serving+12][lines[new_serving+12].rfind("g")+1:]
            total_carbohydrate = lines[new_serving+13][19:lines[new_serving+13].rfind("g")+1]
            total_carbohydrate_percent = lines[new_serving+13][lines[new_serving+13].rfind("g")+1:]
            dietary_fiber = lines[new_serving+14][14:lines[new_serving+14].rfind("g")+1]
            dietary_fiber_percent = lines[new_serving+14][lines[new_serving+14].rfind("g")+1:]
            sugars = lines[new_serving+15][7:]
            protein = lines[new_serving+16][8:lines[new_serving+16].rfind("g")+1]
            protein_percent = lines[new_serving+16][lines[new_serving+16].rfind("g")+1:]
            temp_list = lines[new_serving+18].split()
            vitamin_A_percent = temp_list[2]
            vitamin_C_percent = temp_list[6]
            temp_list = lines[new_serving+19].split()
            calcium_percent = temp_list[1]
            iron_percent = temp_list[4]
            nut_info_dict = {
                "food_item": each_file[:-4],
                "serving_size": serving_size,
                "calories": calories,
                "calories_from_fat": calories_from_fat,
                "total_fat": total_fat,
                "total_fat_percent": total_fat_percent,
                "saturated_fat": saturated_fat,
                "saturated_fat_percent": saturated_fat_percent,
                "trans_fat": trans_fat,
                "cholesterol": cholesterol,
                "cholesterol_percent": cholesterol_percent,
                "sodium": sodium,
                "sodium_percent": sodium_percent,
                "potassium": potassium,
                "potassium_percent": potassium_percent,
                "total_carbohydrate": total_carbohydrate,
                "total_carbohydrate_percent": total_carbohydrate_percent,
                "dietary_fiber": dietary_fiber,
                "dietary_fiber_percent": dietary_fiber_percent,
                "sugars": sugars,
                "protein": protein,
                "protein_percent": protein_percent,
                "vitamin_A_percent": vitamin_A_percent,
                "vitamin_C_percent": vitamin_C_percent,
                "calcium_percent": calcium_percent,
                "iron_percent": iron_percent,
            }
            whole_food_info.append(nut_info_dict)
        # print(whole_food_info)
        with open(os.path.join("indian-food-dataset-divyanshu-nutrients-json", each_file), "w") as outfile:
            json.dump(whole_food_info, outfile)
