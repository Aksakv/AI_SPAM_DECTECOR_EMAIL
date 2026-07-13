import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_csv("spamm.csv",
    sep="\t",
    names=["label", "message"])

data = data.drop_duplicates()

data = data.dropna(subset=["message", "label"])
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

X = data["message"]
y = data["label"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))

with open("spam_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)
    
print(data[data["label"] == 0].head(5))
print(data[data["label"] == 1].head(5))