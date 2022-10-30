package datastructures.util;

import java.lang.Math;

public class Maths {
  public static int ceil (double a) {
    return (int) Math.ceil(a);
  }

  public static int floor (double a) {
    return (int) Math.floor(a);
  }

  public static double log2(double a) {
    return Math.log(a)/Math.log(2);
  }

  public static boolean isOdd(int a) {
    return ( (a & 1) == 1 );
  }

  public static boolean isEven(int a) {
    return ( (a & 1) == 0 );
  }

}
