from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pca')
def pca():
    return render_template('pca.html')

@app.route('/bert')
def bert():
    return render_template('bert.html')

@app.route('/svm')
def svm():
    return render_template('svm.html')

if __name__ == '__main__':
    app.run(debug=True)
