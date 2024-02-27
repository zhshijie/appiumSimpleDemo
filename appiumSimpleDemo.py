
import unittest
import os
from appium import webdriver
from time  import sleep


class  appiumSimpleTezt (unittest.TestCase):

	def  setUp(self):
		app = os.path.abspath('/Users/zhangshijie/Desktop/demo/appiumSimpleDemo/build/Debug-iphoneos/appiumSimpleDemo.app')

		self.driver = webdriver.Remote(
			command_executor = 'http://127.0.0.1:4723/wd/hub',
			desired_capabilities = {
				'app':app,
				'platformName': 'iOS',
				'platformVersion': '10.2.1',
				'deviceName': 'iPad',
				'bundleId': 'com.test.appiumSimpleDemo',
				'udid': '9417217ac6ab33c0a85f799241e2ab2d3acd2447'
			}
			)

	def test_push_view(self):
		


		next_view_button = self.driver.find_element_by_accessibility_id("entry next view")
		next_view_button.click()

		sleep(2)

		back_view_button = self.driver.find_element_by_accessibility_id("Back")
		back_view_button.click()

	def tearDown(self):
		sleep(1)
		# self.driver.quit()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(appiumSimpleTezt)
	unittest.TextTestRunner(verbosity=2).run(suite)
