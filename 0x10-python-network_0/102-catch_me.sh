#!/bin/bash
# -i OPTIONS, -X PUT, -L, provides user id, curl with -d, provide origin
curl -X PUT -sLd "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
