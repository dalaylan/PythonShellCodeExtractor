'''
@Date: 1 Nov 2018
@Auth: /Dalaylan
@Disc: quick script to extract all commands used in an active shell and convert them to a python file.
 An attempt is made to remove invalid lines by checking if they compile. 
 NOTE: This does not catch ValueErrors, so make sure to test the output.
@Usage: import this file and then call ExtractShellCode() giving it the filepath you wish to write too. The last line excpected for calling the module is excluded
'''

import readline
import os
import pyflakes
from codeop import compile_command

'''
#run it, remove error, redo until it works
#this is hacked together, and prob very vulnerable. Use with caution
def BruteForceErrorRemoval(f):
    if os.path.exists(f):
        try:
            execfile(f)
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
'''

def ExtractShellCode(filepath):
    try:
        #readline.remove_history_item(readline.get_current_history_length()-1)
        with open(filepath, 'w') as f:
            for i in range(readline.get_current_history_length()):
                line = readline.get_history_item(i + 1)
                try:
                    compile_command(line.strip())
                    if not ('ExtractShellCode(' in line):
                        f.write(line+'\n')
                except SyntaxError:
                    pass
        print('Write to '+str(filepath) + ' succeded.')
    except Exception, e:
        print('write failed.')
        print(str(e))
        print(repr(e))




'''
#gets the last so many lines 
def ExtractShellCode(filepath,numLines):
    if (numLines < 0):
	print 'number of lines given is invalid'
    try:
        with open(filepath, 'w') as f:
	    length = readline.get_current_history_length()
            for i in range(length - numLines, length):
                line = readline.get_history_item(i + 1)
                if codeop.compile_command(line):
                    f.write(line)
        print('Write to '+str(filepath) + ' succeded.')
    except Exception e:
        print('write failed.')
        print e
'''
