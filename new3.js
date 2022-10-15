/*
Identify and Callout
The function takes an integer array. Return the maximum number of integers required to form a sequence in the given array



For example: If arr contains [4, 2, 7] then the output should be 3 as three numbers would be needed in the array to make a sequence (3,5,6).



Note: The array may have duplicate elements.For example if the arr is [5,7,9,9] then the output should be 2 as two numbers would be needed in the array to make a sequence (5,6,7,8,9,9)



Note 2: Negative numbers may be present in the array and no array will have less than 2 elements.

Examples
Input: [4,2,1]
Output: 1
Input: [-3,1,5,1]
Output: 6
*/


function IdentifyAndCallout(arr) {
    //return an integer here
    let result = 0;
    let max = Math.max(...arr);
    let min = Math.min(...arr);
    for (let i = min; i <= max; i++) {
        if (!arr.includes(i)) {
            result++;
        }
    }
    return result;
}

console.log(IdentifyAndCallout(readline()));