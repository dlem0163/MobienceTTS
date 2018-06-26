from num2words import num2words
from subprocess import call

cmd_beg = 'espeak -s 240 '
cmd_end = ' 2>/dev/null'
start_msg = "Ready_to_Rivo."
str = ""
char = ""
prev_char = ""
char_count = 0

import time
import threading
import getch


def thread_speak(str):
        call(str, shell=True)


print cmd_beg+start_msg+cmd_end
t = threading.Thread(target=thread_speak, args=([cmd_beg+start_msg+cmd_end]))
t.daemon = True
t.start()

while 1:

        char = getch.getch()
        if char == chr(127):
                print "This is Back Space"
                print str[:char_count]
                str = str[:char_count]
                if char_count != 0:
                        char_count = char_count - 1
                char = ""
                continue
        if char == '\r':
                print cmd_beg+str[:char_count+1]+cmd_end
                t = threading.Thread(target=thread_speak, args=([cmd_beg+str+cmd_end]))
		t.daemon = True
                t.start()
		str = ""
		char_count = 0
	elif char == ' ':
                str = str[:char_count] + '_'
                char_count = char_count + 1
                print cmd_beg+'_'+cmd_end
        else:
                str = str[:char_count] + char
                char_count = char_count + 1
                print cmd_beg+char+cmd_end
                t = threading.Thread(target=thread_speak, args=([cmd_beg+char+cmd_end]))
		t.daemon = True
                t.start()
        print "Number of Char "
        print char_count
        char = ""
        print "String is " + str


