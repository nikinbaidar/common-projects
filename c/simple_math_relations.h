static bool isEven(int a);
static bool isFactor(int a, int b);
static bool inRange(int a, int lower, int upper);
static int power(int x, int n);

bool 
isFactor(int a, int b) 
{
  return ((a/b) * b == a) ? 1 : 0;
}


bool
isEven(int a) 
{
  return !(a & 1);
}


bool 
inRange(int a, int lower, int upper) 
{
  return (a >= lower && a <= upper);
}


int
power(int x, int n)
{
    int result;
    result = (n/2 > 0) ? x * power(x, n/2 - 1) : 1;
    return  isEven(n) ? result * result : x * result * result;
}
