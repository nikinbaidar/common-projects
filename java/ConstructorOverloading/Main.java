/* Superclass */
class SomeApp {
  String current_version;

  SomeApp(String current_version) {
    this.current_version = current_version;
  }

  public void version() {
    System.out.println("The latest version is: " + this.current_version);
  }
}

/* Child class */
public class Main extends SomeApp {
  /* Constructor of the child class */
  Main() {
    /* Calling constructor of super class */
    super("1.1.44");
  }
  public static void main(String[] args) {
    Main object2 = new Main();
    object2.version();
  }
}

/* Output
 * The latest version is 1.1.44
 */
