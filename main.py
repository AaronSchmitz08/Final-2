from gui import *


"""
Sets the window size, prevents resizing, and names it
than it makes a gui object and runs it
"""
def main():
    window = Tk()
    window.title("final")
    window.geometry("350x230")
    window.resizable(False,False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()