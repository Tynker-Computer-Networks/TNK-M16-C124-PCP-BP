import time
# Required library
from pynput import keyboard
from pynput.keyboard import Key, Listener

# Global text variable to store the key values
text = ""

# Function to store the key logs in txt file
def writeToLog(text):
    with open("keylog.txt", "a") as f:
        f.write(text)

# Function to handle key release
def onRelease(key):
    if key == Key.esc:
        return False
    
# Define function onPress to handle key press 



def typingSpeedTest():
    text = "The quick brown fox jumps over the lazy dog\n"
    print("Type this sentence as fast as you can:\n\n", text)

    input("Press Enter when you're ready to start...")
    startTime = time.time()

    userInput = input("Type the sentence here: ")
    # Add  listener to listen onPress and onRelease key events
    # Move the userInput inside the listner

    endTime = time.time()
    totalTime = endTime - startTime
    
    words = text.split()
    numWords = len(words)
    numChars = len(text)
    wpm = (numWords / totalTime) * 60

    correctChars = sum(1 for x, y in zip(text, userInput) if x == y)
    accuracy = (correctChars / numChars) * 100

    print("\nResults:")
    print("Time taken: {:.2f} seconds".format(totalTime))
    print("Your typing speed: {:.2f} WPM".format(wpm))
    print("Accuracy: {:.2f}%".format(accuracy))


typingSpeedTest()
