# Alarm clock project in python 

import time
import datetime
import pygame

def set_alarm(alrm_time):
    print(f"Alarm set for {alrm_time}")
    sound_file = "alarm_sound.mp3"  # Put your actual mp3 file here
    is_running = True

    try:
        while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}", end="\r")

            if current_time == alrm_time:
                print("Alarm ringing, WAKE UP!")

                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy(): # wait for the music to finish playing
                    time.sleep(1) # check every second
                break
    except KeyboardInterrupt:
        print("\nTimer stopped manually.")

if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
