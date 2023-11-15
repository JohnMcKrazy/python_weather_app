import requests
from dotenv import load_dotenv
import os
import sys
from pprint import pprint

load_dotenv()

def get_current_weather(city="Mexico city"):
    try:
       
        request_url=f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
        #print(request_url)
        weather_data=requests.get(request_url).json()
        #pprint(weather_data)
        return weather_data
      
        
        
    except KeyError:
        print("That's incorrect, please introduce a correct city")
        #return get_current_weather()
    
if __name__ == "__main__":    

    print("\n*** Get current Weather conditions ***\n")
    city = input("\nPlease Enter Your City:\n")
    
    ## CHECK FOR EMPTY CHARTS
    #if not bool(city.strip()):
    #    server.show_error()    
    weather_data = get_current_weather()
    print("\n")
    pprint(weather_data)