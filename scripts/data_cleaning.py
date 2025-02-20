import pandas as pd
import numpy as np


user_activity_df = pd.read_csv('input_datasets/user_activity_data.csv')
moderator_performance_df = pd.read_csv('input_datasets/moderator_performance_data.csv')
recommendation_df = pd.read_csv('input_datasets/recommendation_data.csv')


print("User Activity Data:")
print(user_activity_df.head())
print("\nModerator Performance Data:")
print(moderator_performance_df.head())
print("\nRecommendation Data:")
print(recommendation_df.head())

# Handle Missing Values
user_activity_df.ffill(inplace=True)  
moderator_performance_df.ffill(inplace=True)  
recommendation_df.ffill(inplace=True)  

# Convert 'timestamp' to datetime in user_activity_df
if 'timestamp' in user_activity_df.columns:
    user_activity_df['timestamp'] = pd.to_datetime(user_activity_df['timestamp'], errors='coerce')
else:
    print("'timestamp' column not found in user_activity_df.")

# Handle 'avg_response_time' outliers in moderator_performance_df
moderator_performance_df = moderator_performance_df[moderator_performance_df['avg_response_time'] < 100]

# Ensure all columns have correct data types
user_activity_df['session_length'] = pd.to_numeric(user_activity_df['session_length'], errors='coerce')
user_activity_df['messages_sent'] = pd.to_numeric(user_activity_df['messages_sent'], errors='coerce')
user_activity_df['feedback_rating'] = pd.to_numeric(user_activity_df['feedback_rating'], errors='coerce')
user_activity_df['resources_clicked'] = pd.to_numeric(user_activity_df['resources_clicked'], errors='coerce')

moderator_performance_df['chat_sessions_moderated'] = pd.to_numeric(moderator_performance_df['chat_sessions_moderated'], errors='coerce')
moderator_performance_df['user_satisfaction_score'] = pd.to_numeric(moderator_performance_df['user_satisfaction_score'], errors='coerce')

recommendation_df['click_through_rate'] = pd.to_numeric(recommendation_df['click_through_rate'], errors='coerce')
recommendation_df['feedback_score'] = pd.to_numeric(recommendation_df['feedback_score'], errors='coerce')


user_activity_df.drop_duplicates(inplace=True)
moderator_performance_df.drop_duplicates(inplace=True)
recommendation_df.drop_duplicates(inplace=True)

# Save the cleaned datasets to output directory
user_activity_df.to_csv('output/cleaned_data/user_activity_cleaned.csv', index=False)
moderator_performance_df.to_csv('output/cleaned_data/moderator_performance_cleaned.csv', index=False)
recommendation_df.to_csv('output/cleaned_data/recommendation_cleaned.csv', index=False)


print("\nCleaned User Activity Data:")
print(user_activity_df.head())
print("\nCleaned Moderator Performance Data:")
print(moderator_performance_df.head())
print("\nCleaned Recommendation Data:")
print(recommendation_df.head())

# Optionally, generate some basic statistics for the cleaned data
print("\nBasic Statistics for Cleaned User Activity Data:")
print(user_activity_df.describe())

print("\nBasic Statistics for Cleaned Moderator Performance Data:")
print(moderator_performance_df.describe())

print("\nBasic Statistics for Cleaned Recommendation Data:")
print(recommendation_df.describe())
