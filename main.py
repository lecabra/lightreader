import tkinter as tk
import glob
import reader
import os

def main():

    root = tk.Tk()
    root.title("LightReader v0.1 - Choose a folder")
    root.geometry("500x650")
    root.resizable(False, False)

    folders = glob.glob("lib/*", recursive=False)
    buttons = {}

    for i in range(len(folders)):

        name = folders[i]

        def folder_selected(x = folders[i]):
            global chose
            chose = x

            root.destroy()

            lr = reader.LightReader(x+'/')
            lr.mainloop()
            

        buttons[i] = tk.Button(root, text = name[4:], command = folder_selected)
        
        # 3 buttons in a row
        if i % 3 == 0:
            buttons[i].grid(row = i // 3, column = 0)
            buttons[i].config(width = 20)
        elif i % 3 == 1:
            buttons[i].grid(row = i // 3, column = 1)
            buttons[i].config(width = 20)
        else:
            buttons[i].grid(row = i // 3, column = 2)
            buttons[i].config(width = 20)
        

    root.mainloop()


if __name__ == '__main__':

    if not os.path.exists("lib"):
        os.makedirs("lib")
        print('Created lib folder! Add images to it!')

    main()