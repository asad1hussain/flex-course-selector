import cv2
import numpy as np
import pyautogui
import time
filename = input("Enter the filename (including extension, e.g., agile.jpg): ")
threshold = float(input("Enter the threshold "))
shift_amount= input("Enter the shift amount ")
pakka=int(input('1 if pakka 0 if not sure'))
# Load the logo images for detection
available_buttonRS = cv2.imread(filename)
available_buttonDEVOPS = cv2.imread(filename)


# Set the threshold for template matching

shift_amount = int(shift_amount)+535
n=5
# Switch to the target application
pyautogui.hotkey('alt', 'tab')

while True:
    # Refresh the webpage
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(1.9)  # Adjust the waiting time as needed

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to OpenCV format
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Perform template matching for RS
    result_availableRS = cv2.matchTemplate(screenshot_cv, available_buttonRS, cv2.TM_CCOEFF_NORMED)
    _, max_valRS, _, max_locRS = cv2.minMaxLoc(result_availableRS)

    # Perform template matching for DEVOPS
    result_availableDEVOPS = cv2.matchTemplate(screenshot_cv, available_buttonDEVOPS, cv2.TM_CCOEFF_NORMED)
    _, max_valDEVOPS, _, max_locDEVOPS = cv2.minMaxLoc(result_availableDEVOPS)


    # Check if the "available" button is detected
    if max_valRS >= threshold:
        print("RS is available! Clicking and confirming order...")
        #Perform a left click on the logo's detected position
        pyautogui.click(max_locRS[0] + available_buttonRS.shape[1] / 2 + shift_amount + 135, max_locRS[1] + available_buttonRS.shape[0] / 2)
        time.sleep(0.1)
        # # Simulate pressing Enter twice
        if (pakka==1):
            pyautogui.press('enter')
            time.sleep(0.1)
            pyautogui.press('enter')
        #Exit the loop after action is performed
        n=1
        break
    elif max_valDEVOPS >= threshold:
        print("DEVOPS is available! Clicking and confirming order...")
        # Perform a left click on the logo's detected position
        pyautogui.click(max_locRS[0] + available_buttonRS.shape[1] / 2 + shift_amount + 135, max_locRS[1] + available_buttonRS.shape[0] / 2)
        time.sleep(0.1)
        # # # Simulate pressing Enter twice
        if (pakka==1):
            pyautogui.press('enter')
            time.sleep(0.1)
            pyautogui.press('enter')
        # Exit the loop after action is performed
        n=2
        break
    elif max(max_valRS, max_valDEVOPS) < -0.1:
        print("No matching logos found. Exiting...")
        n=3
        break
    print("for RS:")
    print(max_valRS)
    print("for DEVOPS:")
    print(max_valDEVOPS)
    
# Print results
print("Action completed.")
print("for RS:")
print(max_valRS)
print("for DEVOPS:")
print(max_valDEVOPS)
# Switch back to the previous application
#pyautogui.hotkey('alt', 'tab')
time.sleep(3)
