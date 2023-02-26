# Twitter_Sentiment_NLP

# Overview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sentiment Analysis is a NLP (Natural Language Processing) problem to determine whether the sentiment is positive or negative. In this case, we use twitter's sentiment to deterimine whether is it positive, negative, neutral or irrelevant. 

# Application

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I built this application using several tools, libraries and frameworks. Especially for notebook I used Google Colab to help me built the model from notebook

1. Tensorflow
2. pandas
3. seaborn
4. matplotlib
5. sklearn
6. numpy
7. zipfile
8. html
9. FastAPI

# Dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The dataset can be download in [kaggle - Twitter Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)

![image](https://user-images.githubusercontent.com/91602612/199688554-a88fbb04-c571-46ce-bf69-2c0b2a92ec96.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are 2 csv in this zipfile:

* twitter_training.csv: for training model

* twittter_validation.csv: for validation data

In this notebook I only use twitter_training.csv 

# Notebook

## Exploratory Data Analysis

**1. Show first five records in dataset**

![image](https://user-images.githubusercontent.com/91602612/199879543-e2eccbed-af7c-4d35-8862-0b072dd7e42d.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; From that picture, we can see that there are no columns name, therefore we add name for each columns. From adding columns name can help us explore this dataset easily.

![image](https://user-images.githubusercontent.com/91602612/199879727-9232496f-d2e9-4df2-99b6-ff59a06044df.png)

**2. We check shape of dataset that there are 74681 rows and 4 columns**

**3. Check missing values in the dataset**

![image](https://user-images.githubusercontent.com/91602612/199882470-1edc3073-039e-49af-9134-2a42c9fc0a39.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We found that there are 686 missing values in tweet_content column, therefore we need to handle it, in this case I remove them and got 73995 rows and 4 columns after removing the missing values

**4. Drop unnecessary columns**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I dropped **tweet_id** and **entity** columns because we did not need that.

**5. Check label**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I checked label and sum of the values to prevent imbalanced data and the data seems balanced after checked the label data.

![image](https://user-images.githubusercontent.com/91602612/199883252-c7460ff8-d4a8-4975-b73f-8f31c582a514.png)

## Data Preprocessing

**1. One Hot Encoding**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; First thing that I did in preprocessing steps is one hot encoding the label data, because label data is categorical data and not numerical. To handle this problem I used pd.get_dummies() to one hot encoding label or sentiment column.

![image](https://user-images.githubusercontent.com/91602612/199888084-5a8b295e-e3ba-4e8b-bc21-aa68746ad92b.png)


**2. Change column into numpy array**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To process the dataset we need to change each columns into numpy array to helps us tokenize them.

![image](https://user-images.githubusercontent.com/91602612/199888236-bc79fec3-72ab-4e20-913c-c393f92654a3.png)

**3. Split data**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Then I splitted the dataset into train_tweet, test_tweet, train_label and test_label with train size 80% and test size 20% and random_state = 42. Then we got this shape:

![image](https://user-images.githubusercontent.com/91602612/199888426-9580f554-b002-44fe-abda-8fd79d12a055.png)

**4. Tokenizer**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; After that I am using tokenizer to tokenize train_tweet with num_words is 10000 and change unknown character with <oov>. After fit tokenizer into train_tweet, I am using tokenizer.texts_to_sequences() to change texts in train_tweet and test_tweet into sequences.

**5. Add padding**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To handle different length in each sequences I used pad_sequences in train_sequences and test_sequences to padding each sequence with parameter max_len = 150, padding='post' therefore the additional values or padding can be in the back of sequence, and truncating = 'post' therefore we crop sequence from back.

## Build Model

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I build model with tensorflow and using Embedding layers and Bidirectional LSTM layers to help me train my model I used input_dim = 10000, output_dim = 16, and input_length = 150.

![image](https://user-images.githubusercontent.com/91602612/199889768-d4556601-db0e-466d-9556-28edc0324eaa.png)


## Evaluate Model

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I am using callback and my callback stop the training in 9 epochs and I got 92% accuracy, 84% val_accuracy, 19% loss and 59% val_loss.

![image](https://user-images.githubusercontent.com/91602612/199889796-5732af08-7e4f-4b30-9b62-d88a54b3ebf6.png)

