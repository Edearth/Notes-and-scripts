# This file contains snippets of code that can be used as a reference when
# developing with Selenium or can even be adapted to make a base page class.
#
# In fact, I have to remember myself to make a template base page class that
# I can just download, add to a project and have a bunch of functionalities
# in the form of protected methods that extending page classes can call.


# This method opens a page in a new tab.
def openPageInNewTab(driver, url):
	driver.execute_script('window.open("'+url+'","_blank");')
	# Keep in mind that if you want to send commands to the newly opened page
	# you'll have to manually switch the driver to that window
	driver.switch_to_window(driver.window_handles[1])
	# In this case we are going to tab #2 (driver.window_handles[1]) because
	# we know the newly opened tab is the nº2. If you're opening them on a
	# loop or though methods, you'll have to handle the handles
	#
	# I think you can just switch to the last tab, but that's something I
	# have yet to test. I'll leave this line to remember myself to test it,
	# but if someone wants to provide an answer you can go ahead.
	# driver.switch_to_window(driver.window_handles[len(driver.window_handles)])