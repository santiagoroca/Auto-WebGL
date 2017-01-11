import sys
import time
import atexit
import argparse

from time import sleep

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class autogl_config():
        def __init__(self):
                self.config = {
                        "url": ""
                }

        def configurate(self, config):
                self.config.update(config)

        def getUrl(self):
                return self.config['url']

autoglconfig = autogl_config()

#Set Capture to its default false
capture = False

parser = argparse.ArgumentParser()
parser.add_argument("--capture", help="captures test data", action="store_true")
args = parser.parse_args()

if args.capture:
    capture = True

print('\n	\033[4m\033[1mWebGL Automated\033[0m\n')
	
class autogl:

	def __init__(self):
		self.passed = 0
		self.errored = 0

	def should(self, case_description):
		comparison = self.compare('temp/' + case_description + '.png', 'cases/' + case_description + '.png');

		if comparison[1] <= 100.0:
			print_should_sucess(case_description)
			self.passed+=1
		else:
			self.errored+=1
			print_should_error(case_description)


	def compare(self, img1, img2):
		img1 = self.to_grayscale(imread(img1).astype(float))
		img2 = self.to_grayscale(imread(img2).astype(float))    

		img1 = self.normalize(img1)
		img2 = self.normalize(img2)

		diff = img1 - img2
		m_norm = sum(abs(diff))
		z_norm = norm(diff.ravel(), 0)

		return (m_norm, z_norm)
	
	def normalize(self, img):
		rng = img.max()-img.min()
		amin = img.min()

		return (img-amin)*255/rng

	def to_grayscale(self, img):
		if len(img.shape) == 3:
			return average(img, -1) 
		else:
			return img 



class autogl_browser:

	def __init__(self, browser):
		self.browser = browser

	def mouseDownAt(self, x, y, target):
		self.browser.execute_script('document["dispatchMouseDownEvent"]({}, {}, {});'.format(x, y, target))

	def mouseUpAt(self, x, y, target):
		self.browser.execute_script('document["dispatchMouseUpEvent"]({}, {}, {})'.format(x, y, target))

	def mouseMoveFromTo(self, fromx, fromy, tox, toy, target):
		self.browser.execute_script('document["dispatchMouseMoveEvent"]({}, {}, {}, {}, {})'.format(fromx, fromy, tox, toy, target))

	def dragAndDropFromTo(self, fromx, fromy, tox, toy, target):
		self.mouseDownAt(fromx, fromy, target)
		self.mouseMoveFromTo(fromx, fromy, tox, toy, target)
		self.mouseUpAt(tox, toy, target)

	def execute(self, script):
		return self.browser.execute_script(script)

def print_should_execution(case, info = ""):
	print("		\033[94m- Should {} - {}\033[0m".format(case.replace('_', ' '), info), end='\r')

def print_should_sucess(case):
	print("		\033[92m\u2713 Should {}\033[0m".format(case.replace('_', ' ')), end='\n')

def print_should_error(case, info = ""):
	print("		\033[91mX Should {} - {}\033[0m".format(case.replace('_', ' '), info), end='\n')

def test(args = {}):
	def wrap(func):
		options = {
			"waitBeforeExecute": 0,
			"waitAfterExecute": 0
		}

		options.update(args)

		driver = webdriver.Chrome('./chromedriver')
		driver.maximize_window()
		driver.get(autoglconfig.getUrl())
		driver.execute_script(open('functions.js').read())

		#Waits before function execution for x MS (default 0)
		print_should_execution(func.__name__, "Waiting {}ms before execution".format(options["waitBeforeExecute"]))
		sleep(options["waitBeforeExecute"] / 1000)

		print_should_execution(func.__name__)
	
		func(autogl_browser(driver))

		#Waits after function execution for x MS (default 0)
		print_should_execution(func.__name__, "Waiting {}ms after execution".format(options["waitAfterExecute"]))
		sleep(options["waitAfterExecute"] / 1000)
		

		if capture is False:
			try:
				driver.save_screenshot('temp/' + func.__name__ + '.png')
				_autogl.should(func.__name__)
			except FileNotFoundError:
				_autogl.errored+=1
				print_should_error(func.__name__, 'Test Data Not Found')
	
		else:
			driver.save_screenshot('cases/' + func.__name__ + '.png')
			print_should_sucess(func.__name__)

		driver.close();
	return wrap



#Initializes Auto GL Instance
_autogl = autogl()

def exit_handler():
	print('\n\n	\033[92m' + str(_autogl.passed) + ' Passed Test(s)\033[0m')
	print('	\033[91m' + str(_autogl.errored) + ' Failed Test(s)\033[0m\n')

atexit.register(exit_handler)
