import groovy.json.JsonSlurper
import groovy.json.JsonOutput
import groovy.json.JsonBuilder

/*
Please, to initialize this class in a step use the following code snippet:

//if the 'utils' library has not been initialized yet, initialize it
if (!context.utils) testRunner.testCase.testSuite.project.testSuites["Library"].testCases["Utils"].testSteps["Utils"].run(testRunner, context)      

After executing that, context.utils will hold an instance of the following class.
 */

class Utils {

  def log
  def context
  def testRunner

  def Utils(log, context, testRunner){
    this.log = log
    this.context = context
    this.testRunner = testRunner
  }

  def getSlurperResponseFromStep(String stepName, testRunner) {
    def responseContent = testRunner.testCase.getTestStepByName(stepName).getPropertyValue("response")
    return new JsonSlurper().parseText(responseContent)
  }

  def modifyJSONField(json, fieldName, newValue) {
    json[fieldName] = newValue
    def builder = new JsonBuilder(json)
    return new JsonSlurper().parseText(builder.toString())
  }

  def addJSONToRequest(String stepName, json) {
    def step = testRunner.testCase.getTestStepByName(stepName)
    def request = step.getTestRequest()
    request.setRequestContent(JsonOutput.prettyPrint(JsonOutput.toJson(json)))
  }

  def executeStep(String stepName, testRunner, context) {
    def step = testRunner.testCase.getTestStepByName(stepName)
    step.run(testRunner, context)
  }

  def setStepProperty(String stepName, String propertyName, String propertyValue) {
    def step = testRunner.testCase.getTestStepByName(stepName)
    step.setPropertyValue(propertyName,propertyValue)
  }
}

context.setProperty( "utils", new Utils(log, context, testRunner) )
