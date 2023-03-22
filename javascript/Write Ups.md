## JS Write ups

{{{javascript

// 1

// Inverting key-value pairs of an object, without mutating it.

```javascript
const invertKeyValues = (obj, fn) =>
    Object.keys(obj).reduce((acc,key) => {
        const val = fn ? fn(obj[key]) : obj[key];
        acc[val] = acc[val] || []
        acc[val].push(key);
        return acc;
        }, {});

console.log(invertKeyValues({x:1,y: 2, z:1 }));
console.log(invertKeyValues({x:1,y: 2, z:1 },value => 'group' + value));
```


/* Output:

{ '1': ['x', 'z'], '2': ['y'] }
{ group1: ['x', 'z'], group2: ['y']

= Insights: =

- `=>` is a new feature in JS which was introduced in ES6. It is
  called an arrow function. The left part denotes the input and the
  right part  denotes the output of that function. {comprehend as a
  functional programming technique}.

- Object.keys(obj) returns an array of all the keys of the object obj.

- The corresponding inverted value of each inverted key is an array of
  keys responsible for generating the inverted value.

- If a function is supplied, it is applied to each inverted key

*/

/*       _\|/_
         (o o)
 +----oOO-{_}-OOo----------------------------------------------------------+
 |Is it possible to create two functions A and B such that                 |
 |                                                                         |
 |       new A() === new B()?                                              |
 |                                                                         |
 |Meaning,                                                                 |
 |                                                                         |
 |    function A() {...}                                                   |
 |    function B() {...}                                                   |
 |                                                                         |
 |    let objectA = new A;                                                 |
 |    let objectB = new B;                                                 |
 |                                                                         |
 |    let result = (objectA === objectB)                                   |
 |    // true if both functions return the "same object"                   |
 |                                                                         |
 |If result is true, then provide an example code for constructors A and B.|
 +------------------------------------------------------------------------*/

objectNull = {};

function A() {

    return objectNull;
}

function B() {
    return objectNull;
}

let objectA = new A;
let objectB = new B;

let result =  objectA === objectB;

console.log(result);

}}}
