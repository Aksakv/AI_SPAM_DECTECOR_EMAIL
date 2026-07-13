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

    save_prediction(email, prediction, confidence)
    
    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        email=email
    )


if __name__ == "__main__":
    app.run(debug=True)