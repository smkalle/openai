# Path: imagegen.sh
#!/bin/bash
while read line
    
do
    python3 imagegen.py "$line"
done < "$1"

    
