/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // 1. Initialize an empty array to store the results
    const returnedArray = [];
    
    // 2. Loop through every element in the input array
    for (let i = 0; i < arr.length; i++) {
        // 3. Call the function with the element and the index
        // 4. Push the result into our new array
        returnedArray.push(fn(arr[i], i));
    }
    
    // 5. Return the transformed array
    return returnedArray;
};