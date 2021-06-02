//code taken from https://www.geeksforgeeks.org/static-and-dynamic-scoping/
#include<stdio.h> 

int x = 10; 
   
int f() 
{ 
   return x; 
} 
  
int g() 
{ 
   int x = 20; 
   return f(); 
} 
  
int main() 
{ 
  printf("%d", g()); 
  printf("\n"); 
  return 0;
}