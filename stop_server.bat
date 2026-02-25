@echo off
echo.
echo ========================================
echo   ARRET SERVEUR MAX ET MILA
echo ========================================
echo.

REM Verifier si Apache est lance
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if NOT "%ERRORLEVEL%"=="0" (
    echo [INFO] Apache n'est pas en cours d'execution
    goto :end
)

echo [INFO] Arret d'Apache...
cd /d C:\xampp
call apache_stop.bat

REM Attendre l'arret complet
timeout /t 2 /nobreak >nul

REM Verifier si Apache est arrete
tasklist /FI "IMAGENAME eq httpd.exe" 2>NUL | find /I /N "httpd.exe">NUL
if NOT "%ERRORLEVEL%"=="0" (
    echo [OK] Apache arrete avec succes!
) else (
    echo [ATTENTION] Certains processus Apache sont encore actifs
    echo Tentative d'arret force...
    taskkill /F /IM httpd.exe >nul 2>&1
    echo [OK] Processus arretes
)

:end
echo.
echo ========================================
echo   SERVEUR ARRETE
echo ========================================
echo.
pause
