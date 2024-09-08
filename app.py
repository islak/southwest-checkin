from flask import Flask, request, render_template
from checkin import open_southwest_page  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    confirmation_number = request.form['confirmation_number']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    open_southwest_page(confirmation_number, first_name, last_name)

    return 'Check-in form submitted!'

if __name__ == '__main__':
    app.run(debug=True)
