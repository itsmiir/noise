#include <stdint.h>
#include <stdio.h>

int64_t foo(int64_t);
// In C++, it would be:
// extern "C" int64_t foo(int64_t);

int main() {
  printf("%lu\n", foo(10));
}