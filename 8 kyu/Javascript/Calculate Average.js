// Write function avg which calculates average of numbers in given list.

function find_average(array) {
  var sum = 0;
  array.forEach(function(x){
    sum+=x;
  });
  return sum/array.length;
}
