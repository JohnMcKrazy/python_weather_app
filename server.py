from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
app = Flask(__name__)

@app.route("/error")
def show_error():
    return render_template("error.html")
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/weather')
def get_weather():
    try:
        city = request.args.get('city')
        weather_data = get_current_weather(city.strip())
        return render_template(
            "weather.html",
            
            city=weather_data["name"],
            country=weather_data["sys"]["country"],
            weather_description=weather_data["weather"][0]['description'].title(),
            wind_speed=weather_data["wind"]['speed'],
            wind_angle=weather_data["wind"]['deg'],
            humidity=weather_data["main"]['humidity'],
            pressure=weather_data["main"]['pressure'],
            deg=weather_data["main"]['temp'], 
            deg_max=weather_data["main"]['temp_max'], 
            deg_min=weather_data["main"]['temp_min'],
            lat=weather_data["coord"]['lat'],
            lon=weather_data["coord"]['lon']
        )
    except KeyError:
          print("That's incorrect, please introduce a correct city")
          return show_error()


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)