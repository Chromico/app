from flask import Flask
import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged==False: plugged="Not Plugged In"
else: plugged="Plugged In"

app = Flask(__name__)

@app.route("/")
def main():
	return (percent+'% | '+plugged)
	
if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0", port = 5000)
