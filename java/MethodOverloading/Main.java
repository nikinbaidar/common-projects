class MethodOverloading {

  MethodOverloading() {
    System.out.println("Hello");
  }

  int sum;

  public int sum(int a, int b) {
    return a + b;
  }

  public int sum(int a, int b, int c) {
    return a + b + c;
  }

  public int sum(int array[]) {
    for(int item: array) {
      sum += item;
    }
    return sum;
  }
}

public class Main {
  public static void main(String[] args) {
    int [] a = {1, 3, 3, 4};
    MethodOverloading object = new MethodOverloading();
    System.out.println(object.sum);
  }
}
