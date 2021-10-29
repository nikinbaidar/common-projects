public class HelloWorld {

    public static void clearScreen(){
        System.out.print("\033\143");
    }

    public static void main (String[] args) {
        clearScreen();
        System.out.println("Hello, World!");

    }

}
