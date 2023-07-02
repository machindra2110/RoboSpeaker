
import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1, Created by Machindra")
    while True:
        x = input("Enter what you want to say to me:")
        if x == 'q':
            os.system("Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('good Bye , Thanks for visit')")    #for exit
            break
        command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)



