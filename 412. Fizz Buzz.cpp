// Write a program that outputs the string representation of numbers from 1 to n.

// But for multiples of three it should output “Fizz” instead of the number and for the multiples of 
// five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

// Example:

// n = 15,

// Return:
// [
//     "1",
//     "2",
//     "Fizz",
//     "4",
//     "Buzz",
//     "Fizz",
//     "7",
//     "8",
//     "Fizz",
//     "Buzz",
//     "11",
//     "Fizz",
//     "13",
//     "14",
//     "FizzBuzz"
// ]



class Solution {
public:
    vector<string> fizzBuzz(int n) {
        // Check if i is a multiple of 15, 3, 5, or neither of them,
        // and push_back the result to the result vector
        // Time complexity:  O(n)
        // Space complexity: O(n)
        
        vector<string> ans;
        for (int i=1; i<=n; i++){
            if (i%15==0){
                ans.push_back("FizzBuzz");
            }else if (i%3==0){
                ans.push_back("Fizz");
            }else if (i%5==0){
                ans.push_back("Buzz");
            }else{
                ans.push_back(to_string(i));
            }
        }
        return ans;
    }
};




