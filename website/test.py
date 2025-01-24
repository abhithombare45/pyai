my_flask_project/
│-- app.py  (your Flask application)
│-- templates/
    │-- index.html  (your HTML file)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
