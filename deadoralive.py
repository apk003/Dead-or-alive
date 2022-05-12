import pandas as pd
from sklearn.linear_model import LogisticRegression

celebrities = pd.read_csv("E:\celebrities.csv")
X = celebrities[["gender", "age", "height", "weight", "occupation", "net_worth"]].values
y = celebrities["alive"].values


# Gender: 1 = male, 2 = female, 3 = other

# Occupations: 0 = actor, 1 = singer/musician, 2 = author/writer, 3 = director,
# 4 = influencer/content creator, 5 = athlete, 6 = other
# Occupations are based off of what someone MAINLY does as a job

print(X)
print(y)

model = LogisticRegression()
model.fit(X, y)
print(model.coef_, model.intercept_)


net_worth = 0
inv = "invalid\n"

while True:
    gender = int(input("\ngender? 1-3\n"))
    if gender < 1 or gender > 3:
        print(inv)
        continue

    age = int(input("\nage?\n"))
    height = int(input("\nheight in cm?\n"))
    weight = int(input("\nweight in kg?\n"))

while net_worth = 0:
    occupation = int(input("\noccupation? 0-6\n"))
    if occupation < 0 or occupation > 6:
        print(inv)
        continue
    net_worth = int(input("\nnet worth?\n"))


test_X = [[gender, age, height, weight, occupation, net_worth]]
print("\n\n" + str(model.predict(test_X)))
