import keras
from keras import models, layers
from keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.applications.mobilenet import MobileNet

def generate_datagen(path, image_size, batch_size, ratio_split=0.2):
    train_ds = image_dataset_from_directory(
        path,
        validation_split=ratio_split,
        subset='training',
        seed=1234,
        image_size=image_size,
        batch_size=batch_size,
    )
    val_ds = image_dataset_from_directory(
        path,
        validation_split=ratio_split,
        subset='validation',
        seed=1234,
        image_size=image_size,
        batch_size=batch_size,
    )
    return train_ds, val_ds

# Build simple CNN model w/ transfer learning from MobileNet
def build_model(image_size, output_n):
    base_cnn = MobileNet(input_shape=(image_size[0], image_size[1], 3), include_top=False)
    for layer in base_cnn.layers[:]:
        layer.trainable = False
    model = models.Sequential()
    model.add(base_cnn)
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(units=output_n, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    # model.summary()
    return model

if __name__ == '__main__':
	image_size = (224, 224)
	batch_size = 64
	train, valid = generate_datagen(path='dataset/train', 
									image_size=image_size,
                                	batch_size=batch_size)
	model = build_model(image_size, output_n=2)
	history = model.fit(train, validation_data=valid, epochs=1)
	model.save('cats-and-dogs-model.h5')