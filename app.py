from flask import Flask,render_template,request
from src.predict import predict_email
from database.history import save_prediction
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    email = request.form["email"]

    prediction, confidence= predict_email(email)

    print("Email:", email)
    print("Prediction:", prediction)
    print("Confidence:", confidence)
    save_prediction(email, prediction, confidence)
    prediction_text = "Ham" if prediction == 0 else "Spam"
    
    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        email=email
    )


if __name__ == "__main__":
    app.run(debug=True)