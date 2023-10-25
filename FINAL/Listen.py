# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

def Listen():
    warnings.simplefilter("ignore")
    url = "https://dictation.io/speech"
    chrome_driver_path = 'D:\\Jarvis\\Brain\\chromedriver.exe'
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Use fake UI for media access
    chrome_options.add_argument("--use-fake-device-for-media-stream")
        # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    try:
        
        
        # Add a wait for the "Clear Dictation Notepad" button
        wait = WebDriverWait(driver, 10)
        clear_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]"
        clear_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_button_xpath)))
        
        # Close cookie consent banner if present
        try:
            cookie_banner = driver.find_element(by=By.ID, value="cookieconsent:desc")
            close_button = driver.find_element(by=By.CLASS_NAME, value="cc-btn.cc-dismiss")
            close_button.click()
        except Exception:
            pass

        # Click the "Clear Dictation Notepad" button
        clear_button.click()
        
        # Click the "Start" button for speech recognition
        start_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
        start_button = driver.find_element(by=By.XPATH, value=start_button_xpath)
        start_button.click()
        print("Microphone is turned on")

    except Exception as e:
        print("Error: Unable to configure the ChromeDriver properly.")
        print("To resolve this error, make sure to set up the ChromeDriver correctly.")
        print(e)
    output_file_path="D:\Om Folder\SCIENCE EXHIBITION\JARVIS\main\SpeechRecognition.txt"
    while True:
        text_element_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
        text = driver.find_element(by=By.XPATH, value=text_element_xpath).text

        if len(text) == 0:
            pass
        
        
        else:
            driver.find_element(by=By.XPATH, value=clear_button_xpath).click()
            text = text.strip()
            with open(output_file_path, "w") as file_write:
                file_write.write(text)

Listen()

