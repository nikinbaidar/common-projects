#! /bin/bash
# A script to take N site & userName inputs and genereate 16 character long
# random passwords for these accounts. The passwords get appended to usernames
# with the pipe character (|) as the delimeter. The corresponding
# "site=username|password" entries are saved in a plain text file named secret.txt.
# Once all passwords are saved, this script encrypts the file using AES-256
# (Advanced Encryption Stanrad-256) in CBC (Cipher Block Chaining) mode. This
# algorithm generates a SEK (Secure Encryption Key) using PBKDF2
# (Password-Based Key Derivation Function 2) mechanism. Delete the original
# palin text file and move the encrypted file to a place that is easily
# accessible (something like Dropbox).

echo -n "Number of inputs = "
read totalInputs
inputCount=0

## Generate Passwords
while (( inputCount < ${totalInputs} ))
do
  echo -ne "\nEnter the site:- " 
  read site
  echo -n "Enter the username:- " 
  read username
  password=$(mktemp -u XXXXXXXXXXXXXXXX)
  echo "${site}=${username}|${password}" >> unencrypted
  (( inputCount++ ))
done

## Encrypt
while true
do
  echo 
  if openssl enc -base64 -aes-256-cbc -pbkdf2 \
    -in unencrypted -out secret.txt 2> /dev/null
  then
    break
  fi
done

rm unencrypted

# Uncomment the following line to move the encrypted to filet to Dropbox
# mv ./secret.txt ~/Dropbox
