import java.lang.Math;

public class Main {
  public static void main(String[] args) {
    System.out.println(Math.PI);
    System.out.println(Math.E);
    System.out.println(Math.abs(-2));
    System.out.println(Math.pow(5, 2));
  }
}

class ProgrammingLanguage {
  // A polymorphic variable
  String name;

  ProgrammingLanguage(String name) {
    this.name = name;
  }
}

class Java extends ProgrammingLanguage {
  Java(String name) {
    super(name);
  }
}

class Py extends ProgrammingLanguage {
  Py(String name) {
    super(name);
  }
}
