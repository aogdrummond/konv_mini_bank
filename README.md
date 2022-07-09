# Konv Mini Bank



## **Installation**

### Make sure you have docker, docker-composed and git installed on your machine by typing in your command prompt: 

&nbsp;
```
$ python --version
$ docker -v
$ docker-compose -v
$ git --version
$ pip --version
```

### It should provide the installed versions. If any of them is not available to the system yet, install it beforehand.



&nbsp;

### Clone the repository with source code.

```
$ git clone https://github.com/aogdrummond/konv_mini_bank.git
```
&nbsp;
### Create virtual environment.
```
$ python -m venv konv_bank_venv
```
&nbsp;
### Install virtual environment dependencies.
```
$ pip install -r requirements.txt
```
&nbsp;
### Download image and run container.
```
$ docker-compose up
```
&nbsp;
### After those steps, the container with the database should be running and connected to your system, and the aplication is ready to run.



### From applications directory, activate the virtual environment.

```
$ konv_bank_venv\Scrips\activate [Windows] 
or
$ konv_bank_venv\bin\activate [Linux/Mac] 
```
&nbsp;


## **How to use**
* ### To start it on your console, just run "main.py" file:
```
$ python main.py
```

* ### To use it just follow the commands in the console, like in the example below: 

&nbsp;

<img src="img\usage_flow.png"
     style="float: right; margin-right: 60px;"
/>
