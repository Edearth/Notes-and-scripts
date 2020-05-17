import java.util.regex.Matcher
import com.eviware.soapui.impl.wsdl.teststeps.assertions.basic.SimpleContainsAssertion
import com.eviware.soapui.impl.wsdl.teststeps.assertions.basic.SimpleNotContainsAssertion
import com.eviware.soapui.impl.wsdl.teststeps.assertions.basic.GroovyScriptAssertion
import com.eviware.soapui.impl.wsdl.teststeps.assertions.soap.SoapResponseAssertion

for (testCase in testRunner.testCase.testSuite.project.testSuites["Process"].testCases) {
   Matcher matcher = testCase.value.name =~ /(N?TC[0-9]{2})_(.*) - (.*)/
   if (matcher.matches()) {
      testCase.value.name = "prefix " + matcher.group(1) + "_" + matcher.group(2) +
                                 "_" + (matcher.group(3) == "Process OK"? "OK" : "KO")
      
      for (testStep in testCase.value.testSteps) {
         if (testStep.value.name == "Start process") {
            log.info testStep.value.name
            if(testStep.value.metaClass.respondsTo(testStep.value, "getAssertionList")) {
               def assertionList = testStep.value.getAssertionList()
               if(!assertionList.any { it instanceof GroovyScriptAssertion} ){
                  assertionList.each {
                     if (it instanceof SimpleContainsAssertion) {
                        if (it.getToken() == "Process initiated") {
                           testStep.value.name = "[000] " + testStep.value.name
                        } else if(it.getToken() == "Process could not be initiated"){
                           testStep.value.name = "[099] " + testStep.value.name
                        }
                     }
                  }
               } else {
                  if (testStep.value.testCase.testSteps["Get internal id"]
                        .getAssertionList().any { it instanceof SimpleContainsAssertion } ) {
                     testStep.value.name = "[000] " + testStep.value.name
                  } else {
                     testStep.value.name = "[099] " + testStep.value.name
                  }
               }
            }
         } else if (testStep.value.name == "Delete") {
            testStep.value.name = "[000] " + testStep.value.name
         } else if (testStep.value.name == "Validation on DB1") {
            testStep.value.name = "[DB1] " + testStep.value.name
         } else if (testStep.value.name == "Validation on DB2") {
            testStep.value.name = "[DB2] " + testStep.value.name
         } else {
            testStep.value.name = "[ETC] " + testStep.value.name
         }
      }
   }
      
}