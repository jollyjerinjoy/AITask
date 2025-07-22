from appium.webdriver import Remote
from appium.options.android import UiAutomator2Options
from time import sleep

# Step 1: Define Appium options using UiAutomator2Options (for Android)
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "15")  # Update as per your device
options.set_capability("deviceName", "RZCW50TA3QK")  # Optional: just make sure USB debugging is ON
options.set_capability("appPackage", "com.symantec.securewifi")
#options.set_capability("appActivity", "com.symantec.securewifi.ui.main.MainActivity")
options.set_capability("appActivity", "com.symantec.securewifi.ui.MainActivity")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("noReset", True)

# Step 2: Start Appium session
driver = Remote(command_executor="http://localhost:4723", options=options)

# Step 3: Wait and click "Get started"
sleep(3)

get_started_button = driver.find_element("xpath", "//android.widget.Button[@text='Get started']")

get_started_button.click()

sleep(3)
# Step 4: Optionally wait and close
# Run the page navigation
navigate_pages() # type: ignore
sleep(3)
# Close the session after navigation
driver.quit()
