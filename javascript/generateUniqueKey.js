#!/usr/bin/env javascript

let generateUniqueID = () => {
    /* (i) crypto.ranomUUID is not an external package, it is built into
     * javascript. (ii) it has nothing to do with crypto currencies. */
    return crypto.randomUUID()
}

console.log(generateUniqueID())

