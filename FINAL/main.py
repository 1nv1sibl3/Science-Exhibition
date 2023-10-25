from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyttsx3
from selenium.webdriver.chrome.options import Options
import datetime
from util import search_on_wikipedia, play_on_youtube, search_on_google, get_latest_news

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
    "Okay sir, I'm on it.",
    "Getting it for you sir."
]

NEWS_API="1463eec76f4a4f8c98f3f3ecebbacffd"

# Disable SSL verification
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--log-level=3')
#chrome_options.add_argument('--headless=new')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open the web page
driver.get("https://deepai.org/machine-learning-model/text-generator")

engine = pyttsx3.init()
# Get a list of available voices
voices = engine.getProperty('voices')
# Choose a voice that resembles Jarvis (you may need to experiment with different voices)
# You can set the voice using the voice's ID
jarvis_voice_id = "com.apple.speech.synthesis.voice.alex"  # Example voice ID, adjust as needed
# Set the selected voice
engine.setProperty('voice', jarvis_voice_id)
# Adjust the speech rate and volume as needed
engine.setProperty('rate', 180)  # Adjust the rate to your liking
engine.setProperty('volume', 1)  # Adjust the volume (0.0 to 1.0)
def speak(text):
    engine.say(text)
    engine.runAndWait()




def Get_ans(query):
    try:
        # Prompt for the message you want to send
        prompt_text = str(query)

        # Find the textarea for the prompt
        prompt_area = driver.find_element(By.CLASS_NAME, "model-input-text-input")
        
        # Enter your text into the prompt area
        #prompt_area.clear()  # Clear any existing text
        prompt_area.send_keys(prompt_text)
        print('PROMPT SEND')
        # Find the generate button and click it
        generate_button = driver.find_element(By.ID, "modelSubmitButton")
        generate_button.click()
        print('GENERATED')
        # Wait for the try-it result area to load (adjust the timeout as needed)
        wait = WebDriverWait(driver, 10)
        result_area = wait.until(EC.presence_of_element_located((By.ID, "place_holder_picture_model")))
        print('GETTIN RESULT')
        # Extract the generated text
        generated_text = result_area.text
        print('RETURNING')
        # Print the generated text
        return generated_text

    except Exception as e:
        print(e)
        return f"An error occurred: {e}"



is_jarvis_asleep = False
def get_time_of_day():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    else:
        return "evening"


def greet_user():
    time_of_day = get_time_of_day()
    ai_name = "Jarvis"

    greeting_text = f"Good {time_of_day}, I am {ai_name}, your AI assistant. I am awake and ready to assist."
    exhibition_info = "I was created by Oom Honrao and Praneet Malik from class 10 A."
    full_greeting = f"{greeting_text} {exhibition_info}"
    speak(full_greeting)


def activate_jarvis(command):
    global is_jarvis_asleep
    
    if "sleep" in command.lower():
        is_jarvis_asleep = True
        speak("I'm going to sleep now. Call me when you need assistance.")
        with open("D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt", "w") as f:
                    content = f.write('')
    elif "wake up" in command.lower():
        is_jarvis_asleep = False
        speak("I'm awake now. How can I assist you?")
        with open("D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt", "w") as f:
                    content = f.write('')

if __name__ == "__main__":


    greet_user()
    print("up")
    while True:
        #print('works')
        with open("D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt", "r") as f:
            content = f.read().strip()

        if content:
            query = str(content).lower()
            activate_jarvis(query)
            if not is_jarvis_asleep:
                if query == "wake up":
                    pass
                
                elif "search wiki" in query:
                    query = query.replace("search wiki","")
                    result = search_on_wikipedia(query)
                    speak("just a moment, according to wikipedia")
                    speak(result)

                elif "play youtube" in query:
                    query = query.replace("play youtube","")
                    result = play_on_youtube(query)
                    speak("here are the most viewed videos on the given topic")

                elif "google" in query:
                    query = query.replace("google","")
                    result = search_on_google(query)
                    speak("these are the top results")

                elif "tell me latest headlines" in query:
                    query = query.replace("tell me latest headlines","")
                    result = get_latest_news()
                    speak(result)

                else:
                    query = str(content).lower()
                    answer = Get_ans(query)
                    #with open("D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt", "w") as f:
                    #    content = f.write('')
                    speak(answer)


                with open("D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt", "w") as f:
                        content = f.write('')

        else:
            pass

  


    