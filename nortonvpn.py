#from appium import webdriver # type: ignore
#from appium import webdriver
#from appium import webdriver as appium_webdriver
from appium.webdriver import Remote
from time import sleep
# Set up desired capabilities for the mobile app
desired_caps = {
    
    "platformName": "Android",  # Use "iOS" if you're testing on an iPhone
    "platformVersion": "15.0",  # Specify your Android/iOS version
    "deviceName": "Jolly's F54",  # Device name, replace with your device
    "appPackage": "com.norton.vpn",  # Package name of the Norton VPN app
    "appActivity": "com.norton.vpn.MainActivity",  # Main activity of the app
    "automationName": "UiAutomator2"  # For Android
    #"noReset": True
}
# Start the Appium WebDriver session
#driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver = Remote("http://localhost:4723/wd/hub", desired_caps)

sleep(2)
    # Find and click the "Get Started" button
get_started_button = driver.find_element_by_xpath("//android.widget.Button[@text='Get started']")
get_started_button.click()
sleep(3)  # Wait for the next page
# Run the page navigation
navigate_pages() # type: ignore

# Close the session after navigation
driver.quit()