from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Email configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "thebeattyler@gmail.com"  # Change this
app.config["MAIL_PASSWORD"] = "Redcar72"  # Change this

mail = Mail(app)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Report Form page
@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Send email
        msg = Message("Bullying Report", sender=email, recipients=["your-email@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        flash("Report submitted successfully!", "success")
        return redirect(url_for("success"))

    return render_template("report.html")

# Success page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

