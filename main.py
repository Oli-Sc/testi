from flask import Flask, render_template, request, url_for, redirect

app =  Flask(__name__)

@app.route('/', methods=["GET","POST"])


def hallo():
    if request.method == "POST":
        number1 = request.form["ersteZahl"]
        number2 = request.form["zweiteZahl"]
        return number2 
    else:
        return render_template('index.html')

@app.route('/home')

def home():
    return 'Hier ist Home'
if __name__ == '__main__':
    app.run(port=5000, debug=True)