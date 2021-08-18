Snap for testing service startup sequencing. The service scripts just write their argument and the timestamp at the start of the script to a file at `$SNAP_COMMON/<order>_log.txt_`, where `<order>` is either 'before' or 'after', and indicates how the services were sequences in the snapcraft.yaml

`parse.py` simply reads the files, sorts them by timestamp, and prints the resulting sequence.
