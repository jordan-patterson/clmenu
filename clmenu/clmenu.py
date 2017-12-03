#!/usr/bin/env python3

from sys import stdin
from os import system,path
from termcolor import colored

class getch:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def printLogo(filename):
    try:
        file=open(filename,'r')
        data=file.read()
        system("clear")
        print(data)
    except FileNotFoundError:
        print("\n\n\t\t\t\tError: File does not exist")

class Menu:
    '''
        A Class for making a custom menu in the command line
        options: A list of options for the menu
        instructions: A small piece of text telling the user what to do
        logoName: The name of a file with your custom made logo. ASCII ART RECOMMENDED
    '''
    def __init__(self,options,instructions,logoName):
        self.options=options
        self.instructions=instructions
        self.logoName=logoName

    def arrow(self,count,tabs):
        '''
            Method for displaying the menu. The arrow is printed beside the option
            that has index count
        '''
        printLogo(self.logoName)
        print("\n\n\t\t\t\t     "+colored(self.instructions,'magenta')+"\n\n")
        for i in range(len(self.options)):
            if(tabs):
                print("\t\t\t\t      ",end="")
            else:
                print("\t\t   ",end="")
            if(i==count):
                print("->>>>>>[ "+colored(self.options[i],'green')+"   \n")
            else:
                print("      [ "+colored(self.options[i],'cyan')+"    \n")

    def prompt(self,tabs=True):
        '''
            Method for handling the user input and increasing or decreasing count when either UP
            or DOWN arrow key was presssed
        '''
        count=0
        getc=getch()
        self.arrow(count,tabs)
        key=" "
        while(ord(key)!=13):
            key=getc()
            if(ord(key)==66):
                if(count<len(self.options)-1):
                    count+=1
            elif(ord(key)==65):
                if(count>0):
                    count-=1
            self.arrow(count,tabs)
        return count

