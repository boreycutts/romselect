import os
import sys
import shutil

source = input("Input the source directory (leave blank to use the current directory): ")
while not os.path.isdir(os.getcwd() + "/" + source):
    source = input("Yo headass this directory doesn't exist 🤯. Input a real one please (like this --> C:\\Users\\Nick\\sourcedir): ")

destination = input("Input the destination directory: ")
while not os.path.isdir(destination) or not destination: 
    if not destination:
        destination = input("Yo headass please specify a destination directory: ")
    else:
        destination = input("Yo headass this directory doesn't exist 🤯. Input a real one please (like this --> C:\\Users\\Nick\\destinationdir): ")

romlist = input("Input the list of roms: ")
while not os.path.isfile(romlist) or not romlist:
    if not romlist:
        romlist = input("Yo headass please specify a text file containing the list of roms: ")
    else:
        romlist = input("Yo headass this file doesn't exist 🤯. Input a real one please and make sure its in the same directory as this script (like this --> romlist.txt):")

roms = []
with open(romlist, "r") as f:
    roms = f.read().splitlines()
    if not len(roms) > 0:
        print("Yo this list is empty fool. Tf am I supposed to do with this???")
        exit()

dontexist = []
for rom in roms:
    if os.path.isfile(source + "/" + rom):
        shutil.copy(source + "/" + rom, destination + "/" + rom)
    else:
        dontexist.append(rom)

print("its done fool XD")
if len(dontexist) > 0:
    print("Yo some of these roms you gave me don\'t exist. Here\'s a list of em:")
    for rom in dontexist:
        print(dontexist)