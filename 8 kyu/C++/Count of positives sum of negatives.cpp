/*
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
*/


#include <vector>
#include <utility>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.size() == 0)
      return {};
    std::vector<int> end(2);
    for (auto x : input){
      if (x > 0)
        end[0]++;
      if (x < 0)
        end[1] += x;
    }
    return end;
}

//ANOTHER ANSWER
std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty())
        return {};
    int countPositives{0}, sumNegatives{0};
    for (int x : input)
        x > 0 ? countPositives++ : (x != 0 ? sumNegatives += x : 0);
    return {countPositives, sumNegatives};
}
// This one was a little more complex, But I really love this type of condition using the ? and :
// x > 0 ? countPositives++ : (x != 0 ? sumNegatives += x : 0);
// This is a very smart type of nested condition
