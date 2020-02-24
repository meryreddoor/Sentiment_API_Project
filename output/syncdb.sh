#!/bin/bash


LOCAL_DB="mongodb://localhost/emotions"

# Load REMOTE_DB env variable
source .private.env

echo "Importing from local db: $LOCAL_DB"
echo "\t ...to remote: $REMOTE_DB"

mongodump --uri=$LOCAL_DB
mongorestore --uri=$REMOTE_DB 