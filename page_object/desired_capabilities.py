class DesiredCapabilities(object):
    EMULATOR_ANDROID = {
        "platformName": "Android",
        "automationName": "UIAutomator2",
        "platformVersion": "10",
        "udid": "emulator-5554",
        "deviceName": "Pixel 3A",
        "appPackage": "com.classpass.classpass.dev",
        "appActivity": "com.classpass.classpass.appstart.viewcontrollers.activities.SplashScreenActivity",
        "autoGrantPermissions": True,
        "newCommandTimeout": 60,
        "systemPort": 8201
    }

    MAC_MINI_LOCAL_IPHONE_XR = {
        "platformName": "iOS",
        "xcodeSigningId": "Classpass Inc.",
        "udid": "00008020-001D15DC2691002E",
        "automationName": "XCUITest",
        "deviceName": "iPhone",
        "bundleId": "com.classpass.classpass",
        "platformVersion": "14.4",
        "agentPath": "/usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj",
        "newCommandTimeout": 360,
    }

    MAC_MINI_LOCAL_SAMSUNG_S6 = {
        "platformName": "Android",
        "automationName": "UIAutomator2",
        "platformVersion": "7",
        "udid": "0815f83444d83304",
        "deviceName": "samsung SM-G920F",
        "appPackage": "com.classpass.classpass",
        "appActivity": "com.classpass.classpass.appstart.viewcontrollers.activities.SplashScreenActivity",
        "newCommandTimeout": 60,
        "systemPort": 8201
    }

    KOBITON_SAMSUNG_S6 = {
        # The generated session will be visible to you only.In case you want this session available for other users, please assign this device to specific group.
        'sessionName': 'Automation test session',
        'sessionDescription': '',
        'deviceOrientation': 'portrait',
        'noReset': True,
        'fullReset': False,
        'captureScreenshots': True,
        'autoGrantPermissions': False,
        'locationServicesAuthorized': False,
        # The maximum size of application is 500MB
        # By default, HTTP requests from testing library are expired
        # in 2 minutes while the app copying and installation may
        # take up-to 30 minutes. Therefore, you need to extend the HTTP
        # request timeout duration in your testing library so that
        # it doesn't interrupt while the device is being initialized.
        'app': 'kobiton-store:188846',
        'deviceGroup': 'ORGANIZATION',
        # For deviceName, platformVersion Kobiton supports wildcard
        # character *, with 3 formats: *text, text* and *text*
        # If there is no *, Kobiton will match the exact text provided
        'deviceName': 'Galaxy S6',
        # The tag is used for finding devices and the user can input only one tag.
        # For example, the data value will be inputted: tagName="TagName1"
        'tagName': '',
        'platformName': 'Android',
        'platformVersion': '7.0'
    }
