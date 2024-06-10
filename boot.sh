#!/bin/bash

echo "Would you like to play rock-paper-scissors? (yes/no)"
read answer

if [ "$answer" == "yes" ]; then
    python rock_paper_scissors.py
else
    echo "That's too bad, maybe next time."
fi
