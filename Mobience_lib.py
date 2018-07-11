
from num2words import num2words
from subprocess import call

from datetime import datetime
import threading

sound_value = 100
speed_value = 180
pitch_value = 49

cmd_beg = 'espeak -a '+ str(sound_value) +' '
cmd_end = ' 2>/dev/null'


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


def thread_speak_fcn(string):

def thread_start_fcn(string):

#---- SOUND CONTROL ( 0 - 200 ) ----#
def keypad_sound_down():
	if sound_value == 0:
		return
	else:
		sound_value = sound_value - 10

def keypad_sound_up():
	if sound_value == 200:
		return
	else:
		sound_value = sound_value + 10

#---- SPEAK SPEED CONTROL ( 80 - 450 ) ----#
def keypad_speak_fast():
	if speed_value == 450:
		return
	else:
		speed_value = speed_value + 10

def keypad_speak_slow():
	if speed_value == 80:
		return
	else:
		speed_value = speed_value - 10

#---- SPEAK PITCH CONTROL ( 0 - 99 ) ----#
def keypad_pitch_up():
	if pitch_value == 99:
		return
	else:
		pitch_value = pitch_value + 10

def keypad_pitch_down():
	if pitch_value == 9:
		return
	else:
		pitch_value = pitch_value - 10

#---- SPEAK VOICE CHANGE ----#
def keypad_voice_change():


#---- CHANGE KEYPAD MATRIX ----#
def keypad_matrix_1_change(a,b,c,d,e,f,g,h,i,j,k,l):
	MATRIX1 = [ [a,b,c,'A'],
		    [d,e,f,'B'],
		    [g,h,i,'C'],
		    [j,k,l,'D'] ]

def keypad_matrix_2_change(a,b,c,d,e,f,g,h,i,j,k,l):
        MATRIX2 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D'] ]

def keypad_matrix_3_change(a,b,c,d,e,f,g,h,i,j,k,l):
        MATRIX3 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D'] ]

def keypad_matrix_4_change(a,b,c,d,e,f,g,h,i,j,k,l):
        MATRIX4 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D'] ]

# Modified Button Option ( A~D )
#---- Press A option ----#
def keypad_option_1(x,y):
	keypad_repeat(x,y)

#---- Press B option ----#
def keypad_option_2():
	keypad_sound_up()

#---- Press C option ----#
def keypad_option_3():
	keypad_sound_down()

#---- Press D option ----#
def keypad_option_4(string):
	thread_speak_fcn(string)





#---- WORD REPEAT ----#
def keypad_repeat(x,y)
	return MATRIX2[x][y]
#---- SPEAK CURRENT TIME ----#
def keypad_time_speak():
	dt = datetime.now()
	ti = dt.strftime("%H,%M")
	#SPEAK TIME

#---- PRODUCT RESTART ----#
def keypad_restart_fcn():
	#SUDO REBOOT
	call('sudo reboot', shell=True)
