import keyboard  # using module keyboard


class Interface:
    def __init__(self):
        print("***************************************************")
        print("Cette application peut réaliser 3 actions")
        print("[1] Web scrapper un site web")
        print("[2] Web scrapper un site web")
        print("[3] Web scrapper un site web")
        print("pour quitter, appuyez sur q")
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
            except:
            break  # if user pressed a key other than the given key the loop will break
