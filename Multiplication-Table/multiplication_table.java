import java.util.Scanner;

public class multiplication_table {
    public static void main(String[] args) {
        System.out.println("Multiplication table\n--------------------");
        
        while (true) {
            System.out.println("Table of : ");
            String input = user_input();
            
            if (check(input)) {
                
                int table_of = Integer.parseInt(input);
                
                if (table_of != 0) {
                    System.out.println("");
                    
                    for (int i = 1; i <= 10; i++) {
                        System.out.println(i + " × " + table_of + " = " + (i * table_of));
                    }
                    
                    System.out.println("");
                    
                } else {
                    System.out.println("\nError : Multiplication table of 0 cannot be calculated\n");
                }
                
            } else {
                System.out.println("\nError : Make sure you entered number\n");
            }
            
        }
        
    }
    
    public static String user_input() {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        return input;
        
    }
    
    public static boolean check(String value) {
        
        for (char c : value.toCharArray()) {
                
            if (! Character.isDigit(c)) {
                return false;
            }
                
        }
        return true;
            
    }
        
}