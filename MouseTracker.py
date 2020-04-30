from pynput.mouse import Listener #Pynput library is a library that enables us to control the input streams (like keyboard and mouse)

##WHILE THE PROGRAM IS RUNNING, THIS FUNCTION WILL SAVE MOUSE COORDINATES
def write_to_file(x,y):
    mouse_report = "Mouse position: {0} ".format((x,y))

    ##WE CREATE A MOUSELOG.TXT FILE TO RECORD OUR MOUSE MOVEMENTS
    with open("MouseLog.txt", 'a') as f:
        f.write(mouse_report + "\n")

##WHILE THE PROGRAM IS RUNNING, THIS FUNCTION WILL DETECT MOUSE ACTIONS
with Listener(on_move=write_to_file) as l:  # Detects the key that was pressed and returns it to the write_to_function to save it.
    l.join()