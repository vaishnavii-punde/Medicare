import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load the dataset
df = pd.read_csv('medicine_suggestions.csv')

# Vectorize symptom text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Symptom(s)'])
y = df['Recommended Medicine']

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open('med_predictor.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("✅ Model and vectorizer saved successfully!")
