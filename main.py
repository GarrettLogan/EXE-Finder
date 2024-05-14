import os
import tkinter as tk
from tkinter import ttk
from subprocess import Popen


def find_exe_files(path):
    # This function will search for .exe files in the given path and its subdirectories
    executable_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.exe'):
                executable_files.append(os.path.join(root, file))
    return executable_files


def launch_exe(file_path):
    # This function will launch the .exe file
    Popen(file_path, shell=True)


def app():
    # Create the GUI
    root = tk.Tk()
    root.title('EXE Launcher')

    # Frame for Listbox and scrollbar
    mainframe = tk.Frame(root)
    mainframe.pack(padx=10, pady=10)

    # Scrollbar
    scrollbar = tk.Scrollbar(mainframe, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Listbox
    listbox = tk.Listbox(mainframe, yscrollcommand=scrollbar.set, width=50, height=15)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Configure scrollbar
    scrollbar.config(command=listbox.yview)

    # Find (using find_exe_files function) and add exe files to the listbox
    exe_files = find_exe_files('C:/')  # 'C:/' Is the directory that is being searched, if you want to search multiple drives, modify for use with list
    for exe_file in exe_files:
        listbox.insert(tk.END, exe_file)

    # Button to launch the selected file
    launch_button = ttk.Button(root, text='Launch', command=lambda: launch_exe(listbox.get(tk.ACTIVE)))
    launch_button.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    app()
