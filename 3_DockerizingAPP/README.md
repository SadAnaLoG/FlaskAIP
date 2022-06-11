# Dockerizing App

---

1. You copy files from the previous to this folder.
    - Copy `app.py`, `model.py`, `cats-and-dogs-model.h5`, `requirements.txt`
    - Create directory name `app`
    - drag `app.py`, `model.py`, `cats-and-dogs-model.h5` into `app`
    - This directory be like:
```
2_DocerizingAPP/
    README.md
    dockerfile    
    requirements.txt
    app/
        app.py
        model.py
        cats-and-dogs-model.h5
```

2. We first need to install Docker.
    - Optionally, we can install using Winget
        - `$ winget install -e --id Docker.DockerDesktop`

**Info**: using docker is very simple, you just only need to understand the basic concept.
- **Docker Image** is adopted as the instruction for creating your web application.
    - Including source codes and the dependencies that be used in the app.
    - Generally, we communicate docker images using internet sockets.
- **Docker Container** is an instance that follows instructions to create an app from docker images.
    - One Container also can be built with many images that work together.
    - You can have a Python-based app image work with DB images such as SQL or Redis. (Here, to run, we use Docker-compose) 
    - Therefore, Container is said to be the production of dockers images.

3. Write `dockerfile` served as an instruction to create Cats-and-Dogs app.
    
    - Take a look at `dockerfile`, we now discuss it line by line:

```
FROM python # declare the language that we used

RUN apt-get -y update # update apt-get
RUN apt-get install python3-opencv -y # install dependencies for opencv

ADD ./app /home/app/ # add folder app in current directory to image directory
ADD requirements.txt /home/app/ # add requirements.txt in current directory to image directory

WORKDIR /home/app/ # set current work directory

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

ENTRYPOINT ["python3", "app.py"] # run Flask
```
4. Now, let build an docker image:
   - To do so,
     - `$ docker build -t dogs_and_cats_classifier_api:v1.0 .`
        - Do forget `.` refer to build from the current work directory
        - `-t` means name:tag i.e. tag is `v1.0`
    - Let check out the existing of the image: 
        - `$ docker images`
    - To run the image:
        - `$ docker run -d -p 5000:5000 dogs_and_cats_classifier_api:v1.0`
        - `-p` means mapping port from outside:inside docker
    - To see is the image up?
        - `$ curl localhost:5000`

5. Test your API the same as the previous to see if the service up
- Postman: Set as follows.
   - url: `http://localhost:5000/classify/image`
   - header: `{'enctype' : 'multipart/form-data'}`
       - Alternative header: `{'enctype' : application/x-www-form-urlencoded}`
   - Body: `{'image' : <upload file>}`
- cURL:
   - `$ curl --form image=@path/to/image http://localhost:5000/classify/image`

Finally, now we can bring your model and implement it in the API service. Moreover, you make it can be run in any environment no matter what. I hope this tutorial is helpful for you.

Isada

---