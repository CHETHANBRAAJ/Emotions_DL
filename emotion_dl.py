# -*- coding: utf-8 -*-
"""Emotion_DL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13y53IV5iZdKTy6FqzPnSWqJwbeS9wIcG
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pandas as pd

import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path_1 = r'/content/C__Users_CHETHU_Downloads_anger (1).csv'
file_path_2 =r'/content/C__Users_CHETHU_Downloads_fear.csv'
file_path_3=r'/content/C__Users_CHETHU_Downloads_joy.csv'
file_path_4=r'/content/C__Users_CHETHU_Downloads_sad.csv'
file_path_11 = r'/content/C__Users_CHETHU_Downloads_anger2.csv'
file_path_22 =r'/content/C__Users_CHETHU_Downloads_fear2.csv'
file_path_33=r'/content/C__Users_CHETHU_Downloads_joy2.csv'
file_path_44=r'/content/C__Users_CHETHU_Downloads_sad2.csv'

# Specify column names
column_names = ['id', 'text', 'Emotions', 'intensity']  # Add as many column names as needed

# Read CSV file without header
df1 = pd.read_csv(file_path_1, header=None)
df2 = pd.read_csv(file_path_2, header=None)
df3=pd.read_csv(file_path_3, header=None)
df4=pd.read_csv(file_path_4, header=None)
df5 = pd.read_csv(file_path_11, header=None)
df6 = pd.read_csv(file_path_22, header=None)
df7=pd.read_csv(file_path_33, header=None)
df8=pd.read_csv(file_path_44, header=None)


# Assign column names to the DataFrame
df1.columns = column_names
df2.columns = column_names
df3.columns = column_names
df4.columns = column_names
df5.columns = column_names
df6.columns = column_names
df7.columns = column_names
df8.columns = column_names

# Now you have a DataFrame with column names
dff = pd.concat([df1, df2, df3, df4,df5, df6, df7, df8], ignore_index=True)

dataset = pd.DataFrame(dff)

# Install the required libraries
# pip install tensorflow scikit-learn pandas numpy

# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Load your dataset
# Assuming you have a CSV file named 'your_dataset.csv'


# Preprocess the data
X = dataset['text'].values
y_emotion = dataset['Emotions'].values
y_intensity = dataset['intensity'].values

# Encode emotion labels
label_encoder_emotion = LabelEncoder()
y_emotion = label_encoder_emotion.fit_transform(y_emotion)

# Encode intensity labels
label_encoder_intensity = LabelEncoder()
y_intensity = label_encoder_intensity.fit_transform(y_intensity)

# Split the dataset into training and testing sets
X_train, X_test, y_emotion_train, y_emotion_test, y_intensity_train, y_intensity_test = train_test_split(
    X, y_emotion, y_intensity, test_size=0.2, random_state=42
)

# Tokenize and pad the text data
max_words = 10000
max_len = 100

tokenizer = Tokenizer(num_words=max_words, oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)

X_train_seq = pad_sequences(tokenizer.texts_to_sequences(X_train), maxlen=max_len)
X_test_seq = pad_sequences(tokenizer.texts_to_sequences(X_test), maxlen=max_len)

# Assuming the number of classes for emotion and intensity
num_emotion_classes = len(label_encoder_emotion.classes_)
num_intensity_classes = len(label_encoder_intensity.classes_)

# Build the emotion prediction model
embedding_dim = 100
lstm_units = 64

model_emotion = Sequential()
model_emotion.add(Embedding(max_words, embedding_dim, input_length=max_len))
model_emotion.add(LSTM(lstm_units))
model_emotion.add(Dropout(0.5))
model_emotion.add(Dense(64, activation='relu'))
model_emotion.add(Dense(num_emotion_classes, activation='softmax'))  # Emotion classification

# Compile the emotion prediction model
model_emotion.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the emotion prediction model
model_emotion.fit(X_train_seq, y_emotion_train, epochs=10, batch_size=32, validation_data=(X_test_seq, y_emotion_test))

# Build the intensity prediction model
model_intensity = Sequential()
model_intensity.add(Embedding(max_words, embedding_dim, input_length=max_len))
model_intensity.add(LSTM(lstm_units))
model_intensity.add(Dropout(0.5))
model_intensity.add(Dense(64, activation='relu'))
model_intensity.add(Dense(num_intensity_classes, activation='softmax'))  # Intensity classification

# Compile the intensity prediction model
model_intensity.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the intensity prediction model
model_intensity.fit(X_train_seq, y_intensity_train, epochs=50, batch_size=32, validation_data=(X_test_seq, y_intensity_test))

# Evaluate the emotion prediction model on the test set
emotion_scores = model_emotion.evaluate(X_test_seq, y_emotion_test)
print(f"Emotion Prediction - Test Accuracy: {emotion_scores[1]*100:.2f}%")

# Evaluate the intensity prediction model on the test set
intensity_scores = model_intensity.evaluate(X_test_seq, y_intensity_test)
print(f"Intensity Prediction - Test Accuracy: {intensity_scores[1]*100:.2f}%")

# Example text data
example_texts = ["Is that really all you can offer for those who sacrifice daily to keep you safe...?",

                 "I'm absolutely in love with Laurie Hernandez, she's so adorable and is always so cheerful!"]

# Tokenize and pad the example text data
example_sequences = pad_sequences(tokenizer.texts_to_sequences(example_texts), maxlen=max_len)

# Make predictions for emotion
example_emotion_predictions = model_emotion.predict(example_sequences)
decoded_example_emotion_predictions = label_encoder_emotion.inverse_transform(np.argmax(example_emotion_predictions, axis=1))

# Make predictions for intensity
example_intensity_predictions = model_intensity.predict(example_sequences)
decoded_example_intensity_predictions = label_encoder_intensity.inverse_transform(np.argmax(example_intensity_predictions, axis=1))

# Print the example predictions
for i in range(len(example_texts)):
    print(f"Text: {example_texts[i]}")
    print(f"Predicted Emotion: {decoded_example_emotion_predictions[i]}")
    print(f"Predicted Intensity: {decoded_example_intensity_predictions[i]}")
    print("\n")

# Example text data
example_texts = ["Is that really all you can offer for those who sacrifice daily to keep you safe...?",

                 "I'm absolutely in love with Laurie Hernandez, she's so adorable and is always so cheerful!"]

# Tokenize and pad the example text data
example_sequences = pad_sequences(tokenizer.texts_to_sequences(example_texts), maxlen=max_len)

# Make predictions for emotion
example_emotion_predictions = model_emotion.predict(example_sequences)
decoded_example_emotion_predictions = label_encoder_emotion.inverse_transform(np.argmax(example_emotion_predictions, axis=1))

# Make predictions for intensity
example_intensity_predictions = model_intensity.predict(example_sequences)
decoded_example_intensity_predictions = label_encoder_intensity.inverse_transform(np.argmax(example_intensity_predictions, axis=1))

# Print the example predictions
for i in range(len(example_texts)):
    print(f"Text: {example_texts[i]}")
    print(f"Predicted Emotion: {decoded_example_emotion_predictions[i]}")
    print(f"Predicted Intensity: {decoded_example_intensity_predictions[i]}")
    print("\n")

