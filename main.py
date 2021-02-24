import urllib.request 
# This will import a libray in the program and to find URL and download it
import os

def processFile(): 
  file= open ("http_access_log.txt")
  data = file.read()
  year1 = data.count("1994")
  year2 = data.count("1995")
  print("Data was accessed ", year1, " times in 1994.")
  print("Data was accessed ", year1 + year2, " times in 1994 and 1995.")

path= "./http_access_log"
exists = os.path.exists(path)

print("This program will process the access log file data.")

if exists:
  print("Gathering data from existing file...")
  print("Results: ")
  processFile()
  
else:
  print("Downloading data...")
  url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
  urllib.request.urlretrieve(url,'./http_access_log.txt')

  print("Results: ")
  processFile()
