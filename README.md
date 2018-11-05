# PythonShellCodeExtractor

quick script to extract all commands used in an active shell and convert them to a python file.
 - An attempt is made to remove invalid lines by checking if they compile. 
 - NOTE: This does not catch ValueErrors, so make sure to test the output.

Usage:
 - import this file and then call ExtractShellCode() giving it the filepath you wish to write too.
