from src.predict import predict_email

email = input("Enter Email:\n")

result = predict_email(email)

print("Prediction:", result)