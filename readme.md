Snap for testing service startup sequencing. The service scripts just write their argument and the timestamp at the start of the script to a file at `$SNAP_COMMON/log.txt`

`seqtest.read-log` simply reads the files, sorts them by timestamp, and prints the resulting sequence.
