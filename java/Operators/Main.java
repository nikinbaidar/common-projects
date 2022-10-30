/* Binary literals in memory 
 *  3 : 11111111111111111111111111111101
 * -2 : 11111111111111111111111111111110
 */

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Main {

  static int[] a = {5, 4, 6, 1, 3, 2, 7, 8, 9};

  public static void main(String[] args) {

    Main object = new Main();


    object.indexes();
    // object.testarray();
    // object.listOfLists();
  }

  public static void indexes() {
    // int [] a = {1,4,3,5,0,3,4,9,8,5,3,4};
    System.out.println(Arrays.toString(a));
  }

  public void listOfLists() {
    List<ArrayList<Integer>> y = new ArrayList<ArrayList<Integer>>();
    ArrayList<Integer> x = new ArrayList<Integer>();
    x.add(1);
    x.add(2);
    System.out.println(x);
    y.add(x);
    System.out.println(y);
  }

  public void testarray() {
    int [] x = new int[2];
    x[0] = 1;
    x[1] = 2; 

    System.out.println(Arrays.toString(x));
  }

}

