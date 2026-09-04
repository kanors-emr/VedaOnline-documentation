@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

REM Stop the local documentation preview server (process listening on DOCS_PORT).

SET "DOCS_PORT=8000"
ECHO Stopping any process listening on port %DOCS_PORT% ...

SET "FOUND=0"
FOR /F "tokens=5" %%P IN ('NETSTAT -ANO 2^>NUL ^| FINDSTR ":%DOCS_PORT%" ^| FINDSTR "LISTENING"') DO (
    SET "FOUND=1"
    TASKKILL /PID %%P /F >NUL 2>&1
    IF NOT ERRORLEVEL 1 (ECHO   Stopped PID %%P.) ELSE (ECHO   Could not stop PID %%P.)
)

IF "!FOUND!"=="0" ECHO No listener found on port %DOCS_PORT%.
ECHO.
EXIT /B 0
