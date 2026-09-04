@ECHO OFF
SETLOCAL

REM Start local preview of the built documentation (static site, not Veda Online itself).
REM Opens a new console window for the server, then opens the URL in your default browser.

SET "DOCS_PORT=8000"
PUSHD "%~dp0"

IF NOT EXIST "build\html\index.html" (
    ECHO No build found. Run build.bat first.
    POPD
    EXIT /B 1
)

python --version >NUL 2>&1
IF ERRORLEVEL 1 (
    ECHO Python was not found on PATH.
    POPD
    EXIT /B 1
)

ECHO Starting documentation preview at http://127.0.0.1:%DOCS_PORT%/
ECHO Close that window or run stop.bat to stop.
START "Veda Online Documentation" /D "%CD%" CMD /K python -m http.server %DOCS_PORT% --directory build\html

REM Brief wait so the server is listening before the browser opens
TIMEOUT /T 2 /NOBREAK >NUL
START "" "http://127.0.0.1:%DOCS_PORT%/"

POPD
EXIT /B 0
