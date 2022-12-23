import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

stations = pd.read_csv("temp_data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station_id>/<date>")
def get_station_temp(station_id, date):
    filename = "temp_data/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {
        "station": station_id,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/<station_id>")
def get_station_all_temp(station_id):
    filename = "temp_data/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station_id>/<year>")
def get_station_temp_year(station_id, year):
    filename = "temp_data/TG_STAID" + str(station_id).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
