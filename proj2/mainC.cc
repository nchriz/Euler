#include <iostream>
#include <math.h>

using namespace std;

int main(void){
  int n = 4*pow(10,6);
  int sum = 0;

  int x = 1, y = 1;
  int tmp;

  while(y < n){
    tmp = x;
    x = y;
    y = y + tmp;

    sum += ((y%2)==0) ? y : 0;
  }

  cout << sum;
}
