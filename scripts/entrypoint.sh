#!/bin/bash
HOST="0.0.0.0"
PORT="8080"

exec uvicorn main:app --host ${HOST} --port ${PORT} --reload
