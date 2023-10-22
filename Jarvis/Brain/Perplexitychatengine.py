from time import sleep  # Import sleep function from the time module for delays
from selenium import webdriver  # Import the Selenium webdriver module
from selenium.webdriver.chrome.options import Options  # Import Chrome options for configuring the webdriver
from selenium.webdriver.common.by import By  # Import By class for locating elements in the DOM
import warnings  # Import warnings module for ignoring warnings
from selenium.webdriver.chrome.service import Service  # Import Service class for the Chrome webdriver
from selenium.webdriver.support.ui import Select
import pyttsx3

warnings.simplefilter("ignore")
url = "https://labs.perplexity.ai/"
chrome_driver_path = 'Brain\\chromedriver.exe'
chrome_options = Options()
# chrome_options.add_argument("--headless=new")  # Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)

def TextToSpeech(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'David' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.say(Text)
    engine.runAndWait()

ChatNumber = 3

def SecurityByPass():

    while True:
        WebsiteTitle = driver.title
        if "just a moment" in str(WebsiteTitle).lower():
            driver.refresh()
            sleep(3)

        else:
            break

def Setup():
    try:
        SelectButton = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[2]/div[1]/div/div[2]/div/div/div/div/select")
        Select(SelectButton).select_by_index(3)

    except:
        pass

    
def QuerySender(Query):

    Query = str(Query).lower()
    try:
        TextBox = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/textarea")
        TextBox.send_keys(Query)

    except Exception as e:
        print(e)

    sleep(0.5)

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/button").click()

    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/button").click()

def WaitForTheResult():

    sleep(1)

    while True:

        try:
            ButtonStop = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/main/div/div/div[2]/div[2]/div/div/button[2]').is_enabled()

        except:
            break

def Result():

    global ChatNumber
    ChatNumber = str(ChatNumber)
    XpathValue = f"/html/body/div/main/div/div/div[1]/div/div[2]/div/div/div/div[{ChatNumber}]/div/div/div[2]/div[1]/div[2]/div"

    try:
        Text = driver.find_element(by=By.XPATH,value=XpathValue).text
        return Text

    except Exception as e:
        print(e)

    ChatNumberNew = int(ChatNumber) + 2
    ChatNumberNew = str(ChatNumberNew)
    ChatNumber = ChatNumberNew

SecurityByPass()
Setup()

# Var = '''Hello, My Name is Tony Stark. You're my personal ai assistant "Jarvis". Whenever i asks you about what's the time? what's the date? or if i ask you about individual who is not widely recognized. respond with "Sorry, I can't answer That"'''
# QuerySender(Var)

while True:
    Query = input("Enter The Query Here :")
    QuerySender(Query=Query)
    WaitForTheResult()
    Text = Result()
    print(Text)
    TextToSpeech(Text=Text)
    