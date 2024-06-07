import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item ratings data
ratings_data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Item1': [4, 5, 0, 3],
    'Item2': [0, 3, 4, 0],
    'Item3': [5, 0, 3, 4],
    'Item4': [3, 0, 0, 5]
}

# Convert data to DataFrame
ratings_df = pd.DataFrame(ratings_data)

# Calculate similarity matrix
similarity_matrix = cosine_similarity(ratings_df.drop('User', axis=1))

# Function to get top-N recommendations for a user
def get_recommendations(user, top_n=2):
    user_index = ratings_df[ratings_df['User'] == user].index[0]
    user_similarities = similarity_matrix[user_index]
    similar_users_indices = user_similarities.argsort()[::-1][1:]  # Exclude the user itself
    recommendations = []
    for item in ratings_df.columns[1:]:
        if ratings_df.at[user_index, item] == 0:  # Item not already rated by the user
            rating_sum = 0
            weight_sum = 0
            for sim_user_index in similar_users_indices:
                rating_sum += ratings_df.at[sim_user_index, item] * user_similarities[sim_user_index]
                weight_sum += user_similarities[sim_user_index]
            if weight_sum > 0:
                recommendations.append((item, rating_sum / weight_sum))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]

# Example usage
user = 'User1'
top_recommendations = get_recommendations(user)
print(f"Top recommendations for {user}: {top_recommendations}")
