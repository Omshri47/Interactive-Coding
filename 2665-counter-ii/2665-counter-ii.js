/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let currentCount = init;

    return {
        increment: function() {
            return ++currentCount;
        },
        
        decrement: function() {
            return --currentCount;
        },
        reset: function() {
           
            currentCount = init;
            return currentCount;
        },
    };
};