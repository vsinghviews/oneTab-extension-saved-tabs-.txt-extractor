import pyautogui
import time
import os
import pyperclip

onetabbutton = pyautogui.locateCenterOnScreen('d:\\desktop\windowsave.png', confidence = 0.9)
print(onetabbutton)
pyautogui.moveTo(onetabbutton)
pyautogui.rightClick(onetabbutton)
pyautogui.moveTo((1789, 104), duration=1)
pyautogui.click((1525, 120), duration=1)

time.sleep(5)

eibutton = pyautogui.locateCenterOnScreen('d:\\desktop\exportimportURLs.png', confidence = 0.5)
print(eibutton)
pyautogui.moveTo((eibutton), duration=1)
pyautogui.click(eibutton)

exportURLsbutton = pyautogui.locateCenterOnScreen('d:\\desktop\exportURLs button.png', confidence = 0.9)
print(exportURLsbutton)
pyautogui.moveTo((exportURLsbutton), duration=1)
pyautogui.click(exportURLsbutton)

exportBox = pyautogui.locateCenterOnScreen('d:\\desktop\exportBox.png', confidence = 0.9)
print(exportBox)
pyautogui.click(exportBox)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

time.sleep(5)

filename = "example.txt"
counter = 1

while os.path.exists(filename):
    filename = f"example.{counter}.txt"
    counter += 1

with open(filename, "w", encoding="utf-8") as newfile:
    newfile.write(pyperclip.paste())    



