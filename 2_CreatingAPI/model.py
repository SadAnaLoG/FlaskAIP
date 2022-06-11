from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

class CatsAndDogsClassifier:
	def __init__(self, model_path):
		self.model = load_model(model_path)
		self.input_shape = (self.model.input_shape[1], self.model.input_shape[2])

	def predict(self, image):
		image = cv2.resize(image, self.input_shape) #resize to (224, 224)
		image = np.array([image]) #now shape: (1, 224, 224, 3)
		pred = self.model.predict(image)
		return 'cat' if pred.argmax() == 0 else 'dog'

if __name__ == '__main__':
	#load model from the saved model
	model = CatsAndDogsClassifier('cats-and-dogs-model.h5')
	# load sample images
	sample_images =	['../0_PreparingModel/dataset/train/cats/cat.0.jpg',
	'../0_PreparingModel/dataset/train/dogs/dog.0.jpg',
	'../0_PreparingModel/dataset/test/1.jpg', #dog
	'../0_PreparingModel/dataset/test/10.jpg'] #cat
	#run test
	for im in sample_images:
		x = cv2.imread(im)
		print(im, model.predict(x))