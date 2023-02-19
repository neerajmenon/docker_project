# docker_project
Project 3 on Docker for CS6065 Cloud Computing

This repository contains the Image and Source Code for Project 3.

Steps for Running
-----------------
1. Download the image and run using

docker run -it -v </path/to/dir>:/home/data project3_image python3 wc.py

Replace </path/to/dir> with the directory you want to map to /home/data inside the container
Ensure to suffix the command python3 wc.py at the end to run the python script inside the container as it starts up

2. Result will be on the screen as follows :

Files and directories in ' /home/data ' :
['.DS_Store', '6065_ubuntu1_key.cer', 'Hw1_NeerajMenonManghat.pdf', 'IF.txt', 'Limerick.txt', 'cloud_ass1.png', 'mapreduce-osdi04_google-1.pdf', 'wc.py']
Attempting to read IF.txt
Attempting to read Limerick.txt
Word count for IF:  287
Word count for Limerick:  32
Total Count:  319
Top 3 words in If: 
[('you', 12), ('can', 12), ('your', 10)]
Host Name:  da2f7fb3dfce
IP Address:  172.17.0.2



