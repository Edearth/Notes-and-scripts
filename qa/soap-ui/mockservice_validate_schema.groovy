/** 
 * This script validates the schema of the request when assigned to a
 * MockOperation's script dispatch method. If the request is not valid, the
 * script throws an exception and makes the service return an error message.
 */

def wsdlcontext = context.mockService.getMockedInterfaces()[0].getDefinitionContext()
def validator = new com.eviware.soapui.impl.wsdl.support.wsdl.WsdlValidator(wsdlcontext)

def operation = "buscarOficinas"
//mockRequest.soapAction.substring(mockRequest.soapAction.lastIndexOf('/') +1)
log.info  context.mockService.toString() + "::" + operation
def wsdlMockOperation = context.mockService.getMockOperationByName(operation)
 
def msgExchange = new com.eviware.soapui.impl.wsdl.panels.mockoperation.WsdlMockRequestMessageExchange(mockRequest, wsdlMockOperation)
def errors = validator.assertRequest(msgExchange, false)

if (errors.length > 0 ) {
    throw new Exception("VALIDATION ERRORS: " + errors.collect(){ '\n' + it })
}
