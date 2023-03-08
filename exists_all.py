import os
import re
import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Filename passed: ", sys.argv[1])
print("")


result = False
for commit in sys.argv[2:]:

    checkObjectType = ('git', 'cat-file', '-t', commit)
    process1 = subprocess.run(checkObjectType, capture_output=True, text=True)
    output1 = process1.stdout
    if output1.__eq__("commit"):
        print(commit, "is a", output1, "object, not a commit object")

    firstTwo = commit[0:2]
    lastBit = commit[2:]
    l = [".git/objects/", firstTwo, "/", lastBit]
    filename = ''.join(l)
    exists = os.path.exists(filename)
    
    if exists == False:
        print(commit, "is not a valid git object")
        break

    getTree = ('git', 'cat-file', '-p', commit)
    process2 = subprocess.run(getTree, capture_output=True, text=True)
    output2 = process2.stdout

    tree = output1.split("\n")[0][5:]

    getSha1ForFile = ('git', 'cat-file', '-p', tree)
    process3 = subprocess.run(getSha1ForFile, capture_output=True, text=True)
    output3 = process3.stdout

    filesChanged = output3.split("\n")
    for line in filesChanged:
        if re.search(sys.argv[1], line):
            result = True
            break
        if result == False:
            break

print(result)


