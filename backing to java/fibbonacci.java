import java.util.Scanner;

public class fibbonacci {
	
	public static void main (String args[]) {
		
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        
        int a = 1;
        int b = 0;
        int fib = 0;
        
        System.out.println("");
        for( int i = 0; i < num; i++ ) {
            if( i == 0 ) {
                System.out.println(0);
            }
            else if( i == 1 ) {
                System.out.println(1);
            }
            else {
                fib = a+b;
                b = a;
                a = fib;
                System.out.println(fib);
            }
        }
	}
}

