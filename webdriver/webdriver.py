from appium import webdriver
import time


class Driver:
    def __init__(self, config):

        self.run_location = config.run_location
        self.desired_caps = config.desired_capabilities
        self.obtain_device()

    def obtain_device(self):

        raised = True
        seconds_tried = 0
        wait_time = 120

        while raised and seconds_tried <= wait_time:
            try:

                webdriver.Remote(self.run_location, self.desired_caps)

                raised = False
                print("Webdriver: Done waiting for device: Device Obtained")

            except Exception as e:
                time.sleep(5)
                seconds_tried += 5
                print(e)
                print(
                    "Trying device again shortly. Currently waited: "
                    + str(seconds_tried)
                )

        if raised:
            print("Webdriver: Done waiting for device: device NOT obtained")
            raise

