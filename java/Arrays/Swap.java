package basic.utilities;

import java.util.Arrays;

// Swap integers positions of elements in an array.

class Main {

  static int [] a = {4, 0, 8, 9, 23, 79, 34, 8, 5, 3, 1};


  public static void main(String[] args) {

    Main obj = new Main();

    System.out.println(Arrays.toString(obj.a));
    System.out.println();

    obj.iswap(0, 9);

    System.out.println(Arrays.toString(obj.a));

  }
}

