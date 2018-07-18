from num2words import num2words
from subprocess import call

import RPi.GPIO as GPIO
import time
import threading

def thread_speak(string):
	call(string, shell=True)

sound_value = 100

cmd_beg = 'espeak -a '+ str(sound_value) +' '
cmd_end = ' 2>/dev/null'
GPIO.setmode (GPIO.BOARD)

MATRIX1 = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D']]
MATRIX2 = [ ['e','t','o','A'],
           ['a','r','i','B'],
           ['s','h','n','C'],
           [',',' ','.','D']]
MATRIX3 = [ ['w','u','p','A'],
           ['d','f','l','B'],
           ['c','g','m','C'],
           [',',' ','.','D']]
MATRIX4 = [ ['q','y','o','A'],
           ['z','v','j','B'],
           ['x','b','k','C'],
           [',',' ','.','D']]

string = ""
str_cnt = 0
ROW =   [29,31,33,37]
COL =   [26,24,22,21]
sound_value = 0
prev_str = '?'
save_str_1 = 0
save_str_2 = 0
char_count = 0
Mode = 1

for i in range (4):
	GPIO.setup(COL[i], GPIO.OUT)
	GPIO.output(COL[i], 1)


for i in range (4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

t = threading.Thread(target=thread_speak, args=([cmd_beg+ 'Ready.' +cmd_end]))
t.start()

sound_value = 100
try:
    while(True):
        for j in range (4):
            GPIO.output(COL[j],0)

            for i in range(4):
                if GPIO.input (ROW[i]) == 0:
			if prev_str == '?':
				prev_str = MATRIX2[i][j]
				char_count = char_count + 1
			elif MATRIX2[i][j] == 'D' or MATRIX3[i][j] == 'D' or MATRIX4[i][j] == 'D':
				print "Pressed D"
				if prev_str != 'D':
					string = string + prev_str
				string = string.replace(' ', '_')
				t = threading.Thread(target=thread_speak, args=([cmd_beg+string+cmd_end]))
				t.start()
				string = ""
				prev_str = "?"
				char_count = 0
				continue
			elif MATRIX2[i][j] == 'C' or MATRIX3[i][j] == 'C' or MATRIX4[i][j] == 'C':
				if sound_value == 0:
					print "Volume is Min"
					prev_str = "?"
					continue
				print "Volume Down " + str(sound_value)
				sound_value = sound_value - 5
				cmd_beg = 'espeak -a ' + str(sound_value) + ' '
                        elif MATRIX2[i][j] == 'B' or MATRIX3[i][j] == 'B' or MATRIX4[i][j] == 'B':
                                if sound_value == 200:
                                        print "Volume is Min"
                                        prev_str = "?"
                                        continue
				print "Volume Up " + str(sound_value)
				sound_value = sound_value + 5
				cmd_beg = 'espeak -a ' + str(sound_value) + ' '
			elif MATRIX2[i][j] == 'A' and prev_str != 'A':
				string = string + prev_str
				string = string.replace(' ', '_')
				prev_str = MATRIX2[save_str_1][save_str_2]
			elif prev_str == MATRIX2[i][j] and Mode%2 == 1:
				prev_str = MATRIX3[i][j]
				save_str_1 = i; save_str_2 = j;
 			elif prev_str == MATRIX3[i][j] and Mode%2 == 1:
				prev_str = MATRIX4[i][j]
				save_str_1 = i; save_str_2 = j;
			elif prev_str == MATRIX4[i][j] and Mode%2 == 1:
				prev_str = MATRIX2[i][j]
				save_str_1 = i; save_str_2 = j;
			## Number MATRIX1
			elif prev_str == MATRIX1[i][j] and Mode%2 == 0:
				prev_str = MATRIX1[i][j]
			elif prev_str != MATRIX2[i][j] and prev_str != MATRIX3[i][j] and prev_str != MATRIX4[i][j] and prev_str != 'A':
				if prev_str != 'D':
					string = string + prev_str
				string = string.replace(' ', '_')
				prev_str = MATRIX2[i][j]
			elif prev_str == 'A':
				prev_str = MATRIX2[i][j]
			print string,;print prev_str,;print char_count

			if prev_str != 'D' and prev_str and 'A' and prev_str != 'B' and prev_str != 'C':
                        	t = threading.Thread(target=thread_speak, args=([cmd_beg+prev_str+cmd_end]))
                        	t.start()
			time.sleep(0.2)

                while (GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()
