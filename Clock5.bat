@echo off
echo Setup virtual environment
if not exists venv goto :novenv
call :activate
echo Starting Clock5
python Clock5.py
pause
goto :end
:novenv
echo Installing dependencies
python -m venv venv
call :activate
pip install PyQt5
pip install geopy
pip install geocoder
pip install requests
pause
goto :end
:activate
call venv\Scripts\activate.bat
exit /b
