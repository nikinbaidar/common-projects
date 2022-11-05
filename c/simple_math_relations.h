static int isEven(int a);
static int isFactor(int a, int b);

static int inRange(int a, int lower, int upper);

int isFactor(int a, int b) {
  return ((a/b) * b == a) ? 1 : 0;
}


int isEven(int a) {
  return !(a & 1);
}


int inRange(int a, int lower, int upper) {
  return (a >= lower && a <= upper);
}
