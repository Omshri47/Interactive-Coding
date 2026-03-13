/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    // Initialize a cache to store results
    const cache = new Map();

    return function(...args) {
        // Create a unique key based on the arguments
        const key = JSON.stringify(args);

        // Check if the result is already in the cache
        if (cache.has(key)) {
            return cache.get(key);
        }

        // Otherwise, call the function and store the result
        const result = fn(...args);
        cache.set(key, result);

        return result;
    }
}

/** * Example usage:
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 * return a + b;
 * })
 * memoizedFn(2, 2) // 4
 * memoizedFn(2, 2) // 4
 * console.log(callCount) // 1 
 */