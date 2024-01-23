let totalQuestions = 10;

const selectedOptions = Array.from({totalQuestions}, (_, i) => 
    `${i+1}`).reduce((acc, key) => ({ ...acc, [key]: null }), {});

for (const key in selectedOptions) {
    console.log(`${key}: ${selectedOptions[key]}`);
}

let LoremIpsum = "Hello, World!"

const myMap = new Map([
    [ "Math", ["Math1", "fff", LoremIpsum ] ],
    [ "Physics",  ["Physics", "f00", LoremIpsum ] ],
    [ "MedicalIndustryManagement",  ["MedicalIndustryManagement", "ff0", LoremIpsum ] ]
]);

console.log(myMap.get("Math")[0]);





























