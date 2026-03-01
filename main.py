import os

for f in os.scandir("DemoRepository"):
    print(f.name)
