from reader import read_csv
from statistics import mean

data = read_csv("data.csv")
scores = [int(row["score"]) for row in data]
print(f"Average score: {mean(scores)}")
