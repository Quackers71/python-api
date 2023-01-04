# python-api
### Python API Development - Comprehensive Course for Beginners
- https://youtu.be/0sOvCWFmrtA

Setting up your Virtual Env on Windows
- https://youtu.be/0sOvCWFmrtA?t=1475
- Run the below commands in bash then check the (venv) C:\... in CMD
```
cd {project dir}
py -3 -m venv {name}
venv/Scripts/activate.bat
```
- From View > Command Palette - check the '.\fastapi\venv\Scripts\python.exe' is selected as per below :</br></br>
![](./python-interpreter-path.png)</br></br>
- https://fastapi.tiangolo.com/tutorial/</br>
Install Fastapi with all the dependencies with the command below (in Bash):
```
pip install fastapi[all]
pip freeze # to list all the installed packages
```
To run your App (in Bash):
```
$ uvicorn main:app
INFO:     Started server process [5816]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:52533 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:52533 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```
Then goto : http://127.0.0.1:8000 and you should receive :</br></br>
{"message":"Hello World"}</br>
