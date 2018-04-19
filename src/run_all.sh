#!/bin/bash

trap finish EXIT

echo "Starting sensors..." 

files=("control_loop.py" "relay.py" "rotary.py" "screen.py" "temp.py") 
pids=()

for f in "${files[@]}"
do 
	echo "filename = " $f
	./$f &
	pids+=($!)
done


function finish {
	echo "cleaning up..."
	for p in "${pids[@]}"
	do
		echo "killing " $p
		kill $p
	done
}

sleep infinity
exit 0


