import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Filename passed: ", sys.argv[1])
print("")

for commit in sys.argv[1:]:
    cmd = ('git', 'log', '--name-only', commit)
    process = subprocess.run(cmd, capture_output=True, text=True)
    output = process.stdout
    filesChanged = output.split("\n")[7:]
    for line in filesChanged:
        print(line)
        if line == sys.argv[1]:
            print("YAY")


