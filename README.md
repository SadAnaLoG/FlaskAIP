# Tutorial FlaskAPI


---

**Intro**

Here, I concretely demonstrate the way to build simple API for the ML model. This app is called Cats-and-Dogs classification API, which the objective is to separate whether it is a cat or dog from an entire image. Thanks to [Kaggle](https://www.kaggle.com/competitions/dogs-vs-cats) for available dataset. Before getting start and further exploring, let me outline an overview.

This tutorial project consists of three parts following:
- [1_TrainingModel](1_TrainingModel/README.md) Training a Cats-and-Dogs model using CNN (Keras) and saving a model.
- [2_CreatingAPI](2_CreatingAPI/README.md) In here, we copy source codes from the above one and list all using libraries in a requirements file manually. Then we write `app.py` in a form of `Flask` API.
- [3_DockerizingApp](3_DockerizingApp/README.md) To prevent setting-environment problems, we employ Docker to build an image and test it by running a container on local.

**Future Moves**
However, it is really hard to draw instructions deploying an app into a server with just article. So, in further step, I will record a video for deploying the app in docker on the Linux-based Huawei cloud. Stay tuned!

Hope you enjoy learning! 
Isada

---