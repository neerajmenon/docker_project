# docker_project
Project 3 on Docker for CS6065 Cloud Computing

This repository contains the Image and Source Code for Project 3.

Steps for Running
-----------------
1. Load the image from the tar file: (uploaded on Canvas or download from the link below)
https://drive.google.com/file/d/1qgf7eddAUIGfJBMnPooSiRs1wYV93b64/view?usp=sharing

docker load < project3.tar

2.  Run a container from the extracted image :

docker run -it -v </path/to/dir>:/home/data project3_image python3 wc.py

Replace </path/to/dir> with your directory with the files to map to /home/data inside the container
Also remember to suffix the command python3 wc.py at the end to run the python script inside the container upon start-up

3. Result will be on the screen as follows :

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



