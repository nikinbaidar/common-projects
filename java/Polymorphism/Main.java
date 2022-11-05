import java.lang.Math;

public class Main {
  public static void main(String[] args) {
    Java obj_1 = new Java("Java");
    Py obj_2 = new Py("Python");

    System.out.println(obj_1.name);
    System.out.println(obj_2.name);
  }
}

class ProgrammingLanguage {
  // A polymorphic variable
  static String name;

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
