//#include <iostream>
//using namespace std;

#include <stdio.h>

int main(void){
  int i = 1000;
  int a = 3, b = 5;
  int sum = 0;

  for(int j = 0; j < i; j++){
    if((a%j)==0)
      sum += j;
    else if((b%j)==0)
      sum += j;
  }
  //std::cout<<sum;
  printf("%d", sum);

  return 0;

}
