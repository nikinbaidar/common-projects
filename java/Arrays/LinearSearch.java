/* Linear Search Algorithm:
 * Returns the index of the first occurence of the key.
 *
 * Assumption: They provided key is an element of array.
 *
 * */

package arrays.searching;

import java.util.Arrays;

public class LinearSearch {

  static int[] x;

  LinearSearch(int[] a) {
    this.x = Arrays.copyOfRange(a, 0, a.length);
  }

  public static int getIndex(int key) {
    int i = 0;

    while (x[i] != key){
      i++;
    }
  
    return i;
  }

  public static int getIndex(int key, int occurence) {
    int i = 0, count = 1;

      while (i < x.length){
        if (x[i] == key && count == occurence)
          break;
        else if(x[i] == key) {
          count++;
        }
        i++;
      }
  
    return i;
  }

  public static void main(String[] args) {
    int [] a = {5, 4, 6, 1, 3, 6, 2, 7, 8, 6, 9};
    LinearSearch array = new LinearSearch(a);
    System.out.println(Arrays.toString(array.x));

    int key = 6;
    System.out.printf("Element: %d, Index: %d\n", key, array.getIndex(key));
    System.out.printf("Element: %d, Index: %d\n", key, array.getIndex(key, 3));
  }
}
