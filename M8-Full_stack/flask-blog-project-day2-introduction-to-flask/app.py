from flask import Flask,render_template


## create instance
app = Flask(__name__)

@app.route("/") ## <-- decorator
def index():
    ## get blogs from database
    blogs = [{'title':'Blog 1','content':'This is the first blog'},
             {'title':'Blog 2','content':'This is the second blog'},{'title':'Blog 2','content':'This is the second blog'},{'title':'Blog 2','content':'This is the second blog'},{'title':'Blog 2','content':'This is the second blog'}]
    return render_template("home.html",blogs=blogs)


@app.route("/about") ## <-- decorator
def about():
    return render_template("about.html")






if __name__ == "__main__":
    app.run(debug=True)