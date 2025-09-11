while True:
    raw = input("vfs> ")
    cmd, *args= raw.split()
    print(cmd)
    if cmd == "exit":
        break

    if cmd == "ls":
        print(cmd, args)
    if cmd == "cd":
        print(cmd, args)
