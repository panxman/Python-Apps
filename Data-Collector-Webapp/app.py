from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from send_email import send_email


app = Flask(__name__)
# Change username, password and database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/db_name'  # noqa: E501
db = SQLAlchemy(app)


# Create DataBase Class
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(30), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


# Set the Website
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]  # Get the data from POST method
        height = request.form["height_name"]
        # Check if email is NOT in the DB ----------------
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)  # Create Class object
            db.session.add(data)  # Add the data to database
            db.session.commit()
            # Calculate average height
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
        # End Check ------------------------------------
    return render_template("index.html", text="Email already in Database!")


if __name__ == "__main__":
    app.debug = True
    app.run()
