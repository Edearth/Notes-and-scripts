// NOT TESTED YET!
//credit to: http://stackoverflow.com/a/16662257


//get test case from other project
project = testRunner.getTestCase().getTestSuite().getProject().getWorkspace().getProjectByName(project_name)
testSuite = project.getTestSuiteByName(suite_name);
testCase = testSuite.getTestCaseByName(testcase_name);

//set properties
testRunner.testCase.setPropertyValue(property_name, property_value);
testRunner.testCase.setPropertyValue(another_property_name, another_property_value);

// run test case
runner = testCase.run(new com.eviware.soapui.support.types.StringToObjectMap(), false);