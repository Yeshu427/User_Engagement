import pandas as pd

merged_df = pd.read_csv('output/cleaned_data/merged_consolidated_data.csv')
moderator_performance_df = pd.read_csv('output/cleaned_data/moderator_performance_cleaned.csv')
recommendation_df = pd.read_csv('output/cleaned_data/recommendation_cleaned.csv')

print("\nMerged Data Sample:")
print(merged_df.head())

print("\nModerator Performance Data Sample:")
print(moderator_performance_df.head())

print("\nMissing Values in Merged Data:")
print(merged_df.isnull().sum())

print("\nMissing Values in Moderator Data:")
print(moderator_performance_df.isnull().sum())

merged_df.ffill(inplace=True)  
moderator_performance_df.ffill(inplace=True)  

# User Engagement KPIs
avg_session_length = merged_df['session_length'].mean()
avg_messages_sent = merged_df['messages_sent'].mean()
avg_feedback_rating = merged_df['feedback_rating'].mean()
avg_click_through_rate = merged_df['click_through_rate'].mean()

print("\nUser Engagement KPIs:")
print(f"Average Session Length: {avg_session_length} minutes")
print(f"Average Messages Sent: {avg_messages_sent} messages")
print(f"Average Feedback Rating: {avg_feedback_rating}")
print(f"Average Click-Through Rate (CTR): {avg_click_through_rate}")

# Moderator Performance KPIs
avg_chat_sessions_moderated = moderator_performance_df['chat_sessions_moderated'].mean()
avg_response_time = moderator_performance_df['avg_response_time'].mean()
avg_user_satisfaction_score = moderator_performance_df['user_satisfaction_score'].mean()

print("\nModerator Performance KPIs:")
print(f"Average Chat Sessions Moderated: {avg_chat_sessions_moderated} sessions")
print(f"Average Response Time: {avg_response_time} minutes")
print(f"Average User Satisfaction Score: {avg_user_satisfaction_score}")

# Recommendation Effectiveness KPIs
avg_feedback_score = merged_df['feedback_score'].mean()

print("\nRecommendation Effectiveness KPIs:")
print(f"Average Feedback Score for Recommendations: {avg_feedback_score}")

# Exploring trends using correlation coefficients
session_feedback_corr = merged_df[['session_length', 'feedback_rating']].corr().iloc[0, 1]
print(f"\nCorrelation between Session Length and Feedback Rating: {session_feedback_corr}")

messages_feedback_corr = merged_df[['messages_sent', 'feedback_rating']].corr().iloc[0, 1]
print(f"Correlation between Messages Sent and Feedback Rating: {messages_feedback_corr}")

resources_feedback_corr = merged_df[['resources_clicked', 'feedback_rating']].corr().iloc[0, 1]
print(f"Correlation between Resources Clicked and Feedback Rating: {resources_feedback_corr}")

# Identifying anomalies in Session Length (outliers)
session_length_outliers = merged_df[merged_df['session_length'] > merged_df['session_length'].quantile(0.95)]
print(f"\nTop 10 Sessions with Long Session Lengths (Outliers):")
print(session_length_outliers[['user_id', 'session_length']].head(15))  

# Identifying anomalies in Messages Sent
messages_sent_outliers = merged_df[merged_df['messages_sent'] > merged_df['messages_sent'].quantile(0.95)]
print(f"\nTop 10 Sessions with High Messages Sent (Outliers):")
print(messages_sent_outliers[['user_id', 'messages_sent']].head(15))  

# Identifying low Feedback Ratings
low_feedback_sessions = merged_df[merged_df['feedback_rating'] < 2]
print(f"\nTop 10 Sessions with Low Feedback Ratings:")
print(low_feedback_sessions[['user_id', 'feedback_rating']].head(15))  

# Identifying moderators with low user satisfaction scores
low_satisfaction_moderators = moderator_performance_df[moderator_performance_df['user_satisfaction_score'] < 3]
print(f"\nTop 10 Moderators with Low User Satisfaction Scores:")
print(low_satisfaction_moderators[['moderator_id', 'user_satisfaction_score']].head(15))  


