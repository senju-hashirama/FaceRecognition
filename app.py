import face_recognition as fr
from flask import Flask,Response,redirect,render_template,request,url_for,copy_current_request_context,flash
from werkzeug.utils import secure_filename
import cv2
import os
from os.path import exists

app=Flask(__name__)
app.secret_key = "123qwerrty123"
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["labels"]=[]
ALLOWED_EXTENSIONS = set(['mp4', 'mkv', 'png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/upload_file",methods=["POST"])
def upload_file():
    if "recog_files[]" not in request.files :
        flash("no files selected")
        return redirect("/")

    if "work_files[]" not in request.files :
        flash("no files selected")
        return redirect("/")

    recog_files=request.files.getlist("recog_files[]")
    work_files=request.files.getlist("work_files[]")

    for file in recog_files:
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)

            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))

    file=work_files[0]
    if file and allowed_file(file.filename):
        app.config["wfile_format"]=file.filename[-3:]
        filename=secure_filename("test."+file.filename[-3:])
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))

        return redirect("/recog")
@app.route("/recog")
def recog():

    kface=[]
    labels=[]


    for i in os.listdir("./uploads1"):
        if (("test" not in i)&(i.split(".")[-1] in ['png', 'jpg', 'jpeg'])):
            file=fr.load_image_file("./uploads/{}".format(i))
            kface.append(fr.face_encodings(file)[0])
            labels.append(i.split(".")[0])
        elif(("test" in i)&(i.split(".")[-1] in ["mkv","mp4"])):
            locations=



if __name__=="__main__":
    app.run(debug=True)
