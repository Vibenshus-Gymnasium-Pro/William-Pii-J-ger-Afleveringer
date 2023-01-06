#include <chrono>
#include <iostream>

// ##############################################################################
// Written by William Pii Jæger
// Username:
// I have written the whole algorithem with pure math. Not using % or libraries.
// ##############################################################################

// The Algorithem
int euclideanalgorithem(int p_A, int p_B) {
  // Swap if parameters are incorrectly inputted (failsafe)
  if (p_B > p_A) {
    p_A = p_A + p_B;
    p_B = p_A - p_B;
    p_A = p_A - p_B;
  }

  // r is the remainder of the division
  int r;
  // Atemp = previous value of A. Stored as to not calculate A twice
  // (speeds up the code)
  int Atemp;

  // All numbers are divisible by 1, so no need to check if p_B != 1
  while (p_B != 0) {
    r = p_B;
    Atemp = ((p_A / p_B) * p_B);
    p_B = p_A - Atemp;
    p_A = Atemp;
  }

  return r;
}

int main() {
  // Edit default values here (numbers to be checked)
  int num1 = 21;
  int num2 = 28;

  std::cout << "The greatest common divider between " << num1 << " and " << num2
            << " is: " << euclideanalgorithem(num1, num2);

  return 0;
}