#app.py
from model import CatsAndDogsCalssifier
import flask
import cv2

def init():
    global model
    model = CatsAndDogsCalssifier('cats-and-dogs-model.h5')

app = flask.Flask(__name__)
init()

@app.route('/')
def index():
    respond = { 'Service': 'CatsAndDogsClassifier',
                'Project' : 'FlaskAPI',
                'POST' : [{ 'route' : '/classify/image',
                            'header': 'enctype : multipart/form-data',
                            'image' : 'file w/ {.png, .jpg, .JPEG, etc.}'}]}
    return flask.jsonify(respond)

@app.route("/classify/image", methods=['POST'])
def classify_image():
    respond = {"success": False}
    if flask.request.method == "POST":
        open('upload.png', mode='wb').write(flask.request.files["image"].read())
        image = cv2.imread('upload.png')
        preds = model.predict(image)
        respond['results'] = preds
        respond['success'] = True

    return flask.jsonify(respond)

#Run app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)