# docker_project
Project 3 on Docker for CS6065 Cloud Computing

This repository contains the Image and Source Code for Project 3.

Steps for Running
-----------------
1. Load the image from the tar file: (uploaded on Canvas or download from the link below)
https://drive.google.com/file/d/1qgf7eddAUIGfJBMnPooSiRs1wYV93b64/view?usp=sharing

docker load < project3.tar
<img width="493" alt="image" src="https://user-images.githubusercontent.com/14856688/219966811-a9d84a6a-c688-4e7f-adbf-1dad0703decf.png">


2.  Run a container from the extracted image :

docker run -it -v </path/to/dir>:/home/data project3_image python3 wc.py

Replace </path/to/dir> with your directory with the files to map to /home/data inside the container
Also remember to suffix the command python3 wc.py at the end to run the python script inside the container upon start-up

3. Result will be on the screen as follows :

<img width="1151" alt="image" src="https://user-images.githubusercontent.com/14856688/219966761-5f994aec-175b-4368-84bd-dd89819a7eab.png">



