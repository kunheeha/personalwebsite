#!/bin/bash

echo Migration message: 

read MESSAGE

export FLASK_APP=personalwebsite

flask db migrate -m $MESSAGE
