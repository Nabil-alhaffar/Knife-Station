import RPi.GPIO as GPIO
import time
#!/usr/bin/env python3
import speech_recognition as sr


class Dictionary:

    def __init__(self):
        chefs_knife_uses = {"dice vegetables", "chop nuts", "slice herbs", "cut watermelon", "mince cilantro"
                            "carve meat", "chop onion","diced vegetables","sliced herbs","chopped nuts","minced cilantro","chopped onion","carve meat"}
        knife1 = Knife("chef's knife", 21, chefs_knife_uses)

        paring_knife_uses = {"peeling fruits", "peeling vegetables", "cut tomatoes", "cut vegetables",
                             "mince garlic","minced garlic", "mince", "devein shrimp", "cut mushroom", "peel pear", "peel apple",
                             "core apple", "peel tomatoes", "peel orange", "hull strawberries", "core tomatoes",
                             "slice citrus", "slice salami", "slice sausage","sliced salami", "slice lemon","sliced lemon","sliced citrus","peeled peach",
                             "slice lemon","sliced lemons","sliced sausage","peel grape", "peel peach", "cut peach",
                             }
        knife2 = Knife("paring knife", 37, paring_knife_uses)

        bread_knife_uses = {"slice bread", "cut bread", "bread", "cut sandwich", "slice cake","sliced cake", "slice bagels","sliced bagel", "slice bagel",
                            "sliced bagels"}
        knife3 = Knife("bread knife", 7, bread_knife_uses)

        utility_knife_uses = {"peel potatoes", "peel potato","slice meat","sliced meats", "chop vegetables", "slice cheese", "slice meet", "slice tomatoes","dice carrots"
                              "cut tomatoes", "core cabbage", "cut apple","cut carrots","cut carrot","diced carrot","diced carrots","dice carrot","dice carrots", "cut cucumbers",
                              "cut cucumber","peel cucumber","peel cucumber","sliced cheese", "sliced Meats", "sliced meat","cut potatoes","cut potato"}
        knife4 = Knife("utility knife", 13, utility_knife_uses)

        shears_uses = {"snip herbs", "cut chicken", "cut poultry"}
        knife5 = Knife("shears", 12, shears_uses)

        boning_knife_uses = {"remove bones", "bone meat", "bone fish", "bone", "trim fat"}
        knife6 = Knife("boning knife", 6, boning_knife_uses)

        cleaver_uses = {"cleave bones", " dice vegetables", "dice fruits", "split meat from bone", "slice ribs",
                        "split poultry", }
        knife7 = Knife("cleaver", 31, cleaver_uses)


        self.data_base = {
            knife1: knife1.knife_uses,
            knife2: knife2.knife_uses,
            knife3: knife3.knife_uses,
            knife4: knife4.knife_uses,
            knife5: knife5.knife_uses,
            knife6: knife6.knife_uses,
            knife7: knife7.knife_uses,
            
        }


class Knife:
    def __init__(self, knife_name, knife_id, knife_uses):
        self.knife_name = knife_name
        self.knife_id = knife_id
        self.knife_uses = knife_uses


def find_in_database(audio_command, knives):

    for key, value in knives.items():
        if audio_command.lower() in value:
            print("The correct knife to use is:", key.knife_name)
            return (key.knife_id)


def speech_collector(knife):
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source,phrase_time_limit=2)
    message = r.recognize_google(audio)
    try:
        print("You said " + message)
    except sr.UnknownValueError:
        pass
        print("Could not understand audio")
        
    except sr.RequestError as e:
        pass
        print("Could not request results; {0}".format(e))
    
    knife_id= find_in_database(message, knife)
    led_switch(knife_id)
    
    
def led_switch(knife_id):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    ledPin=knife_id
    GPIO.setup(ledPin, GPIO.OUT)
    print ("led turning on")
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(ledPin, GPIO.LOW)

    
if __name__ == '__main__':
    knifeDictionary = Dictionary()
    while True:
        try:
            speech_collector(knifeDictionary.data_base)
            
        except:
            print ("say something:")
            pass




    
