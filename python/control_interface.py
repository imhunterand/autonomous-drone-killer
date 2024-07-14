import tkinter as tk
from communication import send_data

def control_drone():
    root = tk.Tk()
    root.title("Drone Control Interface")

    def fire_command():
        send_data(0, 0, 1)

    fire_button = tk.Button(root, text="Fire", command=fire_command)
    fire_button.pack()

    root.mainloop()

if __name__ == "__main__":
    control_drone()
