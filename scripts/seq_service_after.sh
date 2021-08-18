#!/bin/bash
START=$(date +%s.%N)
echo $?":\t"$START >> $SNAP_COMMON/after_log.txt
