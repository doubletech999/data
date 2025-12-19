# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Dataset
df = pd.read_csv("reviews.csv")

# 3. Data Cleaning
df.dropna(inplace=True)
df["review"] = df["review"].str.lower()

# 4. Data Wrangling
df["review_length"] = df["review"].apply(len)

# 5. EDA
print(df["sentiment"].value_counts())

# 6. Correlation
sentiment_map = {"negative": 0, "neutral": 1, "positive": 2}
df["sentiment_num"] = df["sentiment"].map(sentiment_map)
print(df["review_length"].corr(df["sentiment_num"]))

# 7. Visualization
df["sentiment"].value_counts().plot(kind="bar")
plt.show()

# 8. Conclusion
# Most reviews are positive and longer than negative ones
