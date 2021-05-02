
/*       _\|/_
         (o o)
 +----oOO-{_}-OOo-------------------------------------------------------+
 |2021-04-25                                                            |
 |Sunday                                                                |
 |                                                                      |
 |WAP to rotate a string in the right direction by periodically removing|
 |one letter from the end of the string and attaching it to the front.  |
 +---------------------------------------------------------------------*/

let myString = "nikinbaidar";

console.log(`Original String: ${myString}\n`);

console.log(`Rotation from left to right: \n`);

let lengthOfMyString = myString.length;

for (let i = 0; i < lengthOfMyString; i++) {
    charToPrepend = myString.charAt(lengthOfMyString - 1);
    myString = myString.substr(0,lengthOfMyString - 1);
    myString = charToPrepend.concat(myString);
    console.log(myString);
}

/* Rotating the string from right to left */

console.log("\n");
console.log(`Rotation from right to left: \n`);

lengthOfMyString = myString.length;

for (let i = 0; i < lengthOfMyString; i++) {
    charToAppend = myString.charAt(0);
    myString = myString.substr(1,lengthOfMyString - 1);
    myString = myString.concat(charToAppend);
    console.log(myString);
}
