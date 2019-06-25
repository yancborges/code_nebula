import java.util.Scanner;
import java.util.Random;

public class register_person {
	
	public static void main (String args[]) {
		
        // Constants
        int MAX_PEOPLE = 3;
        String NAMES [] = {"Ana","Jose","Nego ban","Minha vo","Benson","Ben 10","Astolfo","Cavalo festeiro","Einstein"};
        String JOBS [] = {"Doctor","Dentist","Thief","Policeman","Fireman","Unenployed","Drunk","Healer"};
        
        // Instancing
        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        
        // Vars
        Person storage [] = new Person [MAX_PEOPLE];
        
        // Code
        for(int i = 0; i < MAX_PEOPLE; i++) {
            Person p = new Person();
            p.set_name(NAMES[rand.nextInt(NAMES.length)]);
            p.set_birth(new_date());
            p.set_gender(rand.nextInt(2));
            p.set_freedom(rand.nextInt(2));
            
            switch(p.get_freedom()) {
                case 1:
                    p.citzen.set_job_name(JOBS[rand.nextInt(JOBS.length)+1]);
                    p.citzen.set_salary(rand.nextDouble()+1000.0);
                    p.citzen.set_journey(rand.nextInt(36)+5);
                    
                    break;
                case 0:
                    p.reclused.set_date(new_date());
                    p.reclused.set_bail(rand.nextDouble()+5.0);
                    p.reclused.set_days_left(rand.nextInt(1000));
                    break;
            }
            
        }      
        
        
	}
    
    public static String new_date() {
        Random rand = new Random();
        int day = rand.nextInt(31)+1;
        int month = rand.nextInt(12)+1;
        int year = rand.nextInt(2019)+1;
        return day + "/" + month + "/" + year;
        //return rand.nextInt(30)+1 + "/" rand.nextInt(12)+1 + "/" + rand.nextInt(2020);
    }
}

