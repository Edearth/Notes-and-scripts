#class BasePageObject()
# CONSTRUCTOR
# public BaseScreenObject(ProcessExecution pe) {
#	this.pe = pe
#	try {
#			driver = TestSettings.getInstance().getCurrentDriver();
#		} catch (Exception e) {
#			log.severe(TestSettings.getStackTrace(e));
#		}
#	}
#
# METHODS
# > get element
# protected WebElement getElement(By by)
# protected List<MobileElement> getElements(By by)
# protected WebElement getElementWithoutWaiting(By by)
# protected WebElement getElementWithExplicitTimeout(By by, int timeoutSeconds)
# protected List<WebElement> getChildrenOfElement(WebElement parent, String typeOfChildren)
# protected List<MobileElement> getChildrenOfElement(By parent, String typeOfChildren)
# protected List<MobileElement> getChildrenOfElement(String xpath)
# > click
# protected void click(By by)
# protected void click(WebElement element)
# protected void clickElementIfExists(By by)
# protected void clickWithoutWaiting(By by)
# > fill text
# protected void fillText(By by, String text)
# protected void fillText(WebElement element, String text)
# protected void fillTextWithoutWaiting(By by, String text)
# public void selectValueOfPickerWheel(By by, String date)
# > get value
# protected String getValue(By by)
# protected String getValue(WebElement element)
# protected String getValueWithoutWaiting(By by)
# protected String getValueWithoutWaiting(WebElement element)
# > text
# protected String getElementText(By by)
# protected String getElementText(WebElement we)
# protected Dimension getElementSize(WebElement we)
# protected Point getElementLocation(WebElement we)
# > waits
# protected void waitForElementToLoad(By by)
# protected void waitForElementToDisappear(By by)
# protected void wait(int seconds) throws InterruptedException
# > condiciones
# protected boolean elementExists(By element)
# > helpers
# protected String getElementXPath(WebElement we)
# public void scrollTo(By element)
# public void scrollTo(Point location)
# public void scrollDown()