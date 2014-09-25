#include <iostream>

using namespace std;

int isPrime(int x){
  int i;
  for(i < 2; i < x; i++)
    if((x%i)==0)
      return false;
  return true;
}

int main(){

  long long num = 600851475143;
  int prime = 2;

  while(prime <= num){
    if(num%prime)
      prime++;
    else
      num = num/prime;
  }
  cout << prime;

  /*num = 600851475143;

  int i;
  int tmp = 0;
  for(i < 2; i < num; i++)
    if(isPrime(i))
	  if(num%i){
	    num = num/i;
	    tmp = i;
	  }

  cout << tmp;
  */
}
