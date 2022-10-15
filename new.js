/*
Function GoldPicker(arr) takes an array of numbers reflecting value of gold over time. What is the most money you can make by trading gold once over a duration.



For example: if arr is [46, 40, 31, 25, 34, 36, 37, 45, 12] then your program should return 20 because at index 3 the gold was worth $25 and at index 7 the stock was then worth $45.



If there is no money that could have been made with the gold prices, then your program should return -1. For example: arr is [11, 10, 7, 1] then your program should return -1.

Examples
Input: [10,12,4,5,9]
Output: 5
Input: [14,20,4,12,5,11]
Output: 8

*/

function GoldQuestion(arr) {
    //return an array here
    let max = 0;
    let min = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] - min > max) {
            max = arr[i] - min;
        }
    }
    if (max === 0) {
        return -1;
    }
    return max;
    
}

console.log(GoldQuestion(readline()));