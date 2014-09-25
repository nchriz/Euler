#include <iostream>

using namespace std;

int main(){

  int a = 0, b = 0;
  int i;
  for(i = 1; i <= 100; i++)
    b += (a+=i*i, i);
  cout << b*b - a;

}
