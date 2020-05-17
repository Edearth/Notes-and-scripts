 /**
  * Generate a spanish NIF/DNI number.
  */
 def generateNIF() {
    def dni =Math.abs(new Random().nextInt() % 99999999 + 1000000)
    def NIF_STRING_ASOCIATION = "TRWAGMYFPDXBNJZSQVHLCKE"
    def NIF = String.valueOf(dni) + NIF_STRING_ASOCIATION.charAt(dni % 23)
    return NIF;
 }