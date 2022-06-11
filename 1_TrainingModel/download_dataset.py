import gdown
import zipfile
import os
from tqdm import tqdm
import shutil

if __name__ == '__main__':
	# Download cats-and-dogs dataset
	url = "https://drive.google.com/file/d/1HjbcZKzJLl0U5R13znLvRWjC_uHvwtmf/view?usp=sharing"
	output = "cats-and-dogs.zip"
	gdown.download(url=url, output=output, quiet=False, fuzzy=True)

	# Unzip cats-and-dogs.zip
	with zipfile.ZipFile("cats-and-dogs.zip", 'r') as zip_ref:
		zip_ref.extractall(".")

	# Unzip cats-and-dogs/train.zip to dataset
	with zipfile.ZipFile("cats-and-dogs/train.zip", 'r') as zip_ref:
		zip_ref.extractall("dataset")

	# Unzip cats-and-dogs/test.zip to dataset
	with zipfile.ZipFile("cats-and-dogs/test.zip", 'r') as zip_ref:
		zip_ref.extractall("dataset")

	# rename test1 to test
	os.rename('dataset/test1', 'dataset/test')
	
	# Rearrange train directory for flow from directory proposal
	os.mkdir('dataset/train/dogs')
	os.mkdir('dataset/train/cats')
	images = os.listdir('dataset/train')
	import tqdm, shutil
	for im in tqdm(images):
		if 'dog' in im:
			shutil.move(os.path.join('dataset/train', im), 'dataset/train/dogs')
		else:
			shutil.move(os.path.join('dataset/train', im), 'dataset/train/cats')
