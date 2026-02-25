@echo off
echo.
echo ========================================
echo   INITIALISATION DEPOT GITHUB
echo   Max et Mila - Livre pour Enfants
echo ========================================
echo.

REM Definir Git avec chemin complet si necessaire
set GIT_CMD=git
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Program Files\Git\bin\git.exe" (
        set GIT_CMD="C:\Program Files\Git\bin\git.exe"
    ) else (
        echo [ERREUR] Git n'est pas installe!
        pause
        exit /b 1
    )
)

echo [INFO] Verification de Git...
%GIT_CMD% --version
echo.

REM Verifier si deja initialise
if exist ".git" (
    echo [INFO] Depot Git deja initialise
    echo.
    choice /C YN /M "Voulez-vous reinitialiser "
    if errorlevel 2 goto :configure
    if errorlevel 1 (
        echo [INFO] Suppression ancien depot...
        rmdir /s /q .git
    )
)

echo [INFO] Initialisation du depot Git...
%GIT_CMD% init
echo.

:configure
echo [INFO] Configuration Git...
echo.
echo [IMPORTANT] Entrez vos informations GitHub:
echo.

set /p GIT_NAME="Votre nom (ex: Asmir MLN): "
set /p GIT_EMAIL="Votre email GitHub (ex: asmir@example.com): "

%GIT_CMD% config user.name "%GIT_NAME%"
%GIT_CMD% config user.email "%GIT_EMAIL%"

echo.
echo [OK] Configuration terminee
echo     Nom: %GIT_NAME%
echo     Email: %GIT_EMAIL%
echo.

echo [INFO] Ajout des fichiers...
%GIT_CMD% add .
echo.

echo [INFO] Premier commit...
%GIT_CMD% commit -m "Initial commit: Max et Mila - Livre pour enfants avec IA"
echo.

echo ========================================
echo   CREATION DU DEPOT SUR GITHUB
echo ========================================
echo.
echo [IMPORTANT] Avant de continuer:
echo.
echo 1. Allez sur: https://github.com/new
echo 2. Nom du repo: max-mila-livre
echo 3. Description: Livre pour enfants avec illustrations IA - Amazon KDP
echo 4. Cochez: Public (ou Private si vous preferez)
echo 5. NE COCHEZ PAS: Add README, .gitignore, ou license
echo 6. Cliquez sur "Create repository"
echo.

pause

echo.
echo [INFO] Entrez l'URL de votre depot GitHub:
echo Exemple: https://github.com/VOTRE_USERNAME/max-mila-livre.git
echo.

set /p GITHUB_URL="URL du depot: "

echo.
echo [INFO] Ajout de l'origine distante...
%GIT_CMD% remote add origin %GITHUB_URL%
echo.

echo [INFO] Verification de la branche...
%GIT_CMD% branch -M main
echo.

echo [INFO] Push vers GitHub...
echo [ATTENTION] Vous devrez peut-etre entrer vos identifiants GitHub
echo.

%GIT_CMD% push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo   SUCCESS - DEPOT CREE!
    echo ========================================
    echo.
    echo Votre projet est maintenant sur GitHub:
    echo %GITHUB_URL%
    echo.
    echo Prochaines etapes:
    echo   1. Visitez votre repo sur GitHub
    echo   2. Ajoutez des topics: children-book, ai-illustrations, amazon-kdp
    echo   3. Editez la description si necessaire
    echo   4. Partagez votre projet!
    echo.
) else (
    echo.
    echo [ERREUR] Echec du push
    echo.
    echo Solutions possibles:
    echo   1. Verifiez l'URL du depot
    echo   2. Verifiez vos identifiants GitHub
    echo   3. Si erreur d'authentification:
    echo      - Utilisez un Personal Access Token
    echo      - Allez sur: https://github.com/settings/tokens
    echo      - Generer un nouveau token (classic)
    echo      - Utilisez le token comme mot de passe
    echo.
)

echo ========================================
echo   COMMANDES GIT UTILES
echo ========================================
echo.
echo Ajouter des modifications:
echo   git add .
echo   git commit -m "Description des changements"
echo   git push
echo.
echo Voir l'etat:
echo   git status
echo.
echo Voir l'historique:
echo   git log --oneline
echo.
echo Creer une branche:
echo   git checkout -b nom-branche
echo.

pause
