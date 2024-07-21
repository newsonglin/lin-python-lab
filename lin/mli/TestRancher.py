import pyautogui, time
import pyperclip
from pyautogui import press, typewrite, hotkey

time.sleep(5)

s = pyperclip.paste()
print(s)
with open('D:/aaaa.txt', 'w') as g:
    g.write(s)

# switch ime to English
# pyautogui.moveTo(1706, 1048, duration=0.3)  # move to ime
# pyautogui.click()
#
# pyautogui.moveTo(1648, 789, duration=0.3)  # move to English
# pyautogui.click()

# moves mouse to command end
# pyautogui.moveTo(133, 930, duration=0.3)
# pyautogui.click()
#
# # drag and select
# pyautogui.dragTo(1, 1, 8, button='left')
#
# # move mouse to content area, and copy contents
# pyautogui.moveTo(178, 913, duration=0.3)
# pyautogui.click(button='right')
# pyautogui.moveTo(292, 383, duration=0.3)
# pyautogui.click()

# pyautogui.scroll(-1000)
#pyautogui.moveTo(91, 913, duration=0.3)
#pyautogui.dragTo(284, 894, 1, button='left')
#pyautogui.write('Hello world!', interval=0.25)
#typewrite("kubectl get pods -n mli-qa02  -o custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[0].image")


# pyautogui.hotkey('alt', 'space', interval=0.25)
# pyautogui.press('x')
# pyautogui.moveTo(108, 965, duration=0.3)  # moves mouse to X of 112, Y of 1308.
# pyautogui.click()
# pyautogui.dragTo(106, 926, 1, button='left')

#right click
#move
#left click (copy)