import java.util.Scanner;

public class fitting_1_6 {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        
        double a = input.nextDouble();
        double b = input.nextDouble();
        
        if( a > b ) {
            System.out.println(a);
        }
        else {
            System.out.println(b);
        }
        
	}
}

