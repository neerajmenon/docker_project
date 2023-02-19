import socket
import os
 
# Get the list of all files and directories
path = "/home/data"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

def count_words(filename):
  number_of_words = 0
  with open(filename,'r') as file:
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)
    return number_of_words 


print("Attempting to read IF.txt")
if_count = count_words("/home/data/IF.txt")
print("Attempting to read Limerick.txt")
lim_count = count_words("/home/data/Limerick.txt")
print("Word count for IF: ",if_count)
print("Word count for Limerick: ",lim_count)
print("Total Count: ",(if_count+lim_count))

def top_3(string):
    return get_top_3(get_frequency_hash(string))

def get_frequency_hash(text):
    array = text.split(" ")
    frequency = {} 
    for word in array: 
        try: 
           frequency[word] += 1 
        except: 
           frequency[word]= 1
    return frequency

def get_top_3(frequency_hash):
    array_of_tuples = [(k,v) for k,v in frequency_hash.items()]
    sorted_array_of_tuples = sorted(array_of_tuples, key=lambda x: -x[1])
    return [(k,v) for k,v in sorted_array_of_tuples[0:3]]

print("Top 3 words in If: ")
with open('/home/data/IF.txt','r') as file:
    data = file.read()            
    print(top_3(data))

 
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Host Name: ",hostname)
print("IP Address: ",IPAddr)



  
