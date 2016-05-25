@echo off

title Toontown 2.0 Game Launcher

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Prod Server 1
echo #3 - Prod Server 2
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TT_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    set TT_GAMESERVER=158.69.170.152
) else if %INPUT%==3 (
    SET TT_GAMESERVER=162.251.164.150
) else (
    goto selection
)

echo.

if %INPUT%==2 (
    set /P ttUsername="Username: "
) else if %INPUT%==3 (
    set /P ttUsername="Username: "
) else (
    set /P TT_PLAYCOOKIE=Username: 
)

echo.

echo ===============================
echo Starting Toontown 2.0
echo ppython: "C:\Panda3D-1.10.0\python\ppython.exe"

if %INPUT%==2 (
    echo Username: %ttUsername%
) else if %INPUT%==4 (
    echo Username: %ttUsername%
) else (
    echo Username: %TT_PLAYCOOKIE%
)

echo Gameserver: %TT_GAMESERVER%
echo ===============================

cd ../../

:main
if %INPUT%==2 (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else if %INPUT%==4 (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStartRemoteDB
) else (
    "C:\Panda3D-1.10.0\python\ppython.exe" -m toontown.toonbase.ToontownStart
)
pause

goto main
