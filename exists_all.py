import os
import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Filename passed: ", sys.argv[1])
print("")


result = False
for commit in sys.argv[2:]:

    firstTwo = commit[0:2]
    lastBit = commit[2:]
    l = [".git/objects/", firstTwo, "/", lastBit]
    filename = ''.join(l)
    exists = os.path.exists(filename)
    
    if exists == False:
        print(commit, "is not a valid git object")
        break

    cmd = ('git', 'log', '--name-only', commit, '-1')
    process = subprocess.run(cmd, capture_output=True, text=True)
    output = process.stdout
    filesChanged = output.split("\n")
    for line in filesChanged:
        if line == sys.argv[1]:
            result = True
            break
    if result == False:
        break

print(result)


