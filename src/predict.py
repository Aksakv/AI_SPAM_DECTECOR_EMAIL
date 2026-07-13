import pickle

with open("models/spam_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

def predict_email(email):
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)
    confidence = max(model.predict_proba(email_vector)[0]) * 100
    print(type(prediction[0]))
    print(prediction[0])

    return prediction[0], round(confidence, 2)