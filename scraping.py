import requests
from bs4 import BeautifulSoup 
import pandas as pd 
from googletrans import Translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
filtered_sentence_contain = []
import string
filtered_sentence = []
raw_review = []
contain = []
raw_review_without_emoji = []
translated_without_emoji = []
translated_without_emoji_without_periods = []
true_translated = []
no_emoji_sentence = []
dummy = 1
i = 1
slow = 0
import emoji



def selen(person):
    r_number = 1
   
    j = 0
    


    driver.get(person)
    number_on_page = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[1]/div[2]/p[2]').text[1:-1]
    while j == 0:
        driver.implicitly_wait(7)
     
        try:
            
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/button').click()
        except:
            break
    
  
        
    
   
    try:
        for item in range(int(number_on_page)):
            item = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div[2]/div/ul/li['+ str(r_number) + ']/div/div/div[2]/div[1]/p').text
            r_number = r_number + 1
            collected = {
             'Raw Reviews' : item
            }
            raw_review.append(collected)
            
        r_number == 1
        driver.implicitly_wait(1)
        driver.quit()
        
        return raw_review
    except:
        print('Slow Internet Cant load all the reviews in time, please try again later')
        slow = 1
        driver.quit()
        return slow

#first step

    
    return raw_review       
    
def pre_process(raw_reviews):
    filtered_sentence = []
    stop_words = set(stopwords.words('english'))
    divided_text = word_tokenize(raw_reviews)
    
    for word in divided_text:
        if word not in stop_words:
            filtered_sentence.append(word)
    return filtered_sentence
    
#second step  
def google(tag_lish_sentence):
    trans = Translator()
    translated = trans.translate(tag_lish_sentence, src='fil', dest='en')
    return translated.text

#ways
def loops(url):
    while dummy == 1:
        try:
            googles = google(url)
            print(googles)
            break
    
        except:
            googles = google(url)
            print('error1')
            

             
    return googles




#third step
def clean(users):
    while i == 1:
        try:
            loops(users)
            break
        except:
            pass






user = input('Please Enter Store Name :...')
 
url = ('https://www.carousell.ph/' + user + '/reviews/')

try:
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    driver.implicitly_wait(5)
    selen(url)
    
except:
    print('no reviews/ no existed shop')
    driver.quit()



df = pd.DataFrame(raw_review)
print(df)



# for sentence_with_emoji in df['Raw Reviews']:
    
#     each_sentence_with_emoji = {
#         'Raw Review without emoji': emoji.demojize(sentence_with_emoji)
#         }
#     raw_review_without_emoji.append(each_sentence_with_emoji)
    
# df_no_emoji = pd.DataFrame(raw_review_without_emoji)

# print(df_no_emoji)


# for k in df_no_emoji['Raw Review without emoji']:    
#     extracted ={
#               'extracted' :  pre_process(k)
#             }
#     filtered_sentence_contain.append(extracted)
#     ds = pd.DataFrame(filtered_sentence_contain)

        
# print(ds)


# for each_word in ds['extracted']:

#     table = str.maketrans(' ', ' ', string.punctuation)
#     striped = [each_word_ex.translate(table)for each_word_ex in each_word]
#     striped_raw_review = {
#         'Striped':striped
        
#         }
    
#     translated_without_emoji_without_periods.append(striped_raw_review)
    
# df_translated_without_emoji_without_periods = pd.DataFrame(translated_without_emoji_without_periods)


# print(df_translated_without_emoji_without_periods)



    
# for words_striped in df_translated_without_emoji_without_periods['Striped']:
#     for each_words_striped in words_striped:
#         print(loops(each_words_striped))
        


    



        
    

    
            


   




          

    

    
    
    
    

                   








    



    
    

    


    
    















 

