from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import smtplib
import base64
import os

class ConvoBot:
    def __init__(self):
        print("Initializing...Please wait!")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://cleverbot.com')
        self.now = datetime.now()
        self.filename = self.now.strftime("%m%d%Y-%H%M%S")
        print("READY!!")
        
    def send(self, user_input):
        #with open(self.filename +'.txt', 'a') as f:
        #    f.write("You: " + user_input + "\n")
        self.driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(str(user_input))
        self.driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(Keys.ENTER)
            
    def reply(self):
        # Get Response from bot
        try:
            self.line1_present = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "line1")))      
            if self.line1_present:
                share_icon_present = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="line1"]/span[2]')))                
                if share_icon_present:
                    bot_response = self.driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
                    return bot_response
                    print("Bot: " + bot_response)  
                    #with open(self.filename +'.txt', 'a') as f:
                    #    f.write("Bot: " + bot_response + "\n")       
                else:
                    print("Failure...Quiting bot!")
        
        except NoSuchElementException:
            print("Error getting bot's response.")
            print("Quiting bot!")
            
    def start_chat(self, message):
        self.quit_bot = True
        while self.quit_bot:
            #message = input("You: ")
            if message == 'exit':
                yesNo = input("Would you like to receive a transcript of the chat? (y/n): ")
                if yesNo == "y":
                    #ask_email = input("Enter your email and press enter: ")
                    #self.email_transcript(ask_email)
                    print("Transcript emailed. Exiting bot!")
                else:
                    print("You chose not to receive the transcript. Exiting bot!")
                self.driver.quit()
                self.quit_bot = False
            else:
                self.send(message)
                self.reply()
             