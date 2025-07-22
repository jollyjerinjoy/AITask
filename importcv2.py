import cv2
import numpy as np
from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.actions.action_builder import ActionBuilder # type: ignore
from appium.webdriver.common.actions.pointer_input import PointerInput # type: ignore
from PIL import Image # type: ignore
import io

# Step 1: Setup Appium Options
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "15")  # Update as needed
options.set_capability("deviceName", "RZCW50TA3QK")  # Your device ID
options.set_capability("appPackage", "com.symantec.securewifi")
options.set_capability("appActivity", "com.symantec.securewifi.ui.MainActivity")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("noReset", True)

# Step 2: Start the driver
driver = webdriver.Remote("http://localhost:4723", options=options)

# Step 3: Find element on screen using image recognition
def find_element_using_image(image_path):
    # Take a screenshot from the device
    screenshot = driver.get_screenshot_as_png()
    screen_np = np.array(Image.open(io.BytesIO(screenshot)))
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

    # Load the template image
    template = cv2.imread(image_path)
    if template is None:
        raise Exception(f"Image not found: {image_path}")

    result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8
    if max_val < threshold:
        raise Exception("Image not found on screen")

    return max_loc  # (x, y)

# Step 4: Perform tap using W3C Actions
def tap_on_element(image_path):
    x, y = find_element_using_image(image_path)

    # Create touch input and perform tap
    touch_action = ActionBuilder(driver)
    finger = PointerInput(PointerInput.TOUCH, "finger1")
    touch_action.add_action(finger.create_pointer_move(duration=0, x=x+5, y=y+5, origin='viewport'))
    touch_action.add_action(finger.create_pointer_down(PointerInput.LEFT))
    touch_action.add_action(finger.create_pointer_up(PointerInput.LEFT))
    touch_action.perform()

# Step 5: Run it
sleep(5)  # Give the app time to load
tap_on_element("get_started_image.png")  # Your reference button image
sleep(3)

# Step 6: Close driver
driver.quit()