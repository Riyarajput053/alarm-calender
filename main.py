from datetime import datetime, timedelta
import winsound
import requests
import time
import base64

now = datetime.now()
day, month, year = now.day, now.month, now.year
hour, minute = now.hour, now.minute 

user_id = "639296"
api_key = "09fa20aa5199f4a24e00271a07801138be28e211"
language = "en" 

def get_hindu_calender():
    api = "basic_panchang"
    url = f"https://json.astrologyapi.com/v1/{api}"

    data = {
        # "day": day,
        # "month": month,
        # "year": year,
        # "hour": hour,
        # "min": minute,
        "day": 8,
        "month": 4,
        "year": 2025,
        "hour": 16,
        "min": 45,
        "lat": 19.132,
        "lon": 72.342,
        "tzone": 5.5
    }

    auth_string = f"{user_id}:{api_key}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_encoded}",
        "Content-Type": "application/json",
        "Accept-Language": language
    }

    response = requests.post(url, json=data, headers=headers)

    try:
        return response.json()
    except:
        return {}

calender_data = get_hindu_calender()
print("Calendar Data:", calender_data)

def ekam(data):
    tithi_name = data.get("tithi", "").lower()  
    return "ekadashi" in tithi_name  

print("Is today Ekadashi?", ekam(calender_data))


def wait_until_8_am():
    now = datetime.now()
    # target_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
    target_time = now + timedelta(seconds=5)

    if now > target_time:
        target_time += datetime.timedelta(days=1)  

    wait_seconds = (target_time - now).total_seconds()
    print(f"Waiting for {wait_seconds // 3600} hours and {wait_seconds % 3600 // 60} minutes until 8 AM...")
    
    time.sleep(wait_seconds)  
    
def play_alarm():
    print("It's Ekadashi.")
    for _ in range(5): 
        winsound.Beep(500, 800)   
        time.sleep(1) 
        
if __name__ == "__main__":
    
    calendar_data = get_hindu_calender()

    if ekam(calendar_data): 
        wait_until_8_am()  
        play_alarm() 
    else:
        print("today is not ekadashi")
