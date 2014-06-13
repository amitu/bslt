import os
from selenium import webdriver

user = os.environ["BROWSERSTACK_USERNAME"]
key  = os.environ["BROWSERSTACK_KEY"]

desired_cap = {
	'browser': 'IE', 
	'browser_version': '8.0', 
	'os': 'Windows', 
	'os_version': '7',

	'browserstack.local': True,
	"browserstack.debug": True,
}

driver = webdriver.Remote(
    command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (user, key),
    desired_capabilities=desired_cap
)

driver.get("http://localhost:8000")
title = driver.title.encode("utf8")

assert "foo" == title, title

driver.quit()
