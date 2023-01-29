import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Argument passed: ", sys.argv[1])
print("")

cmd = ('git', 'log', '-1', sys.argv[1])
process = subprocess.run(cmd, capture_output=True, text=True)

output = process.stdout

author = output.split("\n")[1]
hash = output.split("\n")[0][6:]

with open(sys.argv[1]) as f:
    lines = f.readlines()

print(author)
print("")
print("SHA-1 for", sys.argv[1], hash)
print("")
for str in lines:
    print(str)