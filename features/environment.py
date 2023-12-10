from appium import webdriver
from appium.options.android import UiAutomator2Options
from app.application import Application
import subprocess
import time


def mobile_driver_init(context, scenario_name):
    """
    :param context: Behave context
    """
    desired_capabilities = {
        "platformName": "Android",
        "automationName": 'uiautomator2',
        "platformVersion": "10",
        "deviceName": "Android Emulator",
        "appActivity": "org.wikipedia.main.MainActivity",
        "appPackage": "org.wikipedia",
        # Put your path below:
        "app": "C:/Users/noahsj/MYpython-appium-automation/mobile_app/wikipedia.apk"
    }

    appium_server_url = 'http://localhost:4723'
    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

    context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    context.driver.implicitly_wait(5)

    context.app = Application(context.driver)


def reset_emulator(context):
    # Clear app data using ADB shell commands
    package_name = "org.wikipedia"  # Replace with your app's package name
    emulator_serial = "emulator-5554"  # Replace with your emulator's serial

    # Stop the app
    subprocess.run(["adb", "-s", emulator_serial, "shell", "am", "force-stop", package_name])

    # Clear app data
    subprocess.run(["adb", "-s", emulator_serial, "shell", "pm", "clear", package_name])

    # Start the app (adjust the app activity and package name if needed)
    subprocess.run(
        ["adb", "-s", emulator_serial, "shell", "am", "start", "-n", f"{package_name}/org.wikipedia.main.MainActivity"])

    time.sleep(10)  # Adjust sleep time based on your environment


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f'{step}.png')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
    reset_emulator(context)

