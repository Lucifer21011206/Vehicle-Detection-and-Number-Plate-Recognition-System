from flask import Flask, render_template
import threading
from detection import update_vehicle_data
from vehicle_data import vehicle_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', vehicle_data=vehicle_data)


if __name__ == "__main__":
    threading.Thread(target=update_vehicle_data).start()
    app.run(debug=True)
