// Find the largest set of numbers the length of 5 decimal places in a big number.

function solution(digits){
  if (digits.length <= 5) return Number(digits);
  debugger;
  return Math.max(Number(digits.substr(0, 5)), solution(digits.substr(1)));
}
