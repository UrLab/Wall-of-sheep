# Wall of sheep


## Create the database:
    createdb wifisteal
    psql -d wifisteal -f createdb.sql


## Steal passwd:
    sudo tcpdump -i wlp2s0 tcp port 80 -vv | python parse.py


## Run the webserver:
   export FLASK_APP=app.py
   flask run
