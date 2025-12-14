#!/bin/bash

# Run the setup script to create the DB and the schema in the DB
# Note: make sure that your password matches what is in the Dockerfile
echo "Setting up database and tables"

for i in {1..50};
do
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "${SA_PASSWORD}" -d master -i create-database.sql
    if [ $? -eq 0 ]
    then
        echo "Database created"
        break
    else
        echo "not ready yet..."
        sleep 1
    fi
done

echo "Retrieving Scryfall data"
START=$(date +%s)
curl -X GET "https://api.scryfall.com/bulk-data" > bulk-data.json
echo "downloading bulk data"
for i in 0 1 2 3 4; do URI=$(cat ./bulk-data.json | jq -r '.data[$i].download_uri') && curl -X GET $URI > $i.json; done
echo "bulk data downloaded"
echo "Scryfall download took $(($END-$START)) seconds"

START=$(date +%s)
#/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "${SA_PASSWORD}" -d master -i import-data.sql

END=$(date +%s)

echo "Setup done"

echo "Setup took $(($END-$START)) seconds"