@echo off
echo.
echo ========================================
echo   PUSH VERS GITHUB
echo ========================================
echo.

REM Definir Git avec chemin complet si necessaire
set GIT_CMD=git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Program Files\Git\bin\git.exe" (
        set GIT_CMD="C:\Program Files\Git\bin\git.exe"
    )
)

echo [INFO] Verification de l'etat...
%GIT_CMD% status
echo.

set /p COMMIT_MSG="Message du commit: "

echo.
echo [INFO] Ajout des modifications...
%GIT_CMD% add .

echo [INFO] Commit...
%GIT_CMD% commit -m "%COMMIT_MSG%"

echo [INFO] Push vers GitHub...
%GIT_CMD% push

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Modifications pushees avec succes!
) else (
    echo.
    echo [ERREUR] Echec du push
    echo Verifiez vos identifiants et votre connexion
)

echo.
pause
