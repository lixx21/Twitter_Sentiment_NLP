import tensorflow as tf
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = tf.keras.models.load_model('../model/sentiment_model.h5', compile=False)
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')

#model.summary()

#laod tokenizer from pickle
with open('../model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/index/')
def index():
    return 'hello world'

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post('/predict')
async def predict(request: Request, text: str = Form()):

    classes = ['Irrelevant','Negative', 'Neutral', 'Positive']

    # text = "Just realized the windows partition of my Mac is now 6 years behind on Nvidia drivers and I have no idea how he didn’t notice"
    sequence = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(sequence,
                       maxlen = 150,
                       padding = 'post',
                       truncating = 'post')
    
    pred = model.predict(pad)

    num_pred = np.argmax(pred)

    sentiment = classes[num_pred]
    return templates.TemplateResponse("home.html", {"request": request, 'sentiment':sentiment, 'text':text})
    # return {'sentiment':sentiment}








