import java.util.Scanner;

public class fitting_1_1 {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        
        if(number > 10) {
            System.out.println("Bigger than 10");
        }
        else {
            System.out.println("Lower than 10");
        }
        
	}
}

