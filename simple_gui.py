import tkinter as tk
import webbrowser
import os
from functools import partial

TITLE = "Simple-GUI Automation"
WIDTH = 35

def get_button_data():
    with open("Buttons.txt") as f:
        data = f.readlines()
    assert len(data) > 0 

    Buttons = {}
    
    for button in data:
        button, url = button.split(", ")
        url = url.strip('\n')
        Buttons[button] = url 

    return Buttons

def delete_button(index):
    index -= 1 
    with open("Buttons.txt") as f:
        data = f.readlines()
    
    data.pop(index)

    with open("Buttons.txt", "w") as f:
        f.writelines(data)
    
def edit_button(index, name, url):
    index -= 1 
    with open("Buttons.txt") as f:
        data = f.readlines()
    
    button = data[index]
    button = button.split(", ")
    if name == "" and url != "":
        button[1] = url 
    
    elif name != "" and url == "":
        button[0] = name 

    else:
        button[0] = name 
        button[1] = url 
    
    button = ', '.join(button)
    data[index] = button 
    with open("Buttons.txt", "w") as f:
        f.writelines(data)
    
def add_button(name, url):
    button = ", ".join([name, url])
    with open("Buttons.txt", 'a') as f:
        f.write(f'\n{button}')

def send_notification(msg):
    os.system(f'notify-send "{TITLE}" "{msg}"')

def open_link(link):
    send_notification(f"Opening {link}")
    webbrowser.open(link)

def app():
    buttons_data = get_button_data()
    app = tk.Tk()
    app.title(TITLE)

    buttons_tk = []
    i = 1 
    for button in buttons_data:
        buttons_tk.append(tk.Button(app, text=f'{i}: {button}', width=WIDTH, command=partial(open_link, buttons_data[button])))
        i += 1
    
    #Pack Buttons
    for i in range(len(buttons_tk)):
        buttons_tk[i].pack()


    app.mainloop()

def breakline():
    print("-"*60)

def print_buttons():
    print("Current Buttons: ")
    for index, val in enumerate(get_button_data()):
        print(f'{index+1}: {val}')

def main(): 
    os.system("clear")

    breakline()
    print(TITLE)
    breakline()

    print("1) Launch the app.")
    print("2) Edit a button's label/url")
    print("3) Delete a button.")
    print("4) Add a button.")
    print("5) Exit.")
    print()
    breakline()
    choice = int(input("Your choice: "))

    if choice == 1:
        app()
    elif choice == 2:
        print_buttons()        
        print("Press Enter to keep the original value.") 
        index = input("Enter the button's index: ")
        name = input("Enter the button's new name: ")
        url = input("Enter the button's new url: ")
        edit_button(int(index), name, url)
    elif choice == 3:
        print_buttons()
        index = input("Edit a button's label/urindex: ")
        delete_button(int(index))
    elif choice == 4:
        name = input("Enter the new button's name: ")
        url = input("Enter the url for the new button: ")
        add_button(name, url)

    if choice in range(1, 5):
        main()

    elif choice == 5:
        os.system("clear")
        exit()
    else:
        raise Exception("Wrong Choice.")

if __name__ == "__main__":
    main()