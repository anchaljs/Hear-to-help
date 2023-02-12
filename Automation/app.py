#webdriver not installed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3
import js2py #to convert js into python
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
# from goto import with_goto
#from selenium.webdriver.common.action_chains import ActionChains #hover-----------------------

driver = webdriver.Chrome('D:\\Python\\Automation\\chrome-driver')
driver.maximize_window()
#action = ActionChains(driver) #hover---------------------

#initialize assistant
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#to set the voice type
engine.setProperty('voice', voices[1].id) #here 0 means male, and 1 means female

# engine.say('Hi! I am a voice assistant')
# engine.runAndWait()

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response

time.sleep(3)
speak("Hello master! I am now online..")

# @with_goto
# label .start
while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' in voice:
        speak('Opening google...')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(window_list[-1])
        driver.get('https://google.com')

    elif 'college' in voice:
        speak('Opening your college...')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(window_list[-1])
        driver.get('https://www.igdtuw.ac.in/')
    
    elif 'search google' in voice:
        while True:
            speak('I am listening...')
            query = recognize_speech()
            if query != 'Error':
                break

        # element = driver.find_element_by_name('q')
        element = driver.find_element("name",'q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)

    elif 'switch tab' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab=0
        for i in range(num_tabs):
           if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i+1
                    break
        driver.switch_to.window(driver.window_handles[cur_tab])

    elif 'close tab' in voice:
        speak('Closing Tab...')
        driver.close() 
    
    elif 'go back' in voice:
        driver.back()

    elif 'go forward' in voice:
        driver.forward()

    elif 'exit' in voice:
        speak('Goodbye Master!')
        driver.quit()
        break


    #JUGAAADDDDDD
    #Navbar
    elif 'navigation' in voice:
        URL  = driver.current_url
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, 'html.parser')

        tags = soup.find_all(class_ = 'dropdown-toggle')
        for tag in tags:
            speak(tag.get_text())
            #firstLevelMenu = driver.find_element_by_id("menu")
            #action.move_to_element(tag).perform()

        speak('Which one do you want to explore?')
        # voice = recognize_speech().lower()
        # print(voice)

        # if 'yes' in voice:
        #     speak('Which one do you want to explore?')
   
        voice = recognize_speech().lower()
        print(voice)
        if 'student life' in voice:
            speak('Opening your student life section...')
            driver.execute_script("window.open('');")
            window_list = driver.window_handles
            driver.switch_to.window(window_list[-1])
            driver.get('https://www.igdtuw.ac.in/studentlife.php?id=1')
            

            while True:
                voice = recognize_speech().lower()
                print(voice)
                if 'read content' in voice:

                    URL  = driver.current_url
                    content = requests.get(URL)
                    soup = BeautifulSoup(content.text, 'html.parser')

                    title = soup.find(class_ = 'title')
                    speak(title.get_text())
                    text = soup.find(class_ = 'headingPara')
                    speak(text.get_text()) 

                # voice = recognize_speech().lower()
                # print(voice)
                elif 'navigation' in voice:

                    URL  = driver.current_url
                    content = requests.get(URL)
                    soup = BeautifulSoup(content.text, 'html.parser')
                    tags = soup.find(class_ = 'sidenav')
                
                    for tag in tags:
                        speak(tag.get_text())

                # voice = recognize_speech().lower()
                # print(voice)
                elif 'close tab' in voice:
                    speak('Going back to main...')
                    driver.close()
                    # goto .start
                 


        
                


        #eval_result, example = js2py.run_file('nav.js')




    else:
        speak('Not a valid command. Please try again..')
    
    # time.sleep(2)
    time.sleep(5)



