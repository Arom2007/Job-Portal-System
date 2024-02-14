def send_registration_email(user):
    subject = "Sign Up Success"
    message = f"Congratulations {user.first_name}. You have successfully created an account."
    user.email_user(subject=subject, message=message, from_email="noreply@gmail.com")
