import pyttsx3
import speech_recognition as sr
import eel
import time
import os
import requests

# Weather API Configuration
OPENWEATHER_API_KEY = "your_api_key_here"  # Replace with your actual API key

def get_weather(city):
    """Get weather information for a city using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={OPENWEATHER_API_KEY}&q={city}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data.get("cod") != 404:
            main = data["main"]
            temperature = main["temp"]
            humidity = main["humidity"]
            weather_desc = data["weather"][0]["description"]
            
            weather_report = (f"The temperature in {city} is {temperature:.1f}°C with {weather_desc}. "
                             f"The humidity is {humidity}%.")
            return weather_report
        else:
            return "City not found. Please try again."
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return "Sorry, I couldn't fetch the weather information."

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(text)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

# def allCommands(message=1):
#     if message == 1:
#         query = takecommand()
#         print(query)
#         eel.senderText(query)
#     else:
#         query = message
#         eel.senderText(query)

#     try:
#         if "open" in query:
#             from engine.features import openCommand
#             openCommand(query)
        
#         elif "on youtube" in query or "play" in query:
#             from engine.features import PlayYoutube
#             PlayYoutube(query)
        
#         elif "send message" in query or "phone call" in query or "video call" in query:
#             from engine.features import findContact, whatsApp, makeCall, sendMessage
#             contact_no, name = findContact(query)
#             if contact_no != 0:
#                 speak("Which mode you want to use: whatsapp or mobile?")
#                 preferance = takecommand()
#                 print(preferance)

#                 if "mobile" in preferance:
#                     if "send message" in query or "send sms" in query: 
#                         speak("What message to send?")
#                         message = takecommand()
#                         sendMessage(message, contact_no, name)
#                     elif "phone call" in query:
#                         makeCall(name, contact_no)
#                     else:
#                         speak("Please try again.")
#                 elif "whatsapp" in preferance:
#                     message = ""
#                     if "send message" in query:
#                         message = 'message'
#                         speak("What message to send?")
#                         query = takecommand()
#                     elif "phone call" in query:
#                         message = 'call'
#                     else:
#                         message = 'video call'

#                     whatsApp(contact_no, query, message, name)

#         # If it's neither an "open" nor "play" command, fallback to searching Google
#         else:
#             speak(f"Searching for {query} on Google.")
#             from engine.features import openCommand
#             openCommand(query)  # Assuming this will handle Google search

#     except Exception as e:
#         print("Error:", e)
#         speak("Something went wrong. Please try again.")

#     eel.ShowHood()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         eel.DisplayMessage('Listening...')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
        
#         audio = r.listen(source, 10, 6)

#     try:
#         print('Recognizing...')
#         eel.DisplayMessage('Recognizing...')
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}")
#         eel.DisplayMessage(query)
#         time.sleep(2)
#     except Exception as e:
#         print("Error in recognition:", e)
#         return ""
    
#     return query.lower()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        
        elif "find" in query:
            from engine.features import openCommand
            openCommand(query)
        
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "what's the time" in query or "tell me the time" or "the time" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "weather" in query:
            # Handle weather queries
            if "weather in" in query:
                city = query.split("weather in")[-1].strip()
            elif "weather of" in query:
                city = query.split("weather of")[-1].strip()
            elif "weather for" in query:
                city = query.split("weather for")[-1].strip()
            else:
                speak("Which city's weather would you like to know?")
                city = takecommand()
            
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
            else:
                speak("Sorry, I didn't catch the city name. Please try again.")
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)

        else:
            # speak(f"Searching for {query} on Google.")
            from engine.features import openCommand
            openCommand(query)  # Assuming this will handle Google search

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong. Please try again.")

    eel.ShowHood()