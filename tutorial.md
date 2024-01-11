Typing Speed Test
======================
In this activity, you will code to detect the key press to find out the typing speed of the user.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/d703c548-b1da-4beb-9978-52e80ef77911.gif" width = "auto" height = "auto">


Follow the given steps to complete this activity.


1. Define a function `onPress()` that appends characters to the `text` string based on the key pressed from the keyboard.
   * Open the file `main.py`.
    * Define a global variable `text` that will hold the text entered by the user.
    ```
    text = ''
    ```
   * Define `onPress()` function that takes one parameter `key` i.e key entered by the user and access global `text` variables in it
    ```
    def onPress(key):
        global text
    ```
    * Use `keyboard.key` to check if the entered `key` is a special character and perform actions accordingly.
    * If the pressed key is `enter`, `tab`, `space` then append '/n', '/t' , ' ' special characters respectively.
    * If pressed key is `shit`, `shift_r`, `cmd`, `cmd_r`, `ctrl`, `ctrl_r` then `pass`
    * If `backspace` is pressed then check if `text` is empty or not before removing the last character.
    * return `False` if escape is pressed.
    ```
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.shift_r:
            pass
        elif key == keyboard.Key.cmd:
            pass
        elif key == keyboard.Key.cmd_r:
            pass
        elif key == keyboard.Key.backspace and len(text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.esc:
            return False
    ```
    * If not a special key then append that key character to the `text`
    ```
        else:
            text += str(key).strip("'")  
        print(text)
    ```
    * Call `writeToLog(text)` function to store the text in a `.txt` file
    ```
        writeToLog(text)
    ```
2. Create a listener to listen for key presses and call `onPress()` or `onRelease()` to register the key presses by the keylogger.
   * Create a listener that calls `onPress` and `onRelease` functions on `on_press` and `on_release` events respectively.
   * Move taking user input in `userInput` variable inside the listener.
    ```
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        userInput = input("Type the sentence here: ")
        listener.join()
    ```




Save and run the code to check the output.
