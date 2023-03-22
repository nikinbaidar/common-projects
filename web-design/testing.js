/* Function defs */

const displayShadow = function() {
    this.style.boxShadow =  "-5px 5px var(--foreground)";
    this.style.transform = "translate(8px, -8px)"
}

const removeShadow = function() {
    this.style.boxShadow = "None";
    this.style.transform = "translate(0)";
}


const displayAlert = () => alert("You just clicked me.")


const updateOptions = () => {
    let index = 0;
    let sem = semesters.options[semesters.selectedIndex];
    let subjects = course.get(sem.value);

    for (match of anchors) {
        match.innerHTML = subjects[index++];
    }
}

// Main

/* Init things */

let match;

// Implement JSON instead?
const course = new Map([
    [ "1", ["1" , "2" , "3" , "4" , "5" , "6"] ],
    [ "2", ["7" , "8" , "9" , "10", "11", "12"] ],
    [ "3", ["13", "14", "15", "16", "17", "18"] ],
    [ "4", ["19", "20", "21", "22", "23", "24"] ],
    [ "5", ["25", "26", "27", "28", "29", "30"] ],
    [ "6", ["31", "32", "33", "34", "35", "36"] ],
    [ "7", ["37", "38", "39", "40", "41", "42"] ],
    [ "8", ["43", "44", "45", "46", "47", "48"] ]
]);

const options  = document.getElementsByClassName('grid-item'); 
const anchors  = document.querySelectorAll('.options p'); 
const semesters = document.getElementById("semesters");

updateOptions();

/* Add event listeners */

for (match of options) {
    match.onmousemove = displayShadow;
    match.onmouseout = removeShadow;
    match.onclick = displayAlert;
}

semesters.onchange = updateOptions;
