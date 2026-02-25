@echo off
echo.
echo ========================================
echo   INSTALLATION STABLE DIFFUSION WebUI
echo   Pour illustrations professionnelles
echo ========================================
echo.

REM Verifier si Git est installe
set GIT_CMD=git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Program Files\Git\bin\git.exe" (
        set GIT_CMD="C:\Program Files\Git\bin\git.exe"
        echo [INFO] Git trouve dans: C:\Program Files\Git\bin\git.exe
    ) else (
        echo [ERREUR] Git n'est pas installe!
        echo.
        echo Veuillez installer Git depuis: https://git-scm.com/download/win
        pause
        exit /b 1
    )
)

echo [OK] Git est installe
echo.

REM Creer dossier pour Stable Diffusion
set SD_DIR=C:\Users\Asmir\Desktop\stable-diffusion-webui

if exist "%SD_DIR%" (
    echo [INFO] Stable Diffusion deja installe dans %SD_DIR%
    echo.
    choice /C YN /M "Voulez-vous le reinstaller "
    if errorlevel 2 goto :launch
    if errorlevel 1 (
        echo [INFO] Suppression ancienne installation...
        rd /s /q "%SD_DIR%"
    )
)

echo [INFO] Clonage du depot Stable Diffusion WebUI...
echo.
cd C:\Users\Asmir\Desktop
%GIT_CMD% clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

if %ERRORLEVEL% NEQ 0 (
    echo [ERREUR] Echec du clonage
    pause
    exit /b 1
)

echo.
echo [OK] Stable Diffusion WebUI clone avec succes!
echo.

:launch
echo ========================================
echo   PREMIER LANCEMENT
echo ========================================
echo.
echo [INFO] Le premier lancement va:
echo   1. Telecharger Python embarque
echo   2. Installer toutes les dependances
echo   3. Telecharger le modele par defaut
echo.
echo [ATTENTION] Cela peut prendre 10-30 minutes
echo             et consommer 4-8 GB d'espace disque
echo.
choice /C YN /M "Voulez-vous lancer maintenant "
if errorlevel 2 goto :end
if errorlevel 1 (
    echo.
    echo [INFO] Lancement de Stable Diffusion WebUI...
    cd "%SD_DIR%"
    start "" webui-user.bat
    
    echo.
    echo [INFO] Une fenetre va s'ouvrir avec l'installation
    echo        Attendez que l'interface web se lance automatiquement
    echo.
    echo        URL: http://127.0.0.1:7860
    echo.
)

:end
echo ========================================
echo   INSTALLATION TERMINEE
echo ========================================
echo.
echo Pour lancer Stable Diffusion:
echo   1. Aller dans: %SD_DIR%
echo   2. Double-cliquer sur: webui-user.bat
echo   3. Ouvrir: http://127.0.0.1:7860
echo.
pause
