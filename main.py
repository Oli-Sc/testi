from flask import Flask

app =  Flask(__name__)

@app.route('/')


def hallo():
    return 'Hallo zusammen wie geths?'

@app.route('/home')

def home():
    return 'Hier ist Home'
if __name__ == '__main__':
    app.run(port=5000, debug=True)
