from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/pre', methods=['POST'])
def pred():
    USD = request.form['USD']
    pred = int(USD)*91.91
    return str(pred)

if __name__=='__main__':
    app.run(host='0.0.0.0', port= 2122, debug=True)