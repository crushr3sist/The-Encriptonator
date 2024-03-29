#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import math
import sys
import os
import time
from pygame_functions import *
from pygame.locals import *

pygame.init()

  # ##vars###

# screen_size

window_Width = 1280
window_Height = 720

screenSize(window_Width, window_Height)

# window_caption

pygame.display.set_caption('The Encryptonator')

# background

setBackgroundImage('g.png')

# colors

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

  # ##print_testing###

##title##

title = makeLabel(
    'The Encryptinator',
    80,
    370,
    0,
    WHITE,
    font='Ariel',
    )
showLabel(title)

###choice text###

msg1 = makeLabel(
    'Encryptor or Decryptor?',
    80,
    330,
    350,
    WHITE,
    font='Ariel',
    )
dec = makeLabel(
    'Type in the Encrypted password to Decrypt',
    50,
    330,
    350,
    WHITE,
    font='Ariel',
    )
showLabel(msg1)

###enc text###

choiceE = makeTextBox(480, 100, 350)
showTextBox(choiceE)
entry = textBoxInput(choiceE)
hideTextBox(choiceE)
encryptedPassword = ''

print 'Encryptor or Decryptor?'

######choice

if entry[0] == 'E' or entry[0] == 'e':

# encription portion

    enc = makeLabel(
        'Type in a password to start the Encryption',
        50,
        330,
        350,
        WHITE,
        font='Ariel',
        )
    showLabel(enc)
    hideLabel(msg1)
    inputE = makeTextBox(window_Width / 3, window_Height / 3, 450)
    showTextBox(inputE)
    password = textBoxInput(inputE)
    hideTextBox(choiceE)
    updateDisplay()
    passwordLength = len(password)
    alphabet1 = 'XYZabcdefghijklmnopqrstuvw'
    alphabet2 = 'xyzABCDEFGHIJKLMNOPQRSTUVW'
    numbers = '1234567890'
    characters = "!@#$%^&*()-=_+[]\{}|;<>?,./"
    print 'the password you typed: ' + password
    for i in range(passwordLength):
        encryptLetter = password[i]

        if encryptLetter == 'u':
            encryptedPassword = str(encryptedPassword + 'x')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'v':

            encryptedPassword = str(encryptedPassword + 'y')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'w':

            encryptedPassword = str(encryptedPassword + 'z')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'U':

            encryptedPassword = str(encryptedPassword + 'X')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'V':

            encryptedPassword = str(encryptedPassword + 'Y')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'W':

            encryptedPassword = str(encryptedPassword + 'Z')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '8':

            encryptedPassword = str(encryptedPassword + '1')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '9':

            encryptedPassword = str(encryptedPassword + '2')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '0':

            encryptedPassword = str(encryptedPassword + '3')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == ' ':

            encryptedPassword = str(encryptedPassword + '%')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == ',':

            encryptedPassword = str(encryptedPassword + '!')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '.':

            encryptedPassword = str(encryptedPassword + '@')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '/':

            encryptedPassword = str(encryptedPassword + '#')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        else:
            for e in range(26):
                if encryptLetter == alphabet1[e]:
                    encryptedPassword = str(encryptedPassword
                            + alphabet1[e + 3])
                    print 'Encrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)
                elif encryptLetter == alphabet2[e]:

                    encryptedPassword = str(encryedPassword
                            + alphabet2[e + 3])
                    print 'Encrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

            for e in range(10):
                if encryptLetter == numbers[e]:
                    encryptedPassword = str(encryptedPassword
                            + numbers[e + 3])
                    print 'Encrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

            for e in range(26):
                if encryptLetter == characters[e]:
                    encryptedPassword = str(encryptedPassword
                            + characters[e + 3])
                    print 'Encrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

# password saver

    try:
        f = open("h:\encryptedDatabase.txt", 'a')
        f.write(str(encryptedPassword) + '\n')
        f.close()
    except:
        print 'We have encountered an error, please try again later!'
elif entry[0] == 'D' or entry[0] == 'd':

# decryption portion

    hideLabel(msg1)
    showLabel(dec)
    print "ENCRYPTION CANNOT INCLUDE: '' Characters, Inputting these will not be registered!"
    inputD = makeTextBox(window_Width / 3, window_Height / 4, 450)
    showTextBox(inputD)
    encryption = textBoxInput(inputD)
    encryptionLength = len(encryption)
    alphabet1 = 'XYZabcdefghijklmnopqrstuvw'
    alphabet2 = 'xyzABCDEFGHIJKLMNOPQRSTUVW'
    numbers = '1234567890'
    characters = "!@#$%^&*()-=_+[]\{}|;<>?,./"
    print 'the encryption you typed: ' + encryption
    for i in range(encryptionLength):
        encryptLetter = encryption[i]

        if encryptLetter == 'x':
            encryptedPassword = str(encryptedPassword + 'u')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'y':

            encryptedPassword = str(encryptedPassword + 'v')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'z':

            encryptedPassword = str(encryptedPassword + 'w')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'X':

            encryptedPassword = str(encryptedPassword + 'U')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'Y':

            encryptedPassword = str(encryptedPassword + 'V')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == 'Z':

            encryptedPassword = str(encryptedPassword + 'W')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '1':

            encryptedPassword = str(encryptedPassword + '8')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '2':

            encryptedPassword = str(encryptedPassword + '9')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '3':

            encryptedPassword = str(encryptedPassword + '0')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '%':

            encryptedPassword = str(encryptedPassword + ' ')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '!':

            encryptedPassword = str(encryptedPassword + ',')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '@':

            encryptedPassword = str(encryptedPassword + '.')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        elif encryptLetter == '#':

            encryptedPassword = str(encryptedPassword + '/')
            print 'Encrypting: ' + encryptLetter
            time.sleep(0.1)
            print 'Password is: ' + encryptedPassword
            time.sleep(0.1)
        else:
            for e in range(26):
                if encryptLetter == alphabet1[e]:
                    encryptedPassword = str(encryptedPassword
                            + alphabet1[e - 3])
                    print 'Decrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)
            for e in range(26):
                if encryptLetter == alphabet2[e]:
                    encryptedPassword = str(encryptedPassword
                            + alphabet2[e - 3])
                    print 'Decrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

            for e in range(10):
                if encryptLetter == numbers[e]:
                    encryptedPassword = str(encryptedPassword
                            + numbers[e - 3])
                    print 'Decrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

            for e in range(26):
                if encryptLetter == characters[e]:
                    encryptedPassword = str(encryptedPassword
                            + characters[e - 3])
                    print 'Decrypting: ' + encryptLetter
                    time.sleep(0.1)
                    print 'Password is: ' + encryptedPassword
                    time.sleep(0.1)

# output portion

pswd = makeLabel(
    'Your password is: ' + encryptedPassword,
    80,
    360,
    450,
    WHITE,
    font='Ariel',
    )
showLabel(pswd)

waitPress()

endWait()


