from appium import webdriver
from time import sleep

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15.0",
    "deviceName": "RZCW50TA3QK",  # Replace with your actual device ID from adb devices
    "appPackage": "com.norton.vpn",
    "appActivity": "com.norton.vpn.MainActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723", desired_caps)

sleep(2)

# Find and click "Get started"
get_started_button = driver.find_element_by_xpath("//android.widget.Button[@text='Get started']")
get_started_button.click()

sleep(3)

driver.quit()
