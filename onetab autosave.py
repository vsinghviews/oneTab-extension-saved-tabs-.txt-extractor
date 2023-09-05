import pyautogui
import time
import os
import pyperclip

#Opening onetab user interface
onetabbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\onetabbutton.png', confidence=0.9)
print(onetabbutton)
pyautogui.moveTo(onetabbutton)
pyautogui.rightClick(onetabbutton)

dropdownbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\onetabdropdown.png', confidence=0.5)
pyautogui.moveTo(dropdownbutton)
print(dropdownbutton)

time.sleep(5)

displaydropdownbutton = pyautogui.locateCenterOnScreen('d:\\desktop\\usb\\overload\\images\\displayonetab drop down.png', confidence=0.4)
pyautogui.moveTo(displaydropdownbutton)
print(onetabbutton)
pyautogui.click(displaydropdownbutton)

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
pyautogui.moveTo((exportURLsbutton), duration=1)
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
    filename = f"example.{counter}.txt"
    counter += 1

with open(filename, "w", encoding="utf-8") as newfile:
    newfile.write(pyperclip.paste())    



