import pyautogui
import time
import os
import pyperclip

#Opening onetab user interface
onetabbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\onetabbutton.png', confidence=0.9)
print(onetabbutton)
pyautogui.moveTo(onetabbutton)
pyautogui.rightClick(onetabbutton)
pyautogui.moveTo((1789, 104), duration=1)
pyautogui.click((1525, 120), duration=1)

#Pausing state so that the export button can be found
time.sleep(5)

#Opening saved tabs .txt list
exportimportbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\exportimportURLs.png', confidence=0.9)
print(exportimportbutton)
pyautogui.moveTo((exportimportbutton), duration=0.5)
pyautogui.click(exportimportbutton)

#Locating saved tabs
exportURLsbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\exportURLs button.png', confidence = 0.9)
print(exportURLsbutton)
pyautogui.moveTo((exportURLsbutton), duration=0.5)
pyautogui.click(exportURLsbutton)

#Exporting saved tabs to notepad to be saved as file
txtBox = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\exportBox.png', confidence = 0.9)
print(txtBox)
pyautogui.click(txtBox)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

time.sleep(5)

filename = "Overload.txt"
counter = 1

while os.path.exists(filename):
    filename = f"Overload.{counter}.txt"
    counter += 1

with open(filename, "w", encoding="utf-8") as newfile:
    newfile.write(pyperclip.paste())    



