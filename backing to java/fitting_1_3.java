import java.util.Scanner;

public class fitting_1_3 {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        
        double PRICE = 1.3;
        double DISCOUNTED = 1;
        
        int quant = input.nextInt();
        if(quant >= 12) {
            System.out.printf("\nTotal: R$ %f\n", quant*DISCOUNTED);
        }
        else {
            System.out.printf("\nTotal: R$ %f\n", quant*PRICE);
        }
	}
}

