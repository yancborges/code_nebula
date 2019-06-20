import java.util.Scanner;

public class fitting_1_5 {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        
        int now = input.nextInt();
        int birth = input.nextInt();
        
        if((now - birth) >= 16) {
            System.out.println("Sim");
        }
        else {
            System.out.println("Nao");
        }      
    
    }
}

