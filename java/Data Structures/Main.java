class Main extends Test {
  @Override
  public void display() {
    super.display();
    System.out.println("Aliens.");
  }

  public static void main(String[] args) {
    Main obj = new Main();
    obj.display();
  }
}


class Test {
  public void display() {
    System.out.println("We're");
  }
}

