from time import strftime, localtime
import os
import re
import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("")

# Hardcoded intialized variables 
endLoop = True
file = 'main'
authorToNumberOfCommitsMap = {"test": "HAHA"}
firstCommitMap = {"test": 0}
lastCommitMap = {"test": 2000000000}

while endLoop: 
    endLoop = False
    cmd = ('git', 'cat-file', '-p', file)
    process1 = subprocess.run(cmd, capture_output=True, text=True)
    output1 = process1.stdout
    
    cat_file_lines = output1.split("\n")
    for line in cat_file_lines:

        #  Parsing
        if re.search("parent", line):
            file = line[7:47]
            endLoop = True
        if re.search("author", line):
            authorStart = re.search(r"<", line)
            timeStart = re.search(r">", line)
            author = line[authorStart.start()+1:timeStart.start()]
            epoch = line[timeStart.start()+2:timeStart.end()+12]

            # Counting number of contributions by author and storing in dictionary
            authorNumFlag = False
            for authors in authorToNumberOfCommitsMap:
                if author.__eq__(authors):
                    num = authorToNumberOfCommitsMap[author]
                    num = num + 1
                    authorToNumberOfCommitsMap[author] = num
                    authorNumFlag = True
            
            if authorNumFlag == False:
                authorToNumberOfCommitsMap[author] = 1

            # Calculating first commit date for author and storing in dictionary
            firstCommitFlag = False
            for person in firstCommitMap:
                if author.__eq__(person):
                    firstCommitFlag = True
                    if int(epoch) > int(firstCommitMap[person]):
                        firstCommitMap[person] = epoch

            if firstCommitFlag == False:
                firstCommitMap[author] = epoch

            # Calculating last commit date for author and storing in dictionary
            lastCommitFlag = False
            for person in lastCommitMap:
                if author.__eq__(person):
                    lastCommitFlag = True
                    if int(epoch) < int(lastCommitMap[person]):
                        lastCommitMap[person] = epoch

            if lastCommitFlag == False:
                lastCommitMap[author] = epoch

# Printing
for owner in authorToNumberOfCommitsMap:
    if owner.__eq__("test"):
        print("Author Contributions: ")
    else: 
        print(owner, ",", authorToNumberOfCommitsMap[owner], ",", strftime('%Y-%m-%d %H:%M:%S', localtime(int(lastCommitMap[owner]))), ",", strftime('%Y-%m-%d %H:%M:%S', localtime(int(firstCommitMap[owner]))))