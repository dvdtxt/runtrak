from flask import *
from graficos import *
from sql import *

app = Flask(__name__)

init_db()

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

@app.route('/report')
def report():
    records = get_all_data_desc()
    total_distances,total_minutes = total_sums(records)
    return render_template('report.html', minutes=round(total_minutes,2), distances=round(total_distances,2))

@app.route('/distance_over_time.png')
def dist_over_time_png():
    records = get_all_data_asc()
    img = distance_over_time(records)
    return send_file(img, mimetype='image/png')

@app.route('/duration_over_time.png')
def dura_over_time_png():
    records = get_all_data_asc()
    img = duration_over_time(records)
    return send_file(img, mimetype='image/png')

init_db()
