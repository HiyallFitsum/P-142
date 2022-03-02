import pandas as pd

df = pd.read_csv("shared_articles.csv")
df.head()
total_views = df2[(df2["contentId"] == df1["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
total_like = df2[(df2["contentId"] == df1["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
total_bookmark = df2[(df2["contentId"] == df1["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
total_follow = df2[(df2["contentId"] == df1["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
total_comments = df2[(df2["contentId"] == df1["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]

 = .sort_values('', ascending=False)
[[]].head(10)