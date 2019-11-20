#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Wed Nov 20 11:26:56 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'findObjects'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lowe/Documents/Programmering/Python/PsychoPy projects/psychopy_find_targets/find_targets_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_routine"
welcome_routineClock = core.Clock()
txt_welcome = visual.TextStim(win=win, name='txt_welcome',
    text='Your task in this experiment is to find certain objects in images.\n\nYou will be shown different images with corresponding objects. The object you are to find is always shown under the image. The image is hidden in multiple locations on each image [NOTE: this isn’t true for the placeholder images used here]\n\nEach time you find an object in the image you are to click it once with the computer mouse (left button). A small blue cross will be left where you’ve clicked. The crosses are there to help you know where you’ve already clicked.\n\nAfter you’ve found and clicked on an object at one location, try to find it at a new location and click there, too. [NOTE: again, this isn’t the case with the placeholder image used here]\n\nEach image is shown for a limited amount of time. Try to find the object in as many locations as possible.',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_welcome_clickme = visual.TextStim(win=win, name='text_welcome_clickme',
    text="When you're done reading, click here using the mouse.",
    font='Arial',
    pos=(0, -350), height=15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "welcome_2_routine"
welcome_2_routineClock = core.Clock()
text_pre_practice_a = visual.TextStim(win=win, name='text_pre_practice_a',
    text='We’ll start now with a practice image. Try to click all locations where you can see the object.\n\nClick here to proceed to the image.',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "practice_a"
practice_aClock = core.Clock()
practice_poly = visual.Rect(
    win=win, name='practice_poly',
    width=[431, 290][0], height=[431, 290][1],
    ori=0, pos=(0, 100),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)
practice_context = visual.ImageStim(
    win=win,
    name='practice_context', 
    image='sin', mask=None,
    ori=0, pos=(0, 100), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
practice_mouse = event.Mouse(win=win)
x, y = [None, None]
practice_mouse.mouseClock = core.Clock()
def makeCross(pos):
    cross = visual.ShapeStim(win, pos=pos, depth=-2, vertices='cross', size=(5,5), lineColor=[-0.8, -0.8, 1], fillColor=[-0.8, -0.8, 1])
    cross.setAutoDraw(True)
    return cross
practice_target = visual.ImageStim(
    win=win,
    name='practice_target', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, -250), size=(108, 108),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "feedback_a"
feedback_aClock = core.Clock()
testImg_3 = visual.ImageStim(
    win=win,
    name='testImg_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 100), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_feedback = event.Mouse(win=win)
x, y = [None, None]
mouse_feedback.mouseClock = core.Clock()
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='There was one pizza slice in the image, as you can see above. Did you find them all? [note: in the original experiment, the practice object is shown in multiple locations]\n\nNote that the objects you are to find in the images are sometimes rotated and can have different sizes. [again, this refers to the original images]',
    font='Arial',
    pos=(0, -200), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_feedback_continue = visual.TextStim(win=win, name='text_feedback_continue',
    text='Click here to start the actual test.',
    font='Arial',
    pos=(0, -370), height=15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank500_txt = visual.TextStim(win=win, name='blank500_txt',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank3000"
blank3000Clock = core.Clock()
blank3000_next_txt = visual.TextStim(win=win, name='blank3000_next_txt',
    text='Here comes the image...',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "count_3"
count_3Clock = core.Clock()
text_count_3 = visual.TextStim(win=win, name='text_count_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=100, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "count_2"
count_2Clock = core.Clock()
text_count_2 = visual.TextStim(win=win, name='text_count_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=100, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "count_1"
count_1Clock = core.Clock()
text_count_1 = visual.TextStim(win=win, name='text_count_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=100, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testRout"
testRoutClock = core.Clock()
testPoly = visual.Rect(
    win=win, name='testPoly',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=(0, 100),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)
testImg = visual.ImageStim(
    win=win,
    name='testImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 100), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
testMouse = event.Mouse(win=win)
x, y = [None, None]
testMouse.mouseClock = core.Clock()
def makeCross(pos):
    cross = visual.ShapeStim(win, pos=pos, depth=-2, vertices='cross', size=(5,5), lineColor=[-0.8, -0.8, 1], fillColor=[-0.8, -0.8, 1])
    cross.setAutoDraw(True)
    return cross
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, -250), size=(108, 108),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
blank500_txt = visual.TextStim(win=win, name='blank500_txt',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end_routine"
end_routineClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you! Please wait for the researcher to come over.',
    font='Arial',
    pos=(0, 0), height=25, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_routine"-------
t = 0
welcome_routineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
welcome_routineComponents = [txt_welcome, text_welcome_clickme, mouse]
for thisComponent in welcome_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_routine"-------
while continueRoutine:
    # get current time
    t = welcome_routineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_welcome* updates
    if t >= 0.0 and txt_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        txt_welcome.tStart = t  # not accounting for scr refresh
        txt_welcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(txt_welcome, 'tStartRefresh')  # time at next scr refresh
        txt_welcome.setAutoDraw(True)
    
    # *text_welcome_clickme* updates
    if t >= 0 and text_welcome_clickme.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_welcome_clickme.tStart = t  # not accounting for scr refresh
        text_welcome_clickme.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_welcome_clickme, 'tStartRefresh')  # time at next scr refresh
        text_welcome_clickme.setAutoDraw(True)
    # *mouse* updates
    if t >= 8 and mouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse.tStart = t  # not accounting for scr refresh
        mouse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [text_welcome_clickme]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_routine"-------
for thisComponent in welcome_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_welcome.started', txt_welcome.tStartRefresh)
thisExp.addData('txt_welcome.stopped', txt_welcome.tStopRefresh)
thisExp.addData('text_welcome_clickme.started', text_welcome_clickme.tStartRefresh)
thisExp.addData('text_welcome_clickme.stopped', text_welcome_clickme.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [text_welcome_clickme]:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "welcome_routine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_2_routine"-------
t = 0
welcome_2_routineClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
welcome_2_routineComponents = [text_pre_practice_a, mouse_2]
for thisComponent in welcome_2_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_2_routine"-------
while continueRoutine:
    # get current time
    t = welcome_2_routineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_pre_practice_a* updates
    if t >= 0.0 and text_pre_practice_a.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_pre_practice_a.tStart = t  # not accounting for scr refresh
        text_pre_practice_a.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_pre_practice_a, 'tStartRefresh')  # time at next scr refresh
        text_pre_practice_a.setAutoDraw(True)
    # *mouse_2* updates
    if t >= 1 and mouse_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse_2.tStart = t  # not accounting for scr refresh
        mouse_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [text_pre_practice_a]:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_2_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_2_routine"-------
for thisComponent in welcome_2_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_pre_practice_a.started', text_pre_practice_a.tStartRefresh)
thisExp.addData('text_pre_practice_a.stopped', text_pre_practice_a.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [text_pre_practice_a]:
        if obj.contains(mouse_2):
            gotValidClick = True
            mouse_2.clicked_name.append(obj.name)
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
if len(mouse_2.clicked_name):
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "welcome_2_routine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_a"-------
t = 0
practice_aClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
practice_context.setSize([431, 290])
practice_context.setImage('imgs/contexts/cont_A.jpg')
# setup some python lists for storing info about the practice_mouse
practice_mouse.x = []
practice_mouse.y = []
practice_mouse.leftButton = []
practice_mouse.midButton = []
practice_mouse.rightButton = []
practice_mouse.time = []
gotValidClick = False  # until a click is received
practice_mouse.mouseClock.reset()
crosses = []
practice_target.setImage('imgs/targets/targ_A.jpg')
# keep track of which components have finished
practice_aComponents = [practice_poly, practice_context, practice_mouse, practice_target]
for thisComponent in practice_aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practice_a"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice_aClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_poly* updates
    if t >= 0.0 and practice_poly.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_poly.tStart = t  # not accounting for scr refresh
        practice_poly.frameNStart = frameN  # exact frame index
        win.timeOnFlip(practice_poly, 'tStartRefresh')  # time at next scr refresh
        practice_poly.setAutoDraw(True)
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if practice_poly.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        practice_poly.tStop = t  # not accounting for scr refresh
        practice_poly.frameNStop = frameN  # exact frame index
        win.timeOnFlip(practice_poly, 'tStopRefresh')  # time at next scr refresh
        practice_poly.setAutoDraw(False)
    
    # *practice_context* updates
    if t >= 0.0 and practice_context.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_context.tStart = t  # not accounting for scr refresh
        practice_context.frameNStart = frameN  # exact frame index
        win.timeOnFlip(practice_context, 'tStartRefresh')  # time at next scr refresh
        practice_context.setAutoDraw(True)
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if practice_context.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        practice_context.tStop = t  # not accounting for scr refresh
        practice_context.frameNStop = frameN  # exact frame index
        win.timeOnFlip(practice_context, 'tStopRefresh')  # time at next scr refresh
        practice_context.setAutoDraw(False)
    # *practice_mouse* updates
    if t >= 0.0 and practice_mouse.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_mouse.tStart = t  # not accounting for scr refresh
        practice_mouse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(practice_mouse, 'tStartRefresh')  # time at next scr refresh
        practice_mouse.status = STARTED
        prevButtonState = practice_mouse.getPressed()  # if button is down already this ISN'T a new click
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if practice_mouse.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        practice_mouse.tStop = t  # not accounting for scr refresh
        practice_mouse.frameNStop = frameN  # exact frame index
        win.timeOnFlip(practice_mouse, 'tStopRefresh')  # time at next scr refresh
        practice_mouse.status = FINISHED
    if practice_mouse.status == STARTED:  # only update if started and not finished!
        buttons = practice_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = practice_mouse.getPos()
                practice_mouse.x.append(x)
                practice_mouse.y.append(y)
                buttons = practice_mouse.getPressed()
                practice_mouse.leftButton.append(buttons[0])
                practice_mouse.midButton.append(buttons[1])
                practice_mouse.rightButton.append(buttons[2])
                practice_mouse.time.append(practice_mouse.mouseClock.getTime())
    if testMouse.isPressedIn(practice_poly):
        crosses.append(makeCross(practice_mouse.getPos()))
    
    # *practice_target* updates
    if t >= 0.0 and practice_target.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_target.tStart = t  # not accounting for scr refresh
        practice_target.frameNStart = frameN  # exact frame index
        win.timeOnFlip(practice_target, 'tStartRefresh')  # time at next scr refresh
        practice_target.setAutoDraw(True)
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if practice_target.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        practice_target.tStop = t  # not accounting for scr refresh
        practice_target.frameNStop = frameN  # exact frame index
        win.timeOnFlip(practice_target, 'tStopRefresh')  # time at next scr refresh
        practice_target.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_a"-------
for thisComponent in practice_aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_poly.started', practice_poly.tStartRefresh)
thisExp.addData('practice_poly.stopped', practice_poly.tStopRefresh)
thisExp.addData('practice_context.started', practice_context.tStartRefresh)
thisExp.addData('practice_context.stopped', practice_context.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('practice_mouse.x', practice_mouse.x)
thisExp.addData('practice_mouse.y', practice_mouse.y)
thisExp.addData('practice_mouse.leftButton', practice_mouse.leftButton)
thisExp.addData('practice_mouse.midButton', practice_mouse.midButton)
thisExp.addData('practice_mouse.rightButton', practice_mouse.rightButton)
thisExp.addData('practice_mouse.time', practice_mouse.time)
thisExp.addData('practice_mouse.started', practice_mouse.tStart)
thisExp.addData('practice_mouse.stopped', practice_mouse.tStop)
thisExp.nextEntry()
for across in crosses:
        across.setAutoDraw(False)
thisExp.addData('practice_target.started', practice_target.tStartRefresh)
thisExp.addData('practice_target.stopped', practice_target.tStopRefresh)

# ------Prepare to start Routine "feedback_a"-------
t = 0
feedback_aClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
testImg_3.setSize([431, 290])
testImg_3.setImage('imgs/instruction/instr_A.jpg')
# setup some python lists for storing info about the mouse_feedback
mouse_feedback.x = []
mouse_feedback.y = []
mouse_feedback.leftButton = []
mouse_feedback.midButton = []
mouse_feedback.rightButton = []
mouse_feedback.time = []
mouse_feedback.clicked_name = []
gotValidClick = False  # until a click is received
mouse_feedback.mouseClock.reset()
# keep track of which components have finished
feedback_aComponents = [testImg_3, mouse_feedback, text_feedback, text_feedback_continue]
for thisComponent in feedback_aComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback_a"-------
while continueRoutine:
    # get current time
    t = feedback_aClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *testImg_3* updates
    if t >= 0.0 and testImg_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        testImg_3.tStart = t  # not accounting for scr refresh
        testImg_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(testImg_3, 'tStartRefresh')  # time at next scr refresh
        testImg_3.setAutoDraw(True)
    # *mouse_feedback* updates
    if t >= 1 and mouse_feedback.status == NOT_STARTED:
        # keep track of start time/frame for later
        mouse_feedback.tStart = t  # not accounting for scr refresh
        mouse_feedback.frameNStart = frameN  # exact frame index
        win.timeOnFlip(mouse_feedback, 'tStartRefresh')  # time at next scr refresh
        mouse_feedback.status = STARTED
        prevButtonState = mouse_feedback.getPressed()  # if button is down already this ISN'T a new click
    if mouse_feedback.status == STARTED:  # only update if started and not finished!
        buttons = mouse_feedback.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [text_feedback_continue]:
                    if obj.contains(mouse_feedback):
                        gotValidClick = True
                        mouse_feedback.clicked_name.append(obj.name)
                x, y = mouse_feedback.getPos()
                mouse_feedback.x.append(x)
                mouse_feedback.y.append(y)
                buttons = mouse_feedback.getPressed()
                mouse_feedback.leftButton.append(buttons[0])
                mouse_feedback.midButton.append(buttons[1])
                mouse_feedback.rightButton.append(buttons[2])
                mouse_feedback.time.append(mouse_feedback.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_feedback* updates
    if t >= 0.0 and text_feedback.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_feedback.tStart = t  # not accounting for scr refresh
        text_feedback.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_feedback, 'tStartRefresh')  # time at next scr refresh
        text_feedback.setAutoDraw(True)
    
    # *text_feedback_continue* updates
    if t >= 0.0 and text_feedback_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_feedback_continue.tStart = t  # not accounting for scr refresh
        text_feedback_continue.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_feedback_continue, 'tStartRefresh')  # time at next scr refresh
        text_feedback_continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_aComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_a"-------
for thisComponent in feedback_aComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('testImg_3.started', testImg_3.tStartRefresh)
thisExp.addData('testImg_3.stopped', testImg_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(mouse_feedback.x): thisExp.addData('mouse_feedback.x', mouse_feedback.x[0])
if len(mouse_feedback.y): thisExp.addData('mouse_feedback.y', mouse_feedback.y[0])
if len(mouse_feedback.leftButton): thisExp.addData('mouse_feedback.leftButton', mouse_feedback.leftButton[0])
if len(mouse_feedback.midButton): thisExp.addData('mouse_feedback.midButton', mouse_feedback.midButton[0])
if len(mouse_feedback.rightButton): thisExp.addData('mouse_feedback.rightButton', mouse_feedback.rightButton[0])
if len(mouse_feedback.time): thisExp.addData('mouse_feedback.time', mouse_feedback.time[0])
if len(mouse_feedback.clicked_name): thisExp.addData('mouse_feedback.clicked_name', mouse_feedback.clicked_name[0])
thisExp.addData('mouse_feedback.started', mouse_feedback.tStart)
thisExp.addData('mouse_feedback.stopped', mouse_feedback.tStop)
thisExp.nextEntry()
thisExp.addData('text_feedback.started', text_feedback.tStartRefresh)
thisExp.addData('text_feedback.stopped', text_feedback.tStopRefresh)
thisExp.addData('text_feedback_continue.started', text_feedback_continue.tStartRefresh)
thisExp.addData('text_feedback_continue.stopped', text_feedback_continue.tStopRefresh)
# the Routine "feedback_a" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank500"-------
t = 0
blank500Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [blank500_txt]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank500_txt* updates
    if t >= 0.0 and blank500_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        blank500_txt.tStart = t  # not accounting for scr refresh
        blank500_txt.frameNStart = frameN  # exact frame index
        win.timeOnFlip(blank500_txt, 'tStartRefresh')  # time at next scr refresh
        blank500_txt.setAutoDraw(True)
    frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if blank500_txt.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        blank500_txt.tStop = t  # not accounting for scr refresh
        blank500_txt.frameNStop = frameN  # exact frame index
        win.timeOnFlip(blank500_txt, 'tStopRefresh')  # time at next scr refresh
        blank500_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500"-------
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blank500_txt.started', blank500_txt.tStartRefresh)
thisExp.addData('blank500_txt.stopped', blank500_txt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('find_targets.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blank3000"-------
    t = 0
    blank3000Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank3000Components = [blank3000_next_txt]
    for thisComponent in blank3000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blank3000"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank3000Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank3000_next_txt* updates
        if t >= 0.0 and blank3000_next_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank3000_next_txt.tStart = t  # not accounting for scr refresh
            blank3000_next_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blank3000_next_txt, 'tStartRefresh')  # time at next scr refresh
            blank3000_next_txt.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank3000_next_txt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            blank3000_next_txt.tStop = t  # not accounting for scr refresh
            blank3000_next_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank3000_next_txt, 'tStopRefresh')  # time at next scr refresh
            blank3000_next_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank3000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank3000"-------
    for thisComponent in blank3000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blank3000_next_txt.started', blank3000_next_txt.tStartRefresh)
    trials.addData('blank3000_next_txt.stopped', blank3000_next_txt.tStopRefresh)
    
    # ------Prepare to start Routine "count_3"-------
    t = 0
    count_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    count_3Components = [text_count_3]
    for thisComponent in count_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "count_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = count_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_count_3* updates
        if t >= 0.0 and text_count_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_count_3.tStart = t  # not accounting for scr refresh
            text_count_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_count_3, 'tStartRefresh')  # time at next scr refresh
            text_count_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_count_3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_count_3.tStop = t  # not accounting for scr refresh
            text_count_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_count_3, 'tStopRefresh')  # time at next scr refresh
            text_count_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in count_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "count_3"-------
    for thisComponent in count_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_count_3.started', text_count_3.tStartRefresh)
    trials.addData('text_count_3.stopped', text_count_3.tStopRefresh)
    
    # ------Prepare to start Routine "count_2"-------
    t = 0
    count_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    count_2Components = [text_count_2]
    for thisComponent in count_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "count_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = count_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_count_2* updates
        if t >= 0.0 and text_count_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_count_2.tStart = t  # not accounting for scr refresh
            text_count_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_count_2, 'tStartRefresh')  # time at next scr refresh
            text_count_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_count_2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_count_2.tStop = t  # not accounting for scr refresh
            text_count_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_count_2, 'tStopRefresh')  # time at next scr refresh
            text_count_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in count_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "count_2"-------
    for thisComponent in count_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_count_2.started', text_count_2.tStartRefresh)
    trials.addData('text_count_2.stopped', text_count_2.tStopRefresh)
    
    # ------Prepare to start Routine "count_1"-------
    t = 0
    count_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    count_1Components = [text_count_1]
    for thisComponent in count_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "count_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = count_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_count_1* updates
        if t >= 0.0 and text_count_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_count_1.tStart = t  # not accounting for scr refresh
            text_count_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_count_1, 'tStartRefresh')  # time at next scr refresh
            text_count_1.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_count_1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_count_1.tStop = t  # not accounting for scr refresh
            text_count_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_count_1, 'tStopRefresh')  # time at next scr refresh
            text_count_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in count_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "count_1"-------
    for thisComponent in count_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_count_1.started', text_count_1.tStartRefresh)
    trials.addData('text_count_1.stopped', text_count_1.tStopRefresh)
    
    # ------Prepare to start Routine "testRout"-------
    t = 0
    testRoutClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    testPoly.setSize(img_w_h)
    testImg.setSize(img_w_h)
    testImg.setImage(cont_path)
    # setup some python lists for storing info about the testMouse
    testMouse.x = []
    testMouse.y = []
    testMouse.leftButton = []
    testMouse.midButton = []
    testMouse.rightButton = []
    testMouse.time = []
    gotValidClick = False  # until a click is received
    testMouse.mouseClock.reset()
    crosses = []
    image.setImage(targ_path)
    # keep track of which components have finished
    testRoutComponents = [testPoly, testImg, testMouse, image]
    for thisComponent in testRoutComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testRout"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testRoutClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testPoly* updates
        if t >= 0.0 and testPoly.status == NOT_STARTED:
            # keep track of start time/frame for later
            testPoly.tStart = t  # not accounting for scr refresh
            testPoly.frameNStart = frameN  # exact frame index
            win.timeOnFlip(testPoly, 'tStartRefresh')  # time at next scr refresh
            testPoly.setAutoDraw(True)
        frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if testPoly.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            testPoly.tStop = t  # not accounting for scr refresh
            testPoly.frameNStop = frameN  # exact frame index
            win.timeOnFlip(testPoly, 'tStopRefresh')  # time at next scr refresh
            testPoly.setAutoDraw(False)
        
        # *testImg* updates
        if t >= 0.0 and testImg.status == NOT_STARTED:
            # keep track of start time/frame for later
            testImg.tStart = t  # not accounting for scr refresh
            testImg.frameNStart = frameN  # exact frame index
            win.timeOnFlip(testImg, 'tStartRefresh')  # time at next scr refresh
            testImg.setAutoDraw(True)
        frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if testImg.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            testImg.tStop = t  # not accounting for scr refresh
            testImg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(testImg, 'tStopRefresh')  # time at next scr refresh
            testImg.setAutoDraw(False)
        # *testMouse* updates
        if t >= 0.0 and testMouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            testMouse.tStart = t  # not accounting for scr refresh
            testMouse.frameNStart = frameN  # exact frame index
            win.timeOnFlip(testMouse, 'tStartRefresh')  # time at next scr refresh
            testMouse.status = STARTED
            prevButtonState = testMouse.getPressed()  # if button is down already this ISN'T a new click
        frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if testMouse.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            testMouse.tStop = t  # not accounting for scr refresh
            testMouse.frameNStop = frameN  # exact frame index
            win.timeOnFlip(testMouse, 'tStopRefresh')  # time at next scr refresh
            testMouse.status = FINISHED
        if testMouse.status == STARTED:  # only update if started and not finished!
            buttons = testMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = testMouse.getPos()
                    testMouse.x.append(x)
                    testMouse.y.append(y)
                    buttons = testMouse.getPressed()
                    testMouse.leftButton.append(buttons[0])
                    testMouse.midButton.append(buttons[1])
                    testMouse.rightButton.append(buttons[2])
                    testMouse.time.append(testMouse.mouseClock.getTime())
        if testMouse.isPressedIn(testPoly):
            crosses.append(makeCross(testMouse.getPos()))
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testRoutComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testRout"-------
    for thisComponent in testRoutComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('testPoly.started', testPoly.tStartRefresh)
    trials.addData('testPoly.stopped', testPoly.tStopRefresh)
    trials.addData('testImg.started', testImg.tStartRefresh)
    trials.addData('testImg.stopped', testImg.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('testMouse.x', testMouse.x)
    trials.addData('testMouse.y', testMouse.y)
    trials.addData('testMouse.leftButton', testMouse.leftButton)
    trials.addData('testMouse.midButton', testMouse.midButton)
    trials.addData('testMouse.rightButton', testMouse.rightButton)
    trials.addData('testMouse.time', testMouse.time)
    trials.addData('testMouse.started', testMouse.tStart)
    trials.addData('testMouse.stopped', testMouse.tStop)
    for across in crosses:
            across.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    
    # ------Prepare to start Routine "blank500"-------
    t = 0
    blank500Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank500_txt]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank500_txt* updates
        if t >= 0.0 and blank500_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank500_txt.tStart = t  # not accounting for scr refresh
            blank500_txt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blank500_txt, 'tStartRefresh')  # time at next scr refresh
            blank500_txt.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank500_txt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            blank500_txt.tStop = t  # not accounting for scr refresh
            blank500_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank500_txt, 'tStopRefresh')  # time at next scr refresh
            blank500_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blank500_txt.started', blank500_txt.tStartRefresh)
    trials.addData('blank500_txt.stopped', blank500_txt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end_routine"-------
t = 0
end_routineClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_routineComponents = [text_2]
for thisComponent in end_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_routine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_routineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_2.tStop = t  # not accounting for scr refresh
        text_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
        text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_routine"-------
for thisComponent in end_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
