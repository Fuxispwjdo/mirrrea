import  os
import tkinter as tk
from tkinter import scrolledtext


def expand(s:str):
    for k in os.environ:
        s = s.replace(f'${k}', os.environ[k])
    return s

def simple_parser(input_str):
    parts = input_str.split()
    return parts[0], parts[1:] if len(parts) > 1 else []

class SimpleVFS:
    def __init__(self, root):
        self.root = root
        self.root.title("VFS")
        self.root.geometry("600x400")
        
        # Поле ввода
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        self.entry.bind('<Return>', self.execute_command)
        
        # Область вывода
        self.output = scrolledtext.ScrolledText(root, width=70, height=20)
        self.output.pack(pady=5)
        
        # Кнопка выполнения
        self.btn = tk.Button(root, text="Выполнить", command=self.execute_command)
        self.btn.pack()
        
    def execute_command(self, event=None):
        command = self.entry.get().strip()
        if not command:
            return
            
        self.entry.delete(0, tk.END)
        self.output.insert(tk.END, f"vfs> {command}\n")
        
        try:
            expanded_cmd = expand(command)
            cmd, args = simple_parser(expanded_cmd)
            
            if cmd == "exit":
                self.root.quit()
            elif cmd == "ls":
                path = args[0] if args else "."
                files = os.listdir(path)
                for file in files:
                    self.output.insert(tk.END, f"{file}\n")
            elif cmd == "cd":
                if args:
                    os.chdir(args[0])
                self.output.insert(tk.END, f"Текущая директория: {os.getcwd()}\n")
            else:
                self.output.insert(tk.END, f"Неизвестная команда: {cmd}\n")
                
        except Exception as e:
            self.output.insert(tk.END, f"Ошибка: {str(e)}\n")
            
        self.output.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleVFS(root)
    root.mainloop()
