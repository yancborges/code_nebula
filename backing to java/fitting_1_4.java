import java.util.Scanner;

public class fitting_1_4 {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        
        double grade1 = input.nextDouble();
        double grade2 = input.nextDouble();
        
        double score = (grade1 + grade2)/2;
        System.out.println(score);
    
    }
}

