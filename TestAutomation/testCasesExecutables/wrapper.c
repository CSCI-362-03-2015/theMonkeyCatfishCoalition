#include "wrapper.h"
#include "stdio.h"


unsigned round_to_next_multiple_of(unsigned number, unsigned divisor)
{
  number += divisor - 1;
  number -= number % divisor;
  return number;
}

int main(int argc, char **argv) {
  int a;
  int b;
  unsigned answer;
  a=argv[0];
  b=argv[1];
  answer = round_to_next_multiple_of(argv[0], argv[1]);
  return(answer);
}


