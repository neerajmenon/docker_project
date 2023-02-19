# docker_project
Project 3 on Docker for CS6065 Cloud Computing

This repository contains the Image and Source Code for Project 3.

Steps for Running
-----------------
1. Load the image from the tar file: (uploaded on Canvas or download from the link below)
https://drive.google.com/file/d/1qgf7eddAUIGfJBMnPooSiRs1wYV93b64/view?usp=sharing

docker load < project3_img.tar


2.  Run a container from the extracted image :

docker run -it -v </path/to/dir>:/home/data project3_img python3 wc.py

Replace </path/to/dir> with your directory with the files to map to /home/data inside the container
Also remember to suffix the command python3 wc.py at the end to run the python script inside the container upon start-up.
The container reads the files from /home/data and writes results to /home/output/result.txt before printing its contents onto the shell

<img width="1142" alt="image" src="https://user-images.githubusercontent.com/14856688/219968378-31a2a926-487c-4dd1-9507-20f92de5be55.png">



