# Part I: Training Model


---

1. Create a virtual environment first
	
    - This is really helpful for a Python project to be lightweight.
	- **NOTE** I adopt `$` as a command line specifically for Windows.
	- Run: 
		- `$ python -m venv <name_venv>`
		- I prefer using `part1_venv` avoiding confusing.
	- To activate venv:
		- `$ .\part1_venv\Scripts\activate`
		- Note that this is a windows-cmd format!
		- If the virtual environment is activated, you will notice that the venv name displayed on your terminal.

2. Initially, ML model is trained by data. Thus let's download the data first.
	- See the python file `download_dataset.py`
	- Mention that along with this project, you might confront many module-not-found errors.
		- Fix it simply:
			- `$ python -m pip install <module>`
	- After successfully run `download_dataset.py`, you we get dataset directory such as follows.
```
dataset/
    test/
        1.jpg
        10.jpg
        ...
    train/
        cats/	
            cat.0.jpg
            cat.1.jpg
            ...
        dogs/
            dog.0.jpg
            dog.1.jpg
            ...
```

3. Now, we start training CNN model shown in `train_model.py`. As the description below:
	- See here we use two libraries i.e. Tensorflow and Keras
		- Don't forget to install both
	- We utilize `image_dataset_from_directory` to create generators for train and valid set
	- Later we employ MobileNet model as a backbone and add some dense layers mapping an output.
	- We set training to be just 1 epoch which results look acceptable to me. (accuracy around 0.7)
	- Lastly, we save a model in a name of `cats-and-dogs-model.h5`

**Additional** This dataset is brought from a Kaggle competition so-called [Dogs vs Cats](https://www.kaggle.com/competitions/dogs-vs-cats), you may obey to challenge by joining the competition, fine-tuning your model. so submitting the best of your model to see the result.

That's it for this section. Let move to the next part: [2_CreatingAPI](2_CreatingAPI/README.md).

Isada

---
