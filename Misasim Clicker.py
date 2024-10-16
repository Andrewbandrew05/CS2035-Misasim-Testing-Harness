from win32gui import GetWindowText, GetForegroundWindow
import time
import win32api, win32con
import subprocess
#will need to create installer that imports pyautogui
import pyautogui
import pyperclip
import os

bufferBase = 0.1

#need to find way to guarantee location of misasim buttons
def processDumpFile(filePath):
    os.chdir(filePath)
    file=open("dump.txt")
    candidate0 = []
    candidate1 = []
    candidate2 = []
    candidate3 = []
    candidate4 = []
    candidate5 = []
    candidate6 = []
    candidate7 = []
    pattern = []
    outputString = ""
    patternOrCandidateNumber = 0
    counter = 0
    listOfStrings = ["","","","","","","","","","","",""]
    stringListCounter = 0
    for line in file:
        line = line.split(":")[1]
        line = line.strip()
        outputString += line +", "
        counter += 1
        if counter % 12 == 0:
            listOfStrings[stringListCounter] = listOfStrings[stringListCounter] + outputString
            outputString = outputString[:-2]
            outputString += "\n"
            if patternOrCandidateNumber == 0:
                candidate0.append(outputString)
            elif patternOrCandidateNumber == 1:
                candidate1.append(outputString)
            elif patternOrCandidateNumber == 2:
                candidate2.append(outputString)
            elif patternOrCandidateNumber == 3:
                candidate3.append(outputString)
            elif patternOrCandidateNumber == 4:
                candidate4.append(outputString)
            elif patternOrCandidateNumber == 5:
                candidate5.append(outputString)
            elif patternOrCandidateNumber == 6:
                candidate6.append(outputString)
            elif patternOrCandidateNumber == 7:
                candidate7.append(outputString)
            elif patternOrCandidateNumber == 8:
                pattern.append(outputString)
            outputString = ""
            stringListCounter += 1
        if counter == 144:
            counter = 0
            patternOrCandidateNumber += 1
            stringListCounter = 0
    answerFound = True
    for index in range(0, 12):
        if candidate0[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 0
    answerFound = True
    for index in range(0, 12):
        if candidate1[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 1
    answerFound = True
    for index in range(0, 12):
        if candidate2[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 2
    answerFound = True
    for index in range(0, 12):
        if candidate3[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 3
    answerFound = True
    for index in range(0, 12):
        if candidate4[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 4
    answerFound = True
    for index in range(0, 12):
        if candidate5[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 5
    answerFound = True
    for index in range(0, 12):
        if candidate6[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 6
    answerFound = True
    for index in range(0, 12):
        if candidate7[index] != pattern[index]:
            answerFound = False
            break
    if answerFound:
        return 7

def closeAbsurdAmountofWindows():
    time.sleep(bufferBase) #buffer time
    #MAKE SURE TO HAVE MISASIM FIRST IN TASKBAR
    pyautogui.click(350,1050) #open window lise file
    time.sleep(2 * bufferBase) #buffer time
    pyautogui.click(580,990) #close windo file


def runTest():
    global numFailedTests
    time.sleep(bufferBase) #buffer time
    pyautogui.click(100,50) #reload file
    time.sleep(bufferBase) #buffer time
    pyautogui.click(150, 50) #run test
    time.sleep(bufferBase)
    while "Icon Matching" not in GetWindowText(GetForegroundWindow()):
        pyautogui.click(300,300) #clicks on where icon matching window is to bring it to foreground
        time.sleep(0.05)
    pyautogui.click(700,700) #clicks off incon matching to make it go away
    time.sleep(bufferBase) #buffer time
    pyautogui.click(700, 50) #move to end of trace thing
    time.sleep(bufferBase) #buffer time
    pyautogui.click(300, 50) #dump file
    #types out dump.txt
    while "Save" not in GetWindowText(GetForegroundWindow()):
        time.sleep(0.05)
    time.sleep(bufferBase) #buffer time
    pyautogui.press('d')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('u')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('m')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('p')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('.')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('t')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('x')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('t')
    time.sleep(bufferBase) #buffer time
    pyautogui.press('enter')
    x = 0
    #IF DUMP FILE DOESNT EXIST THIS WILL TAKE A LONG TIME TO RUN AND LIKE WAIT
    while "Confirm" not in GetWindowText(GetForegroundWindow()) and x < 1000: 
        time.sleep(0.05)
        x+=1
    if "Confirm" in GetWindowText(GetForegroundWindow()):
        pyautogui.press('left')
        time.sleep(bufferBase) #buffer time
        pyautogui.press('enter')
    while "MiSaSiM" not in GetWindowText(GetForegroundWindow()):
        time.sleep(0.05)
    time.sleep(0.5) #extra long buffer needed here for some reason
    pyautogui.click(1725, 460) #open reg 2
    time.sleep(bufferBase) #buffer time
    pyautogui.click(300, 250) #click on reg 2
    time.sleep(bufferBase) #buffer time
    pyautogui.hotkey('ctrl', 'a') #highlight text
    time.sleep(bufferBase) #buffer time
    pyautogui.hotkey('ctrl', 'c') #copy text
    time.sleep(bufferBase) #buffer time
    pyautogui.click(1000,10) #clicks off register output to make it go away
    text = pyperclip.paste() #gets text from clipboard
    text = text.split("\n")
    lastLine = ""
    for line in text:
        if len(line) > 3:
            lastLine = line
    answer = int(lastLine.split(",")[3].replace("]", '').strip())
    actualAnswer = processDumpFile(misAsimFilePath)
    if actualAnswer != answer:
        numFailedTests += 1
        fileToCopy = open("dump.txt")
        listOfLines = fileToCopy.readlines()
        fileToCopy.close()
        os.chdir(filePathForBadTests)
        fileToCopyTo = open("failedTest" + str(numFailedTests) + "-" + str(actualAnswer) + ".txt", "w")
        for line in listOfLines:
            fileToCopyTo.write(line)
        fileToCopyTo.close()
        os.chdir(misAsimFilePath)

#closeAbsurdAmountofWindows()
    
global numFailedTests
numFailedTests = 0
misAsimFilePath = input("Please input filepath to misasim asm folder.\n").replace('"', '')
filePathForBadTests = input("Please type the filepath for where you would like to save any failed tests.\n").replace('"', '')
os.chdir(filePathForBadTests)
os.chdir(misAsimFilePath)

numTeststoRun = input("Please type the number of tests you would like to run.\n")
                    

while "MiSaSiM" not in GetWindowText(GetForegroundWindow()):
    time.sleep(0.5)

print("MiSaSim in foreground!")
time.sleep(5)

for i in range(0, int(numTeststoRun)):
    if i > 20 and i % 10 == 0:
        for i in range (0,20):
            closeAbsurdAmountofWindows()
        time.sleep(bufferBase) #buffer time
        pyautogui.click(1000,10) #clicks back into misasim
    runTest()

print("Num tests failed: " + str(numFailedTests))


