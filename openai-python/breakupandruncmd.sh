#!/bin/bash
# This script is used to break up a command into multiple lines and run openai on it
#
# Usage: breakupandruncmd.sh <command>
# Example: breakupandruncmd.sh "echo hello world"
# Example: breakupandruncmd.sh "echo hello world && echo goodbye world"


if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    echo "Usage: breakupandruncmd.sh <cmdstring> <inputfile>"
    exit 1
fi

cmdstring=$1
inpfile=$2
mkdir -p "data/$inpfile.split"
cd data/$inpfile.split
pwd
rm *
split -b 1000 "../$inpfile" segment
ls -l 
cd ../..

# for FILE in data/$inpfile.split/*;/usr/local/bin/python3 cmdfile.py $cmdstring $FILE >> new.txt
# for FILE in data/$inpfile.split/*;echo cmdfile.py $cmdstring $FILE >> new.txt
for FILE in data/$inpfile.split/*; do ls -l $FILE ; done
echo "" > data/$inpfile.result.txt
for FILE in data/$inpfile.split/*; do ls $FILE && python3 cmdfile.py "Summarize this text: " $FILE >> data/$inpfile.result.txt; done
ls -lrt data/$inpfile.result.txt
python3 cmdfile.py "Summarize and Explain the the top points from this article as top 10 bullets : " data/$inpfile.result.txt

