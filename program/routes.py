from datetime import datetime
from thermometer import Thermometer
from program import app
from flask import render_template


thermo = Thermometer()
timenow = str(datetime.today())

@app.route('/')
@app.route('/index')
def index():
    tp = f"{thermo.get_temp():.2f}"
    tm = datetime.today().strftime("%H:%M:%S %m/%d/%Y")
    return render_template('index.html',time=tm,temp=tp)


@app.route('/temp')
def get_temp():
    return f"{thermo.get_temp():.2f}°F"
