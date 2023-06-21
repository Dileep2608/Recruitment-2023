#!/bin/sh

file='users.txt'
final='edited_users.txt'
grep -o '= .*' $file | cut -c 3- > $final

K=553
M=828
U=723
H=698

KISHKINDHA_COUNT=0
MADRA_COUNT=0
USINARA_COUNT=0
HEHEYA_COUNT=0
TOTAL=0

while read line; do
a="$line"

if [ $a -eq $K ]
then 
    KISHKINDHA_COUNT=$((KISHKINDHA_COUNT+1))
elif [ $a -eq $M ]
then 
    MADRA_COUNT=$((MADRA_COUNT+1))
elif [ $a -eq $U ]
then 
    USINARA_COUNT=$((USINARA_COUNT+1))
elif [ $a -eq $H ]
then 
    HEHEYA_COUNT=$((HEHEYA_COUNT+1))
fi

done < $final

TOTAL=$(($KISHKINDHA_COUNT+$MADRA_COUNT+$USINARA_COUNT+$HEHEYA_COUNT))
echo "Number of people from Kishkindha kingdom = $KISHKINDHA_COUNT"
echo "Number of people from Madra kingdom      = $MADRA_COUNT"
echo "Number of people from Usinara kingdom    = $USINARA_COUNT"
echo "Number of people from Heheya kingdom     = $HEHEYA_COUNT"
echo "Total number of people from above four kingdom = $TOTAL"