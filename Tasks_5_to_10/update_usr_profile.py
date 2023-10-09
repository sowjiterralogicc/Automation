from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)       #This line creates an instance of the Flask class and assigns it to the variable app.
# The __name__ variable is a special Python variable that holds the name of the current module.

# Sample user profile
user_profile = {
    "name": "sowji",
    "email": "sowji9937@gmail.com",
    "address": "bangalore"
}
@app.route("/", methods=["GET", "POST"])
def update_profile():
    if request.method == "POST":
        # Get the new name and email from the form
        new_name = request.form["new_name"]
        new_email = request.form["new_email"]
        new_address = request.form["new_address"]

        # Update the user profile dictionary with the new info
        user_profile["name"] = new_name
        user_profile["email"] = new_email
        user_profile["address"] = new_address

    return render_template("update_profile.html", user_profile=user_profile)

if __name__ == "__main__":
    app.run(debug=True)
