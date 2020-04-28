/*
You are provided with a list (or array) of integer arrays (or tuples).
Each integer array has two items which represent number of people get into bus
(The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station 
(after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, 
and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0.
So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.

https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/cpp
*/
//MY ANSWER
#include <utility>
#include <vector>

unsigned int number(const std::vector<std::pair<int, int>>& busStops){
  int t = 0;
  for (int i = 0; i < busStops.size(); i++){
    t += busStops[i].first;
    t -= busStops[i].second;
  }
  return total_people;
}

//ANOTHER ANSWER I FOUND
unsigned int number(const std::vector<std::pair<int, int>> &busStops)
{
    int passengers = 0;
    for (auto i : busStops)
        passengers += i.first - i.second;
    return passengers;
}
/* 
It used a for loop like the one I made, but it used auto...
So a for loop has the parameters => for ( range_declaration : range_expression ) 

range_declaration: a declaration of a named variable, whose type is the 
type of the element of the sequence represented by 
range_expression, or a reference to that type.
Often uses the auto specifier for automatic type 
deduction.

range_expression: any expression that represents a suitable sequence 
or a braced-init-list.
Ex: 
std::vector<int> v = {0, 1, 2, 3, 4, 5}; 
    for (auto i : v) 
        std::cout << i << ' '; 
*/
