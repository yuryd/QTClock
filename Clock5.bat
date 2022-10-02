@echo off
if not exist venv goto :novenv
call :activate
echo Starting Clock5
python Clock5.py
pause
goto :end
:novenv
echo Setup virtual environment
python -m venv venv
call :activate
echo Installing dependencies
pip install PyQt5
pip install geopy
pip install geocoder
pip install requests
pause
goto :end
:activate
echo Switch to virtual environment
call venv\Scripts\activate.bat
exit /b
