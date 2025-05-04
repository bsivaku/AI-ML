import numpy as np


a = np.array([1, 2, 3, 4, 5])

print(a)

print("Mean: ", np.mean(a))
print("Median: ", np.median(a))
print("Standard Deviation: ", np.std(a))
print("Variance: ", np.var(a))
print("Sum: ", np.sum(a))
print("Product: ", np.prod(a))
print("Max: ", np.max(a))
print("Min: ", np.min(a))

import pandas as pd

data = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data)

print(df)

print("Average Age: ", df["Age"].mean())
print("Median Age: ", df["Age"].median())
print("Standard Deviation of Age: ", df["Age"].std())
print("Variance of Age: ", df["Age"].var())

from scipy import stats

#Generate a random sample from a normal distribution
# sample = np.random.normal(loc=0, scale=1, size=1000)

# print("Mean: ", sample)


# Data Visualization

import matplotlib.pyplot as plt

data ={
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math": [85, 90, 78, 92, 88],
    "Science": [88, 95, 80, 94, 92],
    "English": [90, 85, 92, 88, 95],
    "Gender": ["Female", "Male", "Male", "Male", "Female"]
}

df2 = pd.DataFrame(data)

print(df2)

# plt.figure(figsize=(10, 6))
# plt.bar(df2["Student"], df2["Math"], color="blue", label="Math")
# plt.bar(df2["Student"], df2["Science"], color="green", label="Science")
# plt.bar(df2["Student"], df2["English"], color="red", label="English")
# plt.legend()
# plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df2["Student"], df2["Math"], color="blue", label="Math")
plt.plot(df2["Student"], df2["Science"], color="green", label="Science")
plt.plot(df2["Student"], df2["English"], color="red", label="English")
plt.legend()
plt.show()