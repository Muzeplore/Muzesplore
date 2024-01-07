import tkinter as tk

# creating windows ;)

class general(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Muzeplore Home", font=("Arial",50), height=10)
        title.pack()

# root window / packing

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1920x1080")
    root.attributes("-fullscreen", True)
    root.title("Muzeplore Home")

    general(root).pack()
    root.mainloop()