
let hcf = (num1,num2) => {
    if (num1 < num2)
        [num1,num2] = [num2,num1]
    while (num1 % num2 !=0){
        num3 = num2;
        num2 = num1 % num2;
        num1 = num3;
    }
    return num2;
}

let result = hcf(7,14);

console.log(result);
