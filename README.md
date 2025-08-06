# 🤖 Personal AI Desktop Assistant

<div align="center">

![AI Assistant](https://img.shields.io/badge/AI-Assistant-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

*An intelligent personal desktop assistant designed to enhance productivity and simplify tasks through natural language interaction.*

</div>

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [⚡ Installation](#-installation)
- [🚀 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🌟 Features

### 🎯 Core Functionalities

- **🗣️ Voice & Text Interaction**: Communicate seamlessly using voice commands or text inputs
- **🔧 Task Automation**: Streamline your workflow with intelligent automation
- **🧠 Personalized Assistance**: Adaptive learning for customized user experience

### 🚀 Task Automation

- **📱 Application Management**
  - Launch browsers, text editors, media players
  - Quick access to frequently used applications
  
- **📊 Information Retrieval**
  - Real-time weather updates with OpenWeatherMap API
  - Current time and date information
  - Web searches with intelligent responses
  - Location-based weather forecasting

### 👤 Personalized Assistance

- **🧠 Smart Memory**
  - Remember user preferences and frequently used commands
  - Adaptive behavior based on usage patterns
  
- **⏰ Schedule Management**
  - Set reminders, alarms, and notifications
  - Calendar event management

### ✨ Additional Features

- **🔢 Problem Solving**
  - Mathematical calculations
  - Logical problem resolution
  
- **🎵 Media Control**
  - Play music and videos
  - Media player integration
  
- **⚙️ System Management**
  - Adjust volume and brightness
  - System settings control
  
- **📧 Communication**
  - Email management
  - Calendar event handling

---

## 🛠️ Technology Stack

### 🔧 Backend
| Component | Technology |
|-----------|------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Web Framework** | Eel for desktop web apps |
| **Speech Processing** | pyttsx3, SpeechRecognition |
| **Weather API** | OpenWeatherMap API |
| **HTTP Requests** | requests library |

### 🎨 Frontend
| Component | Technology |
|-----------|------------|
| **Web Interface** | HTML5, CSS3, JavaScript |
| **GUI Framework** | Eel (Python to Web) |
| **Interface** | Modern responsive web design |

### 💾 Database
| Component | Technology |
|-----------|------------|
| **Local Storage** | SQLite |
| **Cloud Options** | Cloud-based solutions for data sync |

---

## ⚡ Installation

### 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- OpenWeatherMap API key (free)
- Microphone for voice commands

### 🔽 Step-by-Step Setup

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/detactivepritam/Personal-AI-Desktop-Assistant.git
   cd Personal-AI-Desktop-Assistant
   ```

2. **📦 Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **🔑 Set Up API Keys**
   
   Get your free OpenWeatherMap API key:
   - Visit: https://openweathermap.org/api
   - Sign up for a free account
   - Get your API key from the dashboard
   
   Update `command.py`:
   ```python
   OPENWEATHER_API_KEY = "your_actual_api_key_here"
   ```

4. **🚀 Run the Application**
   ```bash
   python run.py
   ```

---

## 🚀 Usage

### 🎯 Quick Start

1. **🔊 Choose Input Mode**: Select between voice or text input modes
2. **💬 Interact Naturally**: Use natural language commands
3. **⚙️ Customize**: Adjust settings through the intuitive GUI

### 💡 Example Commands

| Command Type | Example |
|--------------|---------|
| **App Launch** | *"Open YouTube"* |
| **Weather** | *"Weather in London"* |
| **Information** | *"What's the time?"* |
| **Search** | *"Search for Python tutorials"* |
| **Media** | *"Play classical music"* |

### 🎨 Customization

- **🎯 Voice Commands**: Use natural language for all interactions
- **🌤️ Weather Integration**: Get real-time weather for any city
- **🎵 Media Control**: YouTube integration for music and videos
- **📊 Web Search**: Intelligent Google search integration

---

## 🌤️ Weather Feature

Get real-time weather information for any city worldwide!

### Weather Commands:
- *"Weather in [city name]"*
- *"Weather of [city name]"*
- *"Weather for [city name]"*
- Just say *"weather"* and specify the city when asked

### Setup:
1. Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace `OPENWEATHER_API_KEY` in `command.py` with your key
3. Start using weather commands immediately!

---

## 🎮 Available Commands

### 🌐 Web & Applications
- *"Open YouTube"* - Opens YouTube
- *"Open Google"* - Opens Google Search
- *"Search for [topic]"* - Google search

### 🌤️ Weather Information
- *"Weather in Mumbai"* - Get Mumbai weather
- *"Weather of London"* - Get London weather
- *"What's the weather like?"* - Ask for city

### ⏰ Time & Date
- *"What's the time?"* - Current time
- *"Tell me the time"* - Current time

### 🎵 Media & Entertainment
- *"Play [song/artist]"* - YouTube search
- *"Play music"* - Open YouTube

---

## � Advanced Features

### 🎤 Voice Recognition
- Continuous hotword detection
- Natural language processing
- Multi-language support (configurable)

### 🌐 Web Interface
- Modern responsive design
- Real-time command feedback
- Voice and text input options

### 🔄 Process Management
- Dual-process architecture
- Graceful shutdown handling
- Error recovery mechanisms

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Personal AI Desktop Assistant Team](https://github.com/detactivepritam)

</div>
