# -*- coding: utf-8 -*-
"""NLP_DICODING_FELIX PRATAMASAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hE83tx_UmPpFoNNp9Z9O4g4gJz1XvM2i

# Nama: Felix Pratamasan
# Email: felixpratama242@gmail.com
"""

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import seaborn as sns
from google.colab import files
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report

"""# Download File from Kaggle"""

#you need to create your own API first in kaggle
#upload kaggle json

files.upload()

#create a kaggle folder
!mkdir ~/.kaggle

#copy kaggle.json to folder created
!cp kaggle.json ~/.kaggle/

#permission for the json to act
! chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d jp797498e/twitter-entity-sentiment-analysis

"""#Read Dataset"""

test_local_zip = '/content/twitter-entity-sentiment-analysis.zip'
zip_ref = zipfile.ZipFile(test_local_zip, 'r')
zip_ref.extractall('/content/dataset')

zip_ref.close()

training_data = pd.read_csv('/content/dataset/twitter_training.csv')

training_data.head()

# add columns name

columns = ['tweet_id', 'entity', 'sentiment', 'tweet_content']
training_data.columns = columns

training_data.head()

#print shape of training data
training_data.shape

training_data.info()

#check missing value
training_data.isnull().sum()

#remove missing values
training_data = training_data.dropna()

#check missing values after remove them
training_data.isnull().sum()

"""# Exploratory Data Analysist"""

#dropping 'tweet_id', 'entity'
training_data = training_data.drop(['tweet_id', 'entity'], axis=1)

print('shape after remove missing values and drop columns: {}'.format(training_data.shape))

sentiments = training_data['sentiment']

# plot label
x_axis = sentiments.value_counts().index
y_axis = sentiments.value_counts()

print(y_axis)

plt.title('Label')
sns.barplot(x = x_axis, y = y_axis,  data=training_data)
plt.show()

"""# Data Preprocessing

"""

onehot_sentiments = pd.get_dummies(training_data['sentiment'])
training_data_clean = pd.concat([training_data, onehot_sentiments], axis=1)
training_data_clean = training_data_clean.drop(columns='sentiment')
training_data_clean

# change column into numpy array
tweet = training_data_clean['tweet_content'].values
label = training_data_clean[['Irrelevant','Negative', 'Neutral', 'Positive']].values

print('twwet type: {}\n{}\n'.format(type(tweet),tweet))
print('label type: {}\n{}'.format(type(label),label))

#split data
train_tweet, test_tweet, train_label, test_label = train_test_split(tweet, label, test_size = 0.2, random_state = 42)

print('shape train_tweet: {}'.format(train_tweet.shape))
print('shape test_tweet: {}'.format(test_tweet.shape))
print('shape label_train: {}'.format(train_label.shape))
print('shape label_test: {}'.format(test_label.shape))

tokenizer = Tokenizer(num_words=10000, oov_token = '<oov>')

tokenizer.fit_on_texts(train_tweet)

#check word index in tokenizer
print(tokenizer.word_index)

train_sequences = tokenizer.texts_to_sequences(train_tweet)
test_sequences = tokenizer.texts_to_sequences(test_tweet)

train_pad = pad_sequences(train_sequences,
                          maxlen = 150,
                          padding = 'post',
                          truncating = 'post')

test_pad = pad_sequences(test_sequences,
                          maxlen = 150,
                          padding = 'post',
                          truncating = 'post')

"""# Buil Model"""

# class myCallback(tf.keras.callbacks.Callback):
#   def on_epoch_end(self, epoch, logs={}):
#     if(logs.get('accuracy')>=0.92 and logs.get('val_accuracy')>=0.92):
#       print("\nAkurasi telah mencapai >= 92%!")
#       self.model.stop_training = True
# callbacks = myCallback()

callbacks = EarlyStopping(monitor = 'val_loss',
                        patience = 3,
                        verbose = 1)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim = 10000, output_dim=16, input_length = 150),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences = True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    # tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    # tf.keras.layers.LSTM(16),
    # tf.keras.layers.LSTM(32, return_sequences=True),
    tf.keras.layers.Flatten(),
    # tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')

])

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')

history = model.fit(train_pad, train_label,
                    batch_size = 128,
                    steps_per_epoch = len(tweet) // 128,
                    epochs = 30,
                    validation_data = (test_pad, test_label),
                    verbose = 1,
                    callbacks=[callbacks])

# Plot the training and validation accuracies for each epoch

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

fig = plt.figure(figsize = (15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


ax1.plot(epochs, acc, 'r', label='Training accuracy')
ax1.plot(epochs, val_acc, 'b', label='Validation accuracy')
ax1.set_title('Training and validation accuracy')
ax1.legend(loc=0)


ax2.plot(epochs, loss, 'r', label='Training loss')
ax2.plot(epochs, val_loss, 'b', label='Validation loss')
ax2.set_title('Training and validation loss')
ax2.legend(loc=0)


plt.show()