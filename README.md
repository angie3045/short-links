# Requirements
- Python 3.7.6
- Make sure we have the requirements installed in your python or virtual environment
```
pip install -r requirements.txt
```
- Make sure you are using the pip for the correct python version, or the correct virtual environment while running the previous command

# How to run it
In windows
   ``` 
    set FLASK_APP=url_shorter.py
    flask run
   ``` 
In Linux
  ``` 
   export FLASK_APP=url_shorter
   flask run
   ``` 
In Pycharm...
In edit configurations
1. Switch "Script Path" to "Module Name"
2. In the module add: flask
3. In the parameters add: run
4. In the environment variables add FLASK_APP=url_shorter
![alt text](Pycharm.png)


Once Running open the URL displayed


# short-links
