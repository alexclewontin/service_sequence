#!/bin/bash
START=$(date +%s.%N)
echo -e $1' '$START >> $SNAP_COMMON/log.txt
