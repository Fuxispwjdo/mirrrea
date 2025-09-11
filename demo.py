# Вариант 40
import  os
def expand(s:str):
    for k in os.environ:
        s = s.replace("$"= k, os.environ[k])
        return s

while True:
    raw = expand(input("vfs> "))
    cmd, *args= raw.split()
    if cmd == "exit":
        break

    if cmd == "ls":
        print(cmd, args)
    if cmd == "cd":
        print(cmd, args)
