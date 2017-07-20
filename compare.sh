#!/bin/bash

#usage: compare.sh <nameofchallenge> [numberoftests]
#   assumes file formats as follows:
#
#     executable: <nameofchallenge>.py
#     
#     inputfile:  <nameofchallenge>.in || <nameofchallenge>.in1 
#     <nameofchallenge>.in2... <nameofchallenge>.in[numberoftests]
#
#     outputfile: <nameofchallenge>.out || <nameofchallenge>.out1
#     <nameofchallenge>.out2... <nameofchallenge>.out[numberoftests]


echo program file
echo
echo $1.py
echo
echo
echo results:
echo
echo

if [ $2 ]
then
  for i in `seq 1 $2`
  do
    diff <(./$1.py < $1.in$i) $1.out$i &>/dev/null
    if [ $? -eq 0 ]
    then
      echo test$i passed
    else
      echo program output
      echo
      ./$1.py < $1.in$i
      echo
      echo
      echo output file
      echo
      cat $1.out$i
      echo
      echo
    fi
  done
else
  diff <(./$1.py < $1.in) $1.out &> /dev/null
  if [ $? -eq 0 ]
  then
    echo no errors!!
  else
    echo program output
    echo
    ./$1.py < $1.in
    echo
    echo
    echo output file
    echo
    cat $1.out
    echo
    echo
  fi
fi
