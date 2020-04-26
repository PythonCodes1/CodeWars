// We need a function that can transform a number into a string.

#include <string>

std::string number_to_string(int num) {
  std::string s = std::to_string(num);
  return s;
}
