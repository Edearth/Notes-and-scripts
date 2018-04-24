This is a sample configuration of the Log Highlight plugin for Sublime Text (found here:
https://github.com/poucotm/Log-Highlight ). This configurationnuses custom regular expressions
that match the beginning and the end of log messages formatted like the following example:

23:59:59,991 DEBUG [com.test.Class1] (http-127.0.0.1:8080-6) Debug message 1
23:59:59,992 DEBUG [com.test.Class1] (http-127.0.0.1:8080-6) Debug message 2
23:59:59,993 ERROR [com.test.Class1] (ServerService Thread Pool -- 113) Error message
23:59:59,994 INFO  [com.test.Class1] (ServerService Thread Pool -- 113) Info message 1
23:59:59,995 INFO  [com.test.Class1] (ServerService Thread Pool -- 113) Info message 2
23:59:59,996 WARNING [com.test.Class1] (ServerService Thread Pool -- 130) Warning message

This configuration will make the debug lines blue, warning lines yellow and error lines red. 
It will also add markers that can be browsed by pressing F2 on warning and error lines.


HOW TO USE:

- Install Log Highlight plugin for Sublime Text: https://github.com/poucotm/Log-Highlight
- Save these files in "%USER_FOLDER%\AppData\Roaming\Sublime Text 3\Packages\User\"
- Open your log file in Sublime Text, select the desired Log Highlighting syntax
- (you might have to right-click and select Log Highlight to refresh the highlighting) 
