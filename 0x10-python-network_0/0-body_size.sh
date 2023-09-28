#!/bin/bash
# Sends a request to get the wc of the HTTP response
curl -s "$1" | wc -c
