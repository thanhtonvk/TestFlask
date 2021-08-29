from flask import Flask, render_template,request

import TaiTrongPrediction

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def Prediction():
    if request.method =="POST":
        f_taitrong = int(request.form["taitrong"])
        predict = TaiTrongPrediction.myfunc(f_taitrong)
        rs = predict
        return render_template("index.html",result = rs)
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
