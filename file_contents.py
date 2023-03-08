import re
import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Argument passed: ", sys.argv[1])
print("")

getTree = ('git', 'cat-file', '-p', 'main')

process1 = subprocess.run(getTree, capture_output=True, text=True)
output1 = process1.stdout

tree = output1.split("\n")[0][5:]
author = output1.split("\n")[2][7:]
print(author)
print("")

getSha1ForFile = ('git', 'cat-file', '-p', tree)
process2 = subprocess.run(getSha1ForFile, capture_output=True, text=True)
output2 = process2.stdout

shas = output2.split("\n")
for s in shas:
    if re.search(sys.argv[1], s):
        sha1 = s[12:52]
        print("SHA-1 for", sys.argv[1], sha1)
        print("")

with open(sys.argv[1]) as f:
    lines = f.readlines()

for str in lines:
    print(str)