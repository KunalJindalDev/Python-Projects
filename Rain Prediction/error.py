import schedule 
import smtplib 
import requests 
from bs4 import BeautifulSoup 


def umbrellaReminder(): 
    city = "Delhi"
    
    # Creating URL and requests instance 
    url = "https://www.google.com/search?q=" + "weather" + city 
    html = requests.get(url).content 
    
    # Getting raw data 
    soup = BeautifulSoup(html, 'html.parser') 
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
    
    # Formatting data 
    sky = time_sky.split('\n')[1] 

    if sky in ["Rainy", "Rain And Snow", "Showers", "Haze", "Cloudy"]: 
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587) 
        
        # Start TLS for security 
        smtp_object.starttls() 
        
        # Authentication 
        smtp_object.login("cisfun67@gmail.com", "devil2002") 
        subject = "Umbrella Reminder"
        body = f"""Take an umbrella before leaving the house.\ 
        Weather condition for today is {sky} and temperature is\ 
        {temperature} in {city}.""" 
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode('utf-8') 
        
        # Sending the mail 
        smtp_object.sendmail("cisfun67@gmail.com", "cppcoder40@gmail.com", msg) 
        
        # Terminating the session 
        smtp_object.quit() 
        print("Email Sent!") 

# Schedule the reminder for 6:00 AM every day
schedule.every().day.at("16:20").do(umbrellaReminder) 

while True: 
    schedule.run_pending() 
