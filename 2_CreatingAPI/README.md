# Implementing API

---

1. Same as previous, always start the project by creating a new venv.
    - You may use your abitary name likes part2_venv.
    - DO NOT FORGET TO ACTIVATE THE NEW VIRTUAL ENVIRONMENT!!
    - TIPS: The best practice for starting a new project with Python
        - see https://www.analyticsvidhya.com/blog/2021/06/best-practices-for-becoming-a-good-python-developer/

2. First of all, do copy the saved model (`cat-and-dogs-model.h5`) that was saved from the previous [1_TrainingModel]() to this directory.

3. Before hand-on to the API part, we need to verify that we can load and predict by the model.
    - Check `model.py`
    - We implement a class of the model for simplification purposes.
        - By initializing with passing the model path
        - We load the model using `tensorflow.keras.models.load_model`
    - Then add predict method that can predict a single image.
        - To be able work, we have to prepare an input image the same as one that how the model be fed in the training phase.
    - Next, we test the model's prediction using some images from the dataset.
      - Take a look on the predicted results. Are they match with the truth?  

4. Now, it's time for the main course, Flask API.
    - First install Flask
        - `$ pip install flask`
    - The way to make API is shown in `app.py`, feel free to check it out. Now I will explain what do we do:
        - Briefly, the request is an image and the response is the result of the prediction (cat vs dog).
        - Request:
            - To do so, the only request method that can send an image is called `POST`.
              - Body: a key is `image` and a value is `file`.
            - To be correct we also need to declare the header matched with the image file with extension e.g. JPG, PNG, .. etc.
        - Respond:
            - It is obvious that we just return a JSON that the result of the model to the client.
    - So let run flask:
        - `$ python app.py`

    - For testing, There are several ways:
        - Postman: Set as follows.
            - url: `http://localhost:5000/classify/image`
            - header: `{'enctype' : 'multipart/form-data'}`
            - (alternative) header: `{'enctype' : application/x-www-form-urlencoded}`
            - Body: `{'image' : <upload file>}`
        - cURL:
            - `$ curl --form image=@path/to/image http://localhost:5000/classify/image`
            - Use CMD, it is not work for PowerShell.
            - This is Windows cURL. The format differs from others.

5. Before going to the next section, let's create the `requirements.txt`
    - It is a text file listing python libraries that be used in the codes 
    - By running this cmd:
        - `$ python -m pip freeze > requirements.txt`

Yeah! Now you learn how to write an API. Let's move to the next one [3_DockerizingApp]() related to how we can build a docker image.

Isada

---