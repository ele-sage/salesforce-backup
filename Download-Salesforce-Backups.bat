@echo off
setlocal

docker ps >nul 2>&1
if errorlevel 1 (
    echo Docker Desktop is not running.
    echo Start Docker Desktop and try again.
    exit /b 1
)

docker-compose -v >nul 2>&1
if errorlevel 1 (
    echo docker-compose is not installed.
    echo Install docker-compose and try again.
    exit /b 1
)

docker-compose up -d
exit /b 0