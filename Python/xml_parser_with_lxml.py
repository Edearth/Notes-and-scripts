# This script uses the lxml module because it offers more XPath features (using 'text()' inside predicates among them). It can be installed with 'pip install lxml' or it can be found here: http://lxml.de/
# That module might also need Microsoft's Visual C++ Redistributable, which can be found here: https://www.visualstudio.com/es/downloads/?rr=http%3A%2F%2Flandinghub.visualstudio.com%2Fvisual-cpp-build-tools
import lxml.etree as ET

#DEFINE NAMESPACES FIRST!
ns = {"cus" : "http://www.bea.com/wli/config/customizations",
       "xt" : "http://www.bea.com/wli/config/xmltypes"}

tree = ET.parse('file.xml')

root = tree.getroot()

business_services = root.xpath("./cus:customization/cus:owners/xt:owner/xt:type[text()=\"BusinessService\"]/ancestor::cus:customization", namespaces=ns)

for i in range(len(business_services)):
    bs = business_services[i]
    path = bs.xpath("./cus:owners/xt:owner/xt:path", namespaces=ns)
    print("- "+path[0].text+":")
    actions = bs.xpath("./cus:actions/xt:replace", namespaces=ns)
    for j in range(len(actions)):
        act = actions[j]
        value = act.xpath("./xt:envValueType[text()='Service URI']/following-sibling::xt:value", namespaces=ns)
        if value:
            print("\t- "+value[0].text)
