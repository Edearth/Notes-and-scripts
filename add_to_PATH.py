import os

#set the path of geckodriver for firefox automation
#"geckodriver.exe" is in the following path:
# "c:\scripts\web_automation\webdrivers\\firefox\geckodriver.exe"
print("Adding geckodriver folder to the PATH.")
os.environ["PATH"] += os.pathsep + "C:\scripts\web_automation\webdrivers\\firefox"
#os.pathsep is the separator for different paths, so we'll use that