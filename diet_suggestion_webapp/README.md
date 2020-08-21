This is the Nutrients Detection webapp which provides an API where any application can make a post request to with <b>food_image</b> as the key which has the value of the image represented in base64 format. The response will be a json object as follows:

{
  "food_item": "butter_chicken",
  "nutritional_info": [
    {
      "food_item": "butter_chicken",
      "serving_size": "1 cup",
      "calories": "485",
      "calories_from_fat": "0",
      "total_fat": "34.9g",
      "total_fat_percent": "54%",
      "saturated_fat": "12.4g",
      "saturated_fat_percent": "62%",
      "trans_fat": "0g",
      "cholesterol": "126mg",
      "cholesterol_percent": "42%",
      "sodium": "455mg",
      "sodium_percent": "19%",
      "potassium": "537mg",
      "potassium_percent": "15%",
      "total_carbohydrate": "10.4g",
      "total_carbohydrate_percent": "3%",
      "dietary_fiber": "2.9g",
      "dietary_fiber_percent": "12%",
      "sugars": "3.4g",
      "protein": "33.3g",
      "protein_percent": "67%",
      "vitamin_A_percent": "22%",
      "vitamin_C_percent": "12%",
      "calcium_percent": "12%",
      "iron_percent": "22%"
    },
    {
      "food_item": "butter_chicken",
      "serving_size": "240 grams",
      "calories": "485",
      "calories_from_fat": "0",
      "total_fat": "34.9g",
      "total_fat_percent": "54%",
      "saturated_fat": "12.4g",
      "saturated_fat_percent": "62%",
      "trans_fat": "0g",
      "cholesterol": "126mg",
      "cholesterol_percent": "42%",
      "sodium": "455mg",
      "sodium_percent": "19%",
      "potassium": "537mg",
      "potassium_percent": "15%",
      "total_carbohydrate": "10.4g",
      "total_carbohydrate_percent": "3%",
      "dietary_fiber": "2.9g",
      "dietary_fiber_percent": "12%",
      "sugars": "3.4g",
      "protein": "33.3g",
      "protein_percent": "67%",
      "vitamin_A_percent": "22%",
      "vitamin_C_percent": "12%",
      "calcium_percent": "12%",
      "iron_percent": "22%"
    },
    {
      "food_item": "butter_chicken",
      "serving_size": "1 serving (120 g)",
      "calories": "243",
      "calories_from_fat": "0",
      "total_fat": "17.5g",
      "total_fat_percent": "27%",
      "saturated_fat": "6.2g",
      "saturated_fat_percent": "31%",
      "trans_fat": "0g",
      "cholesterol": "63.1mg",
      "cholesterol_percent": "21%",
      "sodium": "228mg",
      "sodium_percent": "9%",
      "potassium": "269.1mg",
      "potassium_percent": "8%",
      "total_carbohydrate": "5.2g",
      "total_carbohydrate_percent": "2%",
      "dietary_fiber": "1.5g",
      "dietary_fiber_percent": "6%",
      "sugars": "1.7g",
      "protein": "16.7g",
      "protein_percent": "33%",
      "vitamin_A_percent": "11%",
      "vitamin_C_percent": "6%",
      "calcium_percent": "6%",
      "iron_percent": "11%"
    },
    {
      "food_item": "butter_chicken",
      "serving_size": "1 oz",
      "calories": "57",
      "calories_from_fat": "0",
      "total_fat": "4.1g",
      "total_fat_percent": "6%",
      "saturated_fat": "1.5g",
      "saturated_fat_percent": "7%",
      "trans_fat": "0g",
      "cholesterol": "14.8mg",
      "cholesterol_percent": "5%",
      "sodium": "53.5mg",
      "sodium_percent": "2%",
      "potassium": "63.1mg",
      "potassium_percent": "2%",
      "total_carbohydrate": "1.2g",
      "total_carbohydrate_percent": "0%",
      "dietary_fiber": "0.3g",
      "dietary_fiber_percent": "1%",
      "sugars": "0.4g",
      "protein": "3.9g",
      "protein_percent": "8%",
      "vitamin_A_percent": "3%",
      "vitamin_C_percent": "1%",
      "calcium_percent": "1%",
      "iron_percent": "3%"
    }
  ]
}

For the first time setup, create a virtual environment - https://docs.python.org/3/tutorial/venv.html - with Python 3.6.8 and then activate it.

After activating the virtual environment in terminal or shell or command prompt, browse to the directory containing this README.md file and run the following commands in order:

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

After successful execution of the above commands, you can run the server using the following command:

python manage.py runserver

When the server starts running, you can see the address where the website is hosted on your terminal or shell or command prompt. Simply visit that link in your web browser and you are good to go.

Suppose that the address where the website is hosted is http://127.0.0.1:8000/ then the following URL is of interest:

http://127.0.0.1:8000/diet_suggestion_api/predict_food_item/

GET request to the above URL will give you a response with the key <b>food_image</b> which has a hard coded value of an image of papdi chaat in base64 format.

For a quick example of how the API works, you can copy the response from the GET request above and use that response as the POST request data to the same URL http://127.0.0.1:8000/diet_suggestion_api/predict_food_item/ and you will get the response accordingly.

In a nutshell, you must convert your image to base64 format and use that value for the key <b>food_image</b> and make a POST request to http://127.0.0.1:8000/diet_suggestion_api/predict_food_item/ to get the response as defined in the start.
