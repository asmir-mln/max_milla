@echo off
echo.
echo ========================================
echo   DEMARRAGE SERVEUR MAX ET MILA
echo ========================================
echo.

REM Verifier si Apache est deja lance
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [OK] Apache est deja en cours d'execution
    goto :open_browser
)

REM Demarrer Apache
echo [INFO] Demarrage d'Apache...
cd /d C:\xampp
start /B apache_start.bat

REM Attendre que le serveur demarre
timeout /t 3 /nobreak >nul

REM Verifier si Apache a demarre
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [OK] Apache demarre avec succes!
) else (
    echo [ERREUR] Impossible de demarrer Apache
    echo Veuillez ouvrir XAMPP Control Panel manuellement
    pause
    exit /b 1
)

:open_browser
echo.
echo [INFO] Ouverture de l'interface web...
timeout /t 2 /nobreak >nul

REM Ouvrir le navigateur
start http://localhost/max_mila_livre/api_test.html

echo.
echo ========================================
echo   SERVEUR PRET!
echo ========================================
echo.
echo   Interface API: http://localhost/max_mila_livre/api_test.html
echo   Visualiseur:    http://localhost/max_mila_livre/books.html
echo   API Doc:        http://localhost/max_mila_livre/api.php
echo.
echo ========================================
echo.
pause
