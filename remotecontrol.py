__author__ = "Doğan Seyfi Şen"

import random
import time

class RemoteControl():
    def __init__(self, tvOnOff = "Off", tvVoice = 0, channels = ["TRT", "BBC", "ZDF"], ch = "BBC"):
        self.tvOnOff = tvOnOff
        self.tvVoice = tvVoice
        self.channels = channels
        self.ch = ch
    def tvOn(self):
        print("TV is now on.")
        self.tvOnOff = "On"
    def tvOff(self):
        print("TV is now off.")
        self.tvOnOff = "Off"
    def voiceSettings(self):
        while True:
            voiChar = input("Press '<' to turn the voice down | '>' to turn the voice up | To exit press 'Q or q': ")
            if (voiChar == "<"):
                if (self.tvVoice != 0):
                    self.tvVoice -= 1
                    print("Voice: ", self.tvVoice)
            elif (voiChar == ">"):
                if (self.tvVoice != 50):
                    self.tvVoice += 1
                    print("Voice: ", self.tvVoice)
            else:
                print("Voice level: ", self.tvVoice)
                break
    def __str__(self):
        return "\nTV On/Off: {}\nVoice: {}\nChannels: {}\nChannel you watch: {}\n".format(self.tvOnOff,self.tvVoice,self.channels,self.ch)
    def __len__(self):
        return  len(self.channels)
    def addChannel(self,ch):
        print("Adding: ",ch)
        self.channels.append(ch)
    def randomChannel(self):
        ranCh = random.randint(0,len(self.channels)-1)
        self.ch = self.channels[ranCh]
        print("The channel you watch now: ", self.ch)
remoteControl = RemoteControl()

print("""
============================
TV RC CONSOLE
----------------------------
OPERATIONS:
----------------------------
1. TV ON
2. TV OFF
3. TV INFOS
4. TOTAL OF CHANNELS
5. ADDING A NEW CHANNEL
6. VOICE SETTINGS
7. RANDOM CHANNEL
----------------------------
TO QUIT PRESS 'Q or q'.
============================""")

while True:
    ope = input("Choose operation: ")
    if (ope == "q" or ope == "Q"):
        print("Exiting the program...")
        time.sleep(1)
        print("Exited.")
        break
    if (ope == "1"):
        remoteControl.tvOn()
    elif (ope == "2"):
        remoteControl.tvOff()
    elif (ope == "3"):
        print(remoteControl)
    elif (ope == "4"):
        print("Total of Channels: ",len(remoteControl))
    elif (ope == "5"):
        newChannels = input("Please separate by using ',' the channels that you want to add. Please add: ")
        adding = newChannels.split(",")
        for i in adding:
            remoteControl.addChannel(i)
        time.sleep(2)
        print("List of channel has successfully updated.")
    elif (ope == "6"):
        remoteControl.voiceSettings()
    elif (ope == "7"):
        remoteControl.randomChannel()
    else:
        print("Invalid operation...")
