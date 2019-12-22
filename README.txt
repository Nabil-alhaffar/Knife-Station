This is the python script for the smart knife station project

Project description:

This project is a knife block that uses the google speech recognition API in order to listen to commands and maps it to the best cutlery item
for that particular task. The knife block will listen through a microphone connected to the RPI, and then gives the output in the form of LED buttons.
For example, you would say "slice lemons", and the paring knife will be suggested. If you say "slice bagels", the bread knife will be suggested, and so on.


Software: Python, google speech recognition API
Hardware: RPI 3+, wirings and LED lights, custom designed and 3D printed knife block
----------------------------------------------------------------------------------------------------------

Running instructions:

1- Locate the python script "KnifeStation.py" and open it with IDLE or your preferred python IDE/editor
2- Connect the mouse, keyboard, the microphone and HDMI cable to the RPI embedded within the knife Station and run the script.
3- You can observe the command the knife station listened to through the monitor.
4- Once the knife station gets a predefined command, it will trigger the LED lights corresponding to the suggested knife.

