#Create a simple meditation timer that will allow you to input a time and add in interval chimes if you want them.
#input 1 = meditation_length = equals that total length of the meditation session
#input 2 = interval_length = the length between each sound, if you leave it blank it will default to meditation_length
#Function: Entering the number will start a time that will count down on screen (when I have a front-end) 
##and make a sound at the end of session. It will also make a sound at each time interval if one was input

#stage 1 -- create the coundown with a sound playing every minute - COMPLETE
#stage 2 -- allow a user to input the interval that the sound is played - NOT STARTED

#Sound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=14610">Pixabay</a>

import time
import simpleaudio as sa

#stage 1 - complete
#notes: having the bell toll at 1 second instead of zero so that it tolls at the end too
meditation_length = int(input("How many minutes would you like to meditate: "))

#converts seconds to minutes for range countdown
new_length = int(meditation_length*60)

#ding command creates a WaveObject from a wave file on disk
ding = sa.WaveObject.from_wave_file("service-bell-ring-14610.wav")

#counts down from the number of seconds to -1, moved stop to -1 so that 00:00:00 shows at the final time and has an ending tone
for x in range((new_length), -1, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)

    #plays a ding each minute
    if seconds == 00:
        play_sound = ding.play()
        print('Interval')

    #prints the time left
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    #suspends execution for 1 second, creating the timer
    time.sleep(1)
    
print("Time's up")