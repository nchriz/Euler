#include <iostream>

using namespace std;

int main(void){
  int j;
  int sum = 0;

  for(j = 0; j < 1000; j++){
    sum += ((j%3)==0 || (j%5)==0) ? j : 0;

  }
  cout<<sum;

}
