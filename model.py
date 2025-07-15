import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
df = pd.read_csv(r'C:\Users\limbu\Laptop_recommendation\data\preprocessed\cleaned_laptop_data.csv')
df.fillna('', inplace=True)

# Combine important features into a single string for vectorization
def combine_features(row):
    return f"{row['Generation']} {row['Core']} {row['Ram_GB']}GB RAM {row['SSD_GB']}GB SSD {row['Graphics']} {row['OS']}"

df['combined_features'] = df.apply(combine_features, axis=1)

# Vectorize combined features
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# Calculate similarity matrix
similarity = cosine_similarity(feature_matrix)

# Function to get all laptop models
def get_laptop_names():
    return df['Model'].tolist()

# Function to get index of laptop by model name
def get_laptop_index(model_name):
    return df[df['Model'] == model_name].index[0]

# Recommend similar laptops given an index
def recommend_laptops_by_index(index, num_recommendations=5):
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in scores[1:num_recommendations+1]]
    return df.iloc[recommended_indices][['Model', 'Price', 'Ram_GB', 'SSD_GB', 'Graphics', 'OS']]
