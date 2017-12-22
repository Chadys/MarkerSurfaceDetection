# WHAT IS IT
A simple demo program detecting an ARuco board

# HOW TO USE
You need to have Anaconda.
Start by launching 'calibration.py', which will write a configuration file of your camera.
You'll need to film the image 'pattern_chessboard.png' until the program has enought samples (detection of the pattern is shown by colored lines, the program quits on its own when it's finished calibrating).
Then you can launch 'board_detection.py' and you'll see the correct directional vectors appearing when you film 'board_aruco_57.png'.

# CREDITS
See file 'useful_links' for tutorial used