#include <math.h>
#include <stdbool.h>

static bool isEven(int a);
static bool isFactor(int a, int b);
static bool inRange(int a, int lower, int upper);
static float getDecimalPart(float num);
static double power(double x, double n);

bool isFactor(int a, int b) {
  return ((a/b) * b == a) ? 1 : 0;
}


bool isEven(int a) {
  return !(a & 1);
}


bool inRange(int a, int lower, int upper) {
  return (a >= lower && a <= upper);
}


float getDecimalPart(float num) {
    return (num - (int) num);
}


double power(double x, double n) {
    double result;
    result = (floor(n/2) > 0) ? x * power(x, floor(n/2) - 1) : 1;
    return isEven(n) ? result * result : x * result * result;
}


/* Custom datatype */

struct Point {
    double x;
    double y;
};


/* x and y are co-ordinates and p is the point that they make */
struct Point* makepoint (double x, double y) {

    struct Point* p = malloc(sizeof(struct Point));
    p->x = x;
    p->y = y;
    return p;
}

double distance (struct Point* p1, struct Point* p2) {
    double dx = p1->x - p2->x;
    double dy = p1->y - p2->y;
    return sqrt(dx*dx+dy*dy);
}
