@echo off
echo.
echo ========================================
echo   LANCEMENT STABLE DIFFUSION WebUI
echo ========================================
echo.

cd C:\Users\Asmir\Desktop\stable-diffusion-webui

if not exist "webui-user.bat" (
    echo [ERREUR] Stable Diffusion n'est pas installe!
    echo.
    echo Installez-le d'abord avec: install_stable_diffusion.bat
    pause
    exit /b 1
)

echo [INFO] Lancement de Stable Diffusion...
echo [INFO] Au premier lancement, cela peut prendre 10-30 minutes
echo        pour telecharger Python et les dependances
echo.
echo [INFO] L'interface web s'ouvrira automatiquement
echo        URL: http://127.0.0.1:7860
echo.

start "" webui-user.bat

timeout /t 15 /nobreak >nul
start http://127.0.0.1:7860

echo.
echo ========================================
echo   STABLE DIFFUSION EN COURS...
echo ========================================
echo.
echo Pour generer des images pour Max et Mila:
echo   1. Attendez que l'interface se charge
echo   2. Dans "Prompt", ecrivez votre description en anglais
echo   3. Exemple: "children's book illustration, boy on beach..."
echo   4. Cliquez sur "Generate"
echo.
pause
