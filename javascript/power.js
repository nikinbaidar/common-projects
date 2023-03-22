let p = (x, n) => {
    let y = ( (Math.floor(n/2) > 0) ? x * p(x, Math.floor(n/2)-1) : 1 );
    return (n % 2 == 0) ? y * y : y * y * x;
}

console.log(p(2,2));
