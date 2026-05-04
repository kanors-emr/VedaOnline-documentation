@ECHO OFF
SETLOCAL

REM Clean + build documentation, then start the local preview server.

CALL "%~dp0build.bat"
IF ERRORLEVEL 1 EXIT /B %ERRORLEVEL%

CALL "%~dp0run.bat"
EXIT /B %ERRORLEVEL%
