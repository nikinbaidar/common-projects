class Main extends Test {
  public static void main(String[] args) {
    Main obj = new Main();
  }
}

abstract class Test extends Application {
  public static void display() {
    System.out.println("Some text.");
  }
}

abstract class Application {
  /* Some regullar method */

  abstract void someFunction();

}




