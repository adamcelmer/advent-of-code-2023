#!/bin/bash

sum=0
while read -r line; do
  only_nums="$(echo $line | sed 's/[a-zA-Z]//g')"
  num_first=${only_nums:0:1}
  num_last=${only_nums: -1}
  num="${num_first}${num_last}"
  sum=$(($sum + $num))
done < input.txt

echo "$sum"