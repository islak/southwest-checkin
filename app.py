from flask import Flask, request, render_template
from checkin import open_southwest_page  
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    confirmation_number = request.form['confirmation_number']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    flight_time = request.form['flight_time']

    flight_time_obj = datetime.strptime(flight_time, "%Y-%m-%dT%H:%M")
    checkin_time = flight_time_obj - timedelta(hours=24)
    scheduler.add_job(open_southwest_page, 'date', run_date=checkin_time, args=[confirmation_number, first_name, last_name])

    return 'Check-in scheduled successfully!'

if __name__ == '__main__':
    app.run(debug=True)
