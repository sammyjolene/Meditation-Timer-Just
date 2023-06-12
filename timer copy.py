#Create a simple meditation timer that will allow you to input a time and add in interval chimes if you want them.
#input 1 = meditation_length = equals that total length of the meditation session
#input 2 = interval_length = the length between each sound, if you leave it blank it will default to meditation_length
#Function: Entering the number will start a time that will count down on screen (when I have a front-end) 
##and make a sound at the end of session. It will also make a sound at each time interval if one was input

#stage 1 -- create the coundown with a sound playing every minute - COMPLETE
#stage 2 -- allow a user to input the interval that the sound is played - COMPLETE

#Sound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=14610">Pixabay</a>

import time
import simpleaudio as sa

#stage 1 - complete
meditation_length = int(input("How many minutes would you like to meditate: "))

#the length between each sound, just re-enter the meditation length for start and end ding only
interval_length = int(input("How often (in minutes) would you like the interval ding to go off: "))

#converts seconds to minutes for range countdown
new_Mlength = int(meditation_length*60)

#converts seconds to minutes for interval 
new_Ilength = int(interval_length*60)

#ding command creates a WaveObject from a wave file on disk
ding = sa.WaveObject.from_wave_file("service-bell-ring-14610.wav")

#count for interval dings
count = 0

#counts down from the number of seconds to -1, moved stop to -1 so that 00:00:00 shows at the final time and has an ending tone
for x in range((new_Mlength), -1, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)

    #As we increment count if it is dvisible by interval length the ding should go off OR when we hit the last x (-1) in the range
    if count % new_Ilength == 0 or x == 0:
        play_sound = ding.play()
    count += 1

    #prints the time left
    time_left = (f"{hours:02}:{minutes:02}:{seconds:02}")
    print(time_left)

    #suspends execution for 1 second, creating the timer
    time.sleep(1)

print("Time's up")


#copied to make changes to the original