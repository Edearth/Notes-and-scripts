# Water leak strategy

* If you have a water leak at home, would you mop first and fix the leak later?
* **Fix the leak first**. That means stopping more issues/bugs from coming into the project.
* To allow that, **analyze new code** with the Quality Gate you want for the project. If that fails, the developer **cannot merge**, so there won't be more issues coming into the codebase.
* After that you can mop (fix) the issues progressively.

# General guidelines on setting Quality Gates

* **One or a few** Quality Gates only.
* Use metrics on **new code**.
* **A reliability** rating -> 0 bugs.
* **A security** rating.
* Set thresholds that are **challenging but reachable**, then **tighten** criterias progressively.

# Analysing best practices

* Build before you scan (saves time on scan if build fails).
* Use the scanner that corresponds to your build tool (Gradle scanner, Maven scanner, sonar-scanner (CLI)...).

# Shift left - Branch & PR analysis

* **Shift left:** the sooner you find the issue, the easiest it is to fix.
* Analyze in branch, **before merging** to develop.
* Even better to execute **locally** in your IDE (SonarLint, on-the-fly analysis).
  * There's a **connected mode** for SonarLint that allows it to use the same rules as your SonarQube server.
