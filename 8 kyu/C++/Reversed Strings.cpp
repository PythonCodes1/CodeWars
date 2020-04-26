// Complete the solution so that it reverses the string value passed into it.

#include <string>
#include <algorithm>
using namespace std;

string reverseString(string str)
{
    reverse(str.begin(), str.end());
    return str;
}
