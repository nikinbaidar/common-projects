
/************************************************************/
/* WAP to display the current day and time in the following */
/* format:                                                  */
/*                                                          */
/* Today is: Tuesday                                        */
/* Current tiem is: 10:30:38 PM                             */
/************************************************************/

let currentDateTime = new Date();

let dayOfWeek = currentDateTime.getDay();

let dayList = ["Sunday", "Monday", "Tuesday", "Wednsday",
    "Thursday", "Friday", "Saturday"]

let currentLocalTime = currentDateTime.toLocaleTimeString();

console.log("Today is: ",dayList[dayOfWeek]);
console.log("Current Time is: ",currentLocalTime);
