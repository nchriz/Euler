#include <iostream>

using namespace std;

int isPalindrom(int x){
  int sum = 0, num=x;
  while(num!=0){
    sum = sum * 10;
    sum = sum + num%10;
    num = num/10;
  }
  if(sum == x)
    return 1;
  return 0;
  
}

int main(){
  int i, j;
  int tmp = 0;
  for(i = 999; i>=100; i--){
    for(j = 999; j>=i; j--)
      if(isPalindrom(i*j) && tmp < i*j){
	tmp = i*j;
	break;
	cout << tmp << endl;
      }
  }

  cout << tmp;
  return 0;

}
