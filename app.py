from flask import Flask 
from flask import request 
from flask import redirect
from flask import render_template
from flask import Flask, make_response, request,Response
from flask import session
from flask_mail import Mail
from flask_mail import Message
from datetime import datetime, timedelta
from collections import Counter
import random
import smtplib
import time
import json
from flask import*
from bson.objectid import ObjectId
import pymongo
import os
import mailtrap as mt
from flask.views import MethodView
from flask import jsonify
from flask_jwt_extended import JWTManager
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
import bson.binary
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pathlib
from gridfs import *



app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)

##點我
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

##結果
@app.route("/go")
def go():
    tf = request.args.get("tf")
    return render_template("go.html",tf=tf)



##寄信通知
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hiapples900@gmail.com'
app.config['MAIL_PASSWORD'] = 'bzqzrllmagevgmbc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/send",methods=["POST"])
def send():
    tf=request.form["tf"]
    msg = Message('出門通知', sender = "abc", recipients = ["jhank4321@gmail.com"])
    msg.html = render_template("mail.html",tf=tf)
    msg.body =  msg.html
    mail.send(msg)
    print(tf)
    return redirect(url_for('go', tf=tf))
if __name__ == '__main__':
    app.run(port=3000)
