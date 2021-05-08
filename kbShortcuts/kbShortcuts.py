import keyboard, json

keyboard.unhook_all()

def setHotkey(key, action):
    keyboard.add_hotkey(key, lambda: keyboard.write(action)) 


with open("shortcuts.json", "r", encoding="utf-8") as jfile:
    data = json.load(jfile)

    
    temp = "| %s |"%(data["endProgram"])
    while len(temp)< 8:
        temp = temp.replace(" |", "  |")
    print("#" + "-"*(len(temp)-2) + "#")
    print("| end: " + " "*(len(temp)-8) + "|")
    print(temp)
    print("#" + "-"*(len(temp)-2) + "#\n")


    for i in range(len(data["shortcuts"])):
        item = data["shortcuts"][i]
        if item[0] == "" or item[1] == "":
            continue

        if i != 0:
            print("-"*20)
        setHotkey(item[0], item[1])

        print("key: \"%s\""%item[0])
        print("sentence: \"%s\""%item[1])
    keyboard.wait(data["endProgram"]) 

