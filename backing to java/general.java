import java.util.Scanner;

public class general {
	
	public static void main (String args[]) {
		
        // Basic printing
        System.out.println("Hey, welcome to this review");
        
        // Var instanciation
        int age = 5;
        double height = 1.77;
        String name = "Ricardo milos";
        
        // Basic inputting
        Scanner input = new Scanner(System.in);
        int newint = input.nextInt();
        
        // Ternary
        int b = 5;
        int c = 10;
        // A = C, because its bigger than B
        int a = b > c ? b : c;
        
        // Switch
        int option = 1;
        switch(option) {
            case 1:
                System.out.println("Hey");
                break;
            case 2:
                System.out.println("Ho");
                break;
            case 3:
                System.out.println("Let's");
                break;
            case 4:
                System.out.println("Go!");
                break;
            default:
                System.out.println("I dont like ramones at all");
                
        }
        
        // While loop
        int cont = 0;
        int max = 10;
        while( cont < max ) {
            cont++;
        }
        
        // Do while loop
        do {
            cont--;
        } while( cont > 0 );
        
        // For loop
        for( int i = 0; i > max; i++ ) {
            max = i-2;
        }
        
        // Arrays
        int [] x = new int [8];
        
        // Matrix
        int neil [][] = new int [2][3];
        
	}
}

