from flask import Flask, render_template, request
app = Flask("Projectcnc")

@app.route("/home")
def main_page():
    return render_template("project_mainpage.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact_return", methods=["POST"])
def contact_return_():
    form_data=request.form
    print form_data["gender"]
    if form_data["gender"] == "female":
        return "Welcome to the Code and Coffee Family!"
    else:
        return "Sorry, we only accept female members!"

app.run(debug=True)
