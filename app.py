from flask import *
from basic_func import *
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        distance = request.form['distance']
        time = request.form['time']
        date = request.form['date']
        insert_data(distance=distance,time=time,date=date)
        return redirect(url_for('input'))

    return render_template('input.html')

@app.route('/table')
def table():
    records = get_all_data_desc()
    return render_template('table.html', records=records)

@app.route('/delete_last_row', methods=['POST'])
def delete_last_row():
    delete_last()
    return jsonify(success=True)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        records = get_data_by_date_range(start_date, end_date)
    else:
        # Calcular la fecha de inicio del último mes
        today = datetime.date.today()
        last_month_start = today.replace(day=1) - datetime.timedelta(days=1)
        last_month_start = last_month_start.replace(day=1)

        # Obtener los datos del último mes
        records = get_data_by_date_range(last_month_start, today)
        start_date = last_month_start
        end_date = today
    
    total_distances, total_minutes = total_sums(records)
    avg_speed = calculate_average_speed(total_distances, total_minutes)
    total_workouts = len(records)

    # Prepare data for Chart.js
    labels = [row[3] for row in records]    
    distances = [row[1] for row in records]
    minutes = [row[2] for row in records]

    return render_template('report.html',
                           labels=json.dumps(labels),
                           distances=json.dumps(distances),
                           minutes=json.dumps(minutes),
                           avg_speed=avg_speed,
                           total_distance=total_distances,
                           total_time=total_minutes,
                           total_workouts=total_workouts,
                           start_date=start_date, 
                           end_date=end_date)

init_db()
