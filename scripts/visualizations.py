import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

merged_df = pd.read_csv('output/cleaned_data/merged_consolidated_data.csv')
moderator_performance_df = pd.read_csv('output/cleaned_data/moderator_performance_cleaned.csv')

sns.set(style="whitegrid")


visualization_dir = 'output/visualizations' 
os.makedirs(visualization_dir, exist_ok=True)

# 1. Plot User Engagement KPIs
user_kpis = {
    'Average Session Length (minutes)': merged_df['session_length'].mean(),
    'Average Messages Sent': merged_df['messages_sent'].mean(),
    'Average Feedback Rating': merged_df['feedback_rating'].mean(),
    'Average Click-Through Rate (CTR)': merged_df['click_through_rate'].mean(),
}

plt.figure(figsize=(8, 5))
plt.bar(user_kpis.keys(), user_kpis.values(), color='skyblue')
plt.title('User Engagement KPIs', fontsize=16)
plt.ylabel('Values', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Save the figure in the visualizations folder
plt.savefig(f'{visualization_dir}/user_engagement_kpis.png')
plt.close()

# 2. Plot Moderator Performance KPIs
moderator_kpis = {
    'Average Chat Sessions Moderated': moderator_performance_df['chat_sessions_moderated'].mean(),
    'Average Response Time (minutes)': moderator_performance_df['avg_response_time'].mean(),
    'Average User Satisfaction Score': moderator_performance_df['user_satisfaction_score'].mean(),
}

plt.figure(figsize=(8, 5))
plt.bar(moderator_kpis.keys(), moderator_kpis.values(), color='lightgreen')
plt.title('Moderator Performance KPIs', fontsize=16)
plt.ylabel('Values', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{visualization_dir}/moderator_performance_kpis.png')
plt.close()

# 3. Plot Correlation Heatmap between session length, messages sent, resources clicked, and feedback rating
correlation_data = merged_df[['session_length', 'messages_sent', 'resources_clicked', 'feedback_rating']]
correlation_matrix = correlation_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of User Engagement Metrics', fontsize=16)
plt.tight_layout()
plt.savefig(f'{visualization_dir}/correlation_heatmap.png')
plt.close()

# 4. Boxplot for Session Length Outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=merged_df['session_length'], color='lightcoral')
plt.title('Session Length Outliers', fontsize=16)
plt.xlabel('Session Length (minutes)', fontsize=12)
plt.tight_layout()
plt.savefig(f'{visualization_dir}/session_length_outliers.png')
plt.close()

# 5. Boxplot for Messages Sent Outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=merged_df['messages_sent'], color='lightblue')
plt.title('Messages Sent Outliers', fontsize=16)
plt.xlabel('Messages Sent', fontsize=12)
plt.tight_layout()
plt.savefig(f'{visualization_dir}/messages_sent_outliers.png')
plt.close()

# 6. Boxplot for Feedback Rating Outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=merged_df['feedback_rating'], color='lightgreen')
plt.title('Feedback Rating Outliers', fontsize=16)
plt.xlabel('Feedback Rating', fontsize=12)
plt.tight_layout()
plt.savefig(f'{visualization_dir}/feedback_rating_outliers.png')
plt.close()

print("Visualizations have been saved to the 'output/visualizations' folder.")
