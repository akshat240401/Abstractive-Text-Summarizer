# from crypt import methods
# from crypt import methods
# from unittest import result
# from urllib import request
from flask import Flask,render_template,url_for,request
from flask import request as req
import requests


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method=="POST":
        
        API_URL = "https://api-inference.huggingface.co/models/lidiya/bart-large-xsum-samsum"
        headers = {"Authorization": f"Bearer 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"}

        data=req.form["data"]


        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
        })[0]

        return render_template("index.html",result=output["summary_text"])

    else:
        return render_template("index.html")