# Twitter_Sentiment_NLP

# Overview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sentiment Analysis is a NLP (Natural Language Processing) problem to determine whether the sentiment is positive or negative. In this case, we use twitter's sentiment to deterimine whether is it positive, negative, neutral or irrelevant. 


# Dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The dataset can be download in [kaggle - Twitter Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)

![image](https://user-images.githubusercontent.com/91602612/199688554-a88fbb04-c571-46ce-bf69-2c0b2a92ec96.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are 2 csv in this zipfile:

* twitter_training.csv: for training model

* twittter_validation.csv: for validation data

In this notebook I only use twitter_training.csv 


# Exploratory Data Analysis

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

# Data Preprocessing

**1. One Hot Encoding**

**2. Change column into numpy array**

**3. Split data**

**4. Tokenizer**

**5. Add padding**

# Build Model

# Evaluate Model
