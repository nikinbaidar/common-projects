
/********************************************************/
/* WAP to print the time of day the in 12-hours format. */
/*                                                      */
/* For example,                                         */
/*                                                      */
/*  Current Time is: 00:30 AM                           */
/*  Current Time is: 1:20 PM                            */
/********************************************************/

/* 00 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
   12 1 2 3 4 5 6 7 8 9 10 11 12 01 02 03 04 05 06 07 08 09 10 11 */

let currentDateTime = new Date();

let hoursIntoDay = currentDateTime.getHours();
let minutesIntoHours = currentDateTime.getMinutes() + 15;

let period = (hoursIntoDay < 12) ? "AM" : "PM";

if (hoursIntoDay > 12) {
    hoursIntoDay -= 12;
}

console.log(`Current Time is: ${hoursIntoDay}:${minutesIntoHours} ${period}`);
