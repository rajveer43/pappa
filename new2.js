/*
Repeating Sequence
Have the function take the str parameter being passed and return a compressed version. This algorithm works by taking the occurrence of repeating character and outputting the repeating number along with a single character. For example: "aabbbcc" would return 2a3b2c. The string will not contain any numbers, punctuation, or symbols.

Examples
Input: "aabbcde"
Output: 2a2b1c1d1e
Input: "wwwwbbbw"
Output: 4w3b1w

*/

function RepeatingSequence(str) {
    let result = "";
    let count = 1;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === str[i + 1]) {
            count++;
        } else {
            result += count + str[i];
            count = 1;
        }
    }
    return result;
}

console.log(RepeatingSequence(readline()));