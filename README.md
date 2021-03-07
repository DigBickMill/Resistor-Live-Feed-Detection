# Resistor-Live-Feed-Detection
Designed to run on Raspberry Pi using the Pi camera 2.0. This project aims to be able to detect resistors in a camera live feed, calculate its value and display it through a transparent OLED display driven by an Arduino. The results from the project show that while it is possible to detect resistors, the accuracy at which the program is able to calculate its value can fluctuate wildly, due to the inherent issue of detecting specific colours without the test being in a controlled environment.


My main input into this project stems from training the tflite graph, and writing/appending the files "ColourAnalyser.py", "Display.py", "object_detector.py" and "Display_Driver.INO". I do not claim to own any other work and have followed two guides listed below.

## Making use of these files
To recreate this detection algorithm, I would recommend using the video below as a guide for configuring a Raspberry Pi with the correct environment.
https://www.youtube.com/watch?v=aimSGOAUI8Y&ab_channel=EdjeElectronics

After the environment is setup, add the files "ColourAnalyser.py", "Display.py" and "object_detector.py" into this environment (replace the original object_detector file with this new file as it is what calls to our additional code.

If you are also wishing to display the value out to the SparkFun Transparent OLED Display, I wired the display to an Arduino using the SPI pins instructed. I then used the USB connections between the Raspberry Pi and Arduino in order to send the result to the display. To enable the display to work, compile and upload the "Display_Driver.INO" sketch to the arduino board.


## Content that guided this project
"Webcam Object Detection Using Tensorflow-trained Classifier" by Evan Juras
“Creating your own object detector with the Tensorflow Object Detection API" by Gilbert Tanner
