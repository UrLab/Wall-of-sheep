# Wall of sheep
See [https://www.wallofsheep.com/pages/wall-of-sheep](https://www.wallofsheep.com/pages/wall-of-sheep)

## Required logiciel:
* tcpdump
* postgresql
* create_ap

## Create the database:
    createdb wifisteal
    psql -d wifisteal -f createdb.sql


## Steal passwd:
    sudo tcpdump -i wlp2s0 tcp port 80 -vv | python parse.py


## Run the webserver:
    export FLASK_APP=app.py
    flask run
