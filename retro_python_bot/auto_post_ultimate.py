from instabot import Bot
import datetime
import time
import os
import shutil
import schedule


DIR = "./posts/pending" # Directory for the posts.

post = (datetime.date.today()).strftime("%d%m%Y.jpg") # Pst string with current date formatted as 'yearmonthday.jpg'.
description = post[:8]+'.txt'

current_day = (datetime.date.today().weekday()) # Number of weekday from 0-6.
current_time = int(str(datetime.datetime.now().time())[:2]) # Current hour in 24h format.

bot = Bot() # Initializes Bot() function.

def upload():
    for file in os.listdir(DIR):
        if file == post:
            with open(DIR+'/'+description, 'r') as file: # Opens and reads the caption file of the post.
                caption = file.read()

            bot.upload_photo(DIR+'/'+post, caption=caption) # Upload function.
            print(f'UPLOADED {post}!')

            try:
                shutil.move(DIR+'/'+post, './posts/uploaded/'+post)
                shutil.move(DIR+'/'+description, './posts/uploaded/'+description)
            except:
                print('Unable to move file to new directory. Has the file name changed after the upload?')
        else:
            print('No file has been found to upload.')


def main():
    bot.login() # Login for the instabot module.

    # Check message before beginning own script.
    print('\n---RETROPYTHON---\nChecking for posts to upload...')
    time.sleep(3)

    # Scheduled uploads following 'Education Sector' trends.
    schedule.every().monday.at("14:00").do(upload)
    schedule.every().tuesdat.at("19:00").do(upload)
    schedule.every().wednesday.at("11:00").do(upload)
    schedule.every().thursday.at("15:00").do(upload)
    schedule.every().friday.at("10:00").do(upload)
    schedule.every().saturday.at("20:00").do(upload)
    schedule.every().sunday.at("10:00").do(upload)

    while True:
        schedule.run_pending()
        time.sleep(1)




main()
