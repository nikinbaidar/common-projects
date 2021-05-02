
const invertKeyValues = (obj, fn) =>
    Object.keys(obj).reduce((acc,key) => {
        const val = fn ? fn(obj[key]) : obj[key];
        acc[val] = acc[val] || [];
        acc[val].push(key);
        return acc;
        }, {});

console.log(invertKeyValues({x:1,y: 2, z:1 }));
console.log(invertKeyValues({x:1,y: 2, z:1 },value => 'group' + value));
