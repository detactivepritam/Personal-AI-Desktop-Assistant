"""
Engine Features Module with Weather Support
==========================================
This module contains core features for the Personal AI Desktop Assistant including weather.
"""

import logging
import webbrowser
import subprocess
import os
from typing import Optional

logger = logging.getLogger(__name__)

def playAssistantSound():
    """Play assistant startup sound."""
    logger.info("🔊 Playing assistant sound")
    print("🎵 Assistant sound playing...")

def hotword():
    """Hotword detection functionality."""
    logger.info("👂 Hotword detection started")
    print("👂 Listening for hotword...")
    
    # Basic hotword detection simulation
    import time
    while True:
        time.sleep(1)
        # This would normally listen for "Hey Jarvis" or similar
        # For now, it just runs continuously

def openCommand(query: str):
    """Handle open/search commands including weather."""
    query = query.lower()
    
    if "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        logger.info("🎥 Opened YouTube")
    elif "google" in query:
        search_term = query.replace("google", "").replace("search", "").strip()
        if search_term:
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            webbrowser.open("https://www.google.com")
        logger.info(f"🔍 Searched Google for: {search_term}")
    elif "time" in query:
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        from command import speak
        speak(f"The current time is {current_time}")
    elif "weather" in query:
        # Extract city name from query
        city = ""
        if "weather in" in query:
            city = query.split("weather in")[-1].strip()
        elif "weather of" in query:
            city = query.split("weather of")[-1].strip()
        elif "weather for" in query:
            city = query.split("weather for")[-1].strip()
        
        if city:
            from command import get_weather, speak
            weather_info = get_weather(city)
            speak(weather_info)
        else:
            from command import speak
            speak("Which city's weather would you like to know?")
    else:
        # Default to Google search
        webbrowser.open(f"https://www.google.com/search?q={query}")
        logger.info(f"🔍 Searched for: {query}")

def PlayYoutube(query: str):
    """Play content on YouTube."""
    search_term = query.replace("play", "").replace("youtube", "").strip()
    if search_term:
        search_url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.open(search_url)
        logger.info(f"🎥 Searching YouTube for: {search_term}")
    else:
        webbrowser.open("https://www.youtube.com")

def findContact(query: str):
    """Find contact information (placeholder)."""
    # This would normally search your contacts
    logger.info(f"📱 Finding contact for: {query}")
    return 0, "Unknown"  # Return 0 for no contact found

def whatsApp(contact_no, message, message_type, name):
    """Send WhatsApp message (placeholder)."""
    logger.info(f"📱 WhatsApp {message_type} to {name}: {message}")
    print(f"📱 Would send WhatsApp {message_type} to {name}")

def makeCall(name, contact_no):
    """Make a phone call (placeholder)."""
    logger.info(f"📞 Calling {name} at {contact_no}")
    print(f"📞 Would call {name}")

def sendMessage(message, contact_no, name):
    """Send SMS message (placeholder)."""
    logger.info(f"📧 Sending SMS to {name}: {message}")
    print(f"📧 Would send SMS to {name}: {message}")
