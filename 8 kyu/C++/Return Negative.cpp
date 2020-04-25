// Returns the negative of the input, but if it's already negative or it's 0 return the input
// 8 kyu

int makeNegative(int num)
{
  if(num > 0){
    int x;
    x = num - (num+num);
    return x;
  } else {
    return num;
  }
  return 0;
}
