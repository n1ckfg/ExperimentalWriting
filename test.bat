@echo off

cd /D %~dp0

set PROMPT=%1

rem min:0, max:1.5
set TEMPERATURE=1.35

rem min:0.8, max:0.99
set TOP_P=0.97 

rem min:1, max:1.5
set REPETITION_PENALTY=1.1

rem min:1, max:3
set BATCH_SIZE=3

rem min:256, max:2048
set MAX_LENGTH=512 

python test.py -- %PROMPT% %TEMPERATURE% %TOP_P% %REPETITION_PENALTY% %BATCH_SIZE% %MAX_LENGTH%  
@pause


