#include <iostream>

using namespace std;

int main(){

  int n = 2520;
  int i;
  int canrun = 1;
  while(canrun){
    canrun = 0;
    n += 20;
    for(i = 1; i < 20; i++)
      canrun += (n%i)==0 ? 0 : 1;
  }
  cout << n;
}
