import  os
def expand(s:str):
    for k in os.environ:
        s = s.replace(f'${k}', os.environ[k])
    return s

def simple_parser(input_str):
    parts = input_str.split()
    return parts[0], parts[1:] if len(parts) > 1 else []

while True:
    raw = expand(input("vfs> "))
    cmd, *args= raw.split()
    if cmd == "exit":
        break

    elif cmd == "ls":
        print(cmd, args)
    elif cmd == "cd":
        print(cmd, args)
    else:
        print(f"Неизвестная команда: {cmd}")
