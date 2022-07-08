Konv Mini Bank



How to use

Make sure you have docker, docker-composed and git installed on your machine by typing in your command prompt:
```
$ docker -v
Docker version 20.10.17, build 100c701
$ docker-compose -v
docker-compose version 1.29.2, build 5becea4c
$ git --version ..
git version 2.36.1.windows.1
```
It should provide the installed versions

SE NÃO ESTIVER INSTALADO, DIZER O QUE FAZER

Clone the repo
```
git clone ...
```

Create virtual environment
```
$ python -m venv konv_bank_venv
```
Create virtual environment
```
$ pip install -r requirements.txt
```

Download image and run container
```
$ docker-compose up
```

After those steps, the container with the database should be running and connected to your system, and the aplication is ready to run


HOW TO USE

From applications directory, activate the virtual environment

```
$ konv_bank_venv\Scrips\activate [Windows] 
or
$ konv_bank_venv\bin\activate [Linux/Mac] 
```

To start it on your console, just run "main.py" file:

```
$ python main.py
```