from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template("index.html" )

@app.route("/result",methods=["POST"])
def result():
    name = request.form["name"]
    location = request.form["location"]
    stack = request.form["stack"]
    comment = request.form["comment"]

    return render_template("index2.html",name= name, location = location, stack=stack, comment=comment)

@app.route("/submitted", methods=["POST"])
def submitinfo():
    
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)
