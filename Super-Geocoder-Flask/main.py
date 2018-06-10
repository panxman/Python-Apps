from flask import Flask, render_template, request
from werkzeug import secure_filename
import pandas
import utils


app = Flask(__name__)


# Set the Website
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global up_file
    if request.method == 'POST':
        try:
            up_file = request.files["file"]  # Get the uploaded file
            filename = secure_filename("up-"+up_file.filename)

            df = pandas.read_csv(up_file)
            # Check if file has Address ----------------
            if (('Address' in df.columns) or ('address') in df.columns):
                df = utils.updateDF(df)
                # Save new DataFrame as CSV file
                df.to_csv(filename)
                # DataFrame to HTML Table
                table = df.to_html()
                return render_template("index.html", text=table)
            # End Check --------------------------------
        except:  # noqa: E722
            return render_template("index.html", text="No file selected!")
    return render_template("index.html", text="No Address column found!")


if __name__ == "__main__":
    app.debug = True
    app.run()
