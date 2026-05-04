@ECHO OFF
SETLOCAL

REM Build Sphinx HTML documentation (output: build\html)
REM 1) Runs "clean" first — removes the Sphinx build tree (including doctrees / pickled
REM    environment cache) so the next build is from a fresh state.
REM 2) Runs "html" for a full rebuild.

PUSHD "%~dp0"

IF "%SPHINXBUILD%"=="" SET SPHINXBUILD=sphinx-build

%SPHINXBUILD% >NUL 2>NUL
IF ERRORLEVEL 9009 (
    ECHO.
    ECHO The 'sphinx-build' command was not found. Install Sphinx, e.g.:
    ECHO   python -m pip install -r source\requirements.txt sphinx
    ECHO.
    POPD
    EXIT /B 1
)

ECHO Cleaning previous Sphinx build output...
%SPHINXBUILD% -M clean source build %SPHINXOPTS% %O%

ECHO Building HTML...
REM -a writes every HTML page so the global sidebar stays in sync after toctree or title changes
REM   (incremental sphinx-build can otherwise leave older nav text in unrelated pages).
%SPHINXBUILD% -M html source build -a %SPHINXOPTS% %O%
SET "ERR=%ERRORLEVEL%"

POPD

IF NOT "%ERR%"=="0" EXIT /B %ERR%
ECHO.
ECHO Build finished. Output: build\html\
ECHO Preview: run run.bat or build-and-run.bat
ECHO.
EXIT /B 0
