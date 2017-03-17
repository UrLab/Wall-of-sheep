# Wall of sheep
See [https://www.wallofsheep.com/pages/wall-of-sheep](https://www.wallofsheep.com/pages/wall-of-sheep)

## Required logiciel:
* tcpdump
* postgresql
* create_ap

## Create the database:
    createdb wifisteal
    psql -d wifisteal -f createdb.sql

## Create the wifi:
    sudo ./create_ap wlp2s0 enp0s25 pds-wall-of-sheep urlabULB

## Steal passwd:
    sudo tcpdump -i wlp2s0 tcp port 80 -vv | python3 parse.py

## Run the webserver:
    python3 app.py
