from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, SIva how are you?!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name) #<-- passing variable to page

if __name__ == "__main__":
    app.run(debug=True) 