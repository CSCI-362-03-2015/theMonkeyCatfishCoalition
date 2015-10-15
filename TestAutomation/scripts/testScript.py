import os
import unittest
import subprocess

def main():

    tests=[]
    #this portion empties the temp directory 
    for j in os.listdir("../temp/"):
        os.remove("../temp/" + j)
    #changes to the TestAutomation directory
    os.chdir("../")
    for file in os.listdir("testCases"):
        if file.endswith(".txt"):
            print(file)
            with open(os.getcwd()+"/testCases/"+file, "r") as f:
                i =0
                lines =[]
                for line in f:
                    lines.append(line)
                    i = i+1
                print("this is test case #: "+lines[0].strip('\n'))
                print("this will be "+lines[1].strip('\n'))
            

main()
