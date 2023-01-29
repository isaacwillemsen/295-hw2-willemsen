import sys
import subprocess

print("Script being run: ", sys.argv[0])
print("Argument passed: ", sys.argv[1])

cmd = ('git', 'cat-file', '-p', sys.argv[1])
process = subprocess.run(cmd, capture_output=True, text=True)

output = process.stdout

tree = output.split("\n")[0][5:]

print(tree)