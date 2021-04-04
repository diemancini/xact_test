# XACT Test

A backend (Django) and frontend (Quasar) test to Xact.

## Instalation

This application was developed on Linux Ubuntu 20.04. For carrying out this application, you need to have already installed these frameworks:

* Docker (https://www.docker.com/)
* Docker-Compose (https://docs.docker.com/compose/install/)

For install the application, follow these steps bellow:

* Clone the application from github with:

```bash
      git clone https://github.com/diemancini/xact_test.git
```

* Run these commands on terminal :
```bash
    cd 'path_to_root_application/xact'
    docker-compose build
    docker-compose up
```
    
    
After executing the above-mentioned commands, open a browser and put on address bar the following link
```bash
    http://localhost:8080/#/variables
```

Select Boolean or String options from select tag (Boolean or String) and you should visualise a list with the type, name and value columns.
