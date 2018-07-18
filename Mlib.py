
from num2words import num2words
from subprocess import call
from datetime import datetime

import RPi.GPIO as GPIO
import time
import threading

global sound_value
global speed_value
global pitch_value
global flag
global voice
voice = '-ven+m5'
flag = 0 #---- 0 is Man Voice, 1 is Woman Voice ----#
sound_value = 100
speed_value = 180
pitch_value = 49

global cmd_beg
global cmd_end
cmd_beg = 'espeak '+ voice + ' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
cmd_end = ' 2>/dev/null'

string = ""

global MATRIX1
global MATRIX2
global MATRIX3
global MATRIX4

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
	call(string, shell=True)

def speak(string):
	print "Speak : " + string
	print "Sound Amplitude : " + str(sound_value)
	print cmd_beg
	t = threading.Thread(target=thread_speak_fcn, args=([cmd_beg+string+cmd_end]))
	t.start()

#---- SOUND CONTROL ( 0 - 200 ) ----#
def sounddown():
	global sound_value
	global cmd_beg
	if sound_value == 0:
		print "Sound is Min."
		return
	else:
		sound_value = sound_value - 10
		cmd_beg = 'espeak ' + voice +' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
		print "Sound is " + str(sound_value) + " ( 0 ~ 200 )"

def soundup():
	global sound_value
	global cmd_beg
	if sound_value == 200:
		print "Sound is Max."
		return
	else:
		sound_value = sound_value + 10
                cmd_beg = 'espeak ' + voice + ' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
 		print "Sound is " + str(sound_value) + " ( 0 ~ 200 )"

#---- SPEAK SPEED CONTROL ( 80 - 450 ) ----#
def speedup():
	global speed_value
	global cmd_beg
	if speed_value == 450:
		return
	else:
                cmd_beg = 'espeak ' + voice + ' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
 		speed_value = speed_value + 10

def speeddown():
	global speed_value
	global cmd_beg
	if speed_value == 80:
		return
	else:
                cmd_beg = 'espeak ' + voice + ' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
 		speed_value = speed_value - 10

#---- SPEAK PITCH CONTROL ( 0 - 99 ) ----#
def pitchup():
	global pitch_value
	global cmd_beg
	if pitch_value == 99:
		return
	else:
                cmd_beg = 'espeak ' + voice +' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
 		pitch_value = pitch_value + 10

def pitchdown():
	global pitch_value
	global cmd_beg
	if pitch_value == 9:
		return
	else:
                cmd_beg = 'espeak '+ voice + ' -a '+ str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
 		pitch_value = pitch_value - 10

#---- SPEAK VOICE CHANGE ----#
def voice_change():
	global flag
	global cmd_beg
	global voice
	if flag == 0:
		voice = '-ven+f3'
		flag = 1
		cmd_beg = 'espeak ' + voice + ' -a ' + str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '
	else:
		voice = '-ven+m5'
		flag = 0
		cmd_beg = 'espeak ' + voice + ' -a ' + str(sound_value) + ' -p ' +  str(pitch_value) + ' -s ' + str(speed_value) + ' '

#---- CHANGE KEYPAD MATRIX ----#
def matrix1change(a,b,c,d,e,f,g,h,i,j,k,l):
	global MATRIX1
	MATRIX1 = [ [a,b,c,'A'],
		    [d,e,f,'B'],
		    [g,h,i,'C'],
		    [j,k,l,'D']]

def matrix2change(a,b,c,d,e,f,g,h,i,j,k,l):
        global MATRIX2
	MATRIX2 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D']]

def matrix3change(a,b,c,d,e,f,g,h,i,j,k,l):
	global MATRIX3
        MATRIX3 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D']]

def matrix4change(a,b,c,d,e,f,g,h,i,j,k,l):
	global MATRIX4
        MATRIX4 = [ [a,b,c,'A'],
                    [d,e,f,'B'],
                    [g,h,i,'C'],
                    [j,k,l,'D']]

# Modified Button Option ( A~D )
#---- Press A option ----#
def option_1(x,y):
	repeat(x,y)

#---- Press B option ----#
def option_2():
	soundup()

#---- Press C option ----#
def option_3():
	sounddown()

#---- Press D option ----#
def option_4(string):
	speak(string)

#---- WORD REPEAT ----#
def repeat(x,y):
	return MATRIX2[x][y]
#---- SPEAK CURRENT TIME ----#
def timespeak():
	dt = datetime.now()
	ti = dt.strftime("%H,%M")
	#SPEAK TIME
	speak(ti)
#---- PRODUCT RESTART ----#
def restart():
	#SUDO REBOOT
	call('sudo reboot', shell=True)
