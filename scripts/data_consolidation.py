import pandas as pd

user_activity_df = pd.read_csv('output/cleaned_data/user_activity_cleaned.csv')
moderator_performance_df = pd.read_csv('output/cleaned_data/moderator_performance_cleaned.csv')
recommendation_df = pd.read_csv('output/cleaned_data/recommendation_cleaned.csv')

print("\nCleaned User Activity Data:")
print(user_activity_df.head())

print("\nCleaned Moderator Performance Data:")
print(moderator_performance_df.head())

print("\nCleaned Recommendation Data:")
print(recommendation_df.head())

merged_df = pd.merge(user_activity_df, recommendation_df, on='user_id', how='left')


merged_df.ffill(inplace=True)

# calculating average feedback score per user session
merged_df['avg_feedback_score_per_session'] = merged_df['feedback_rating'] / merged_df['session_length']

# calculating the total number of resources clicked per user session
merged_df['total_resources_clicked'] = merged_df.groupby('user_id')['resources_clicked'].transform('sum')

merged_df.to_csv('output/cleaned_data/merged_consolidated_data.csv', index=False)

print("\nConsolidated Data:")
print(merged_df.head())

print("\nBasic Statistics for Consolidated Data:")
print(merged_df.describe())
