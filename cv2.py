import cv2 # type: ignore

import numpy as np
from appium.webdriver.common.touch_action import TouchAction # type: ignore
import base64

def find_element_using_image(image_path):
    # Take a screenshot of the current screen
    screenshot = driver1.get_screenshot_as_base64() # type: ignore
    nparr = np.frombuffer(base64.b64decode(screenshot), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Load the template image
    template = cv2.imread(image_path)
    
    # Match the template (using OpenCV)
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    
    return max_loc

def tap_on_element(image_path):
    # Find the element using image recognition
    element_position = find_element_using_image(image_path)
    
    # Perform the tap action on the element
    action = TouchAction(driver1) # type: ignore
    action.tap(x=element_position[0], y=element_position[1]).perform()