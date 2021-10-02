@echo off
set ver=%1
set pyver=%2
mkdir C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python%pyver%\Lib\site-packages\PySide%ver%\bin
copy C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python%pyver%\Scripts\pyside%ver%-uic.exe C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide%ver%\bin\uic.exe
