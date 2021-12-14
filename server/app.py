from flask import Flask, send_from_directory, make_response, send_file
import shutil
import os

UPLOAD_FOLDER = "/home/uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 3 * 1000 * 1000


@app.route("/")
def index():
    path = UPLOAD_FOLDER
    list_of_files = {}

    for filename in os.listdir(path):
        list_of_files[filename] = UPLOAD_FOLDER + filename

    res = """
    <!doctype html>
    <title>All Files</title>
    <body>
    <h1>All Files</h1>
    <ul>
    """
    for filename in list_of_files:
        res += "<li>{}</li>".format(filename)
    res += "</ul></body></html>"

    return res

@app.route("/test")
def test():
    return "Hello, World!"

@app.route("/view/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route("/download", methods=["GET", "POST"])
def download():
    FILENAME = "./tmp/uploads"
    shutil.make_archive(FILENAME, "zip", UPLOAD_FOLDER)
    try:
        return send_file(
            FILENAME + ".zip", as_attachment=True, download_name="uploads.zip"
        )
    except Exception as e:
        print(e)
        return make_response("Error", 500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
