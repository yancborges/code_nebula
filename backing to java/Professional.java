public class Professional extends Person {
	
	public String job_name;
    public double salary;
    public int journey;
    
    public Professional() {
        super();
        job_name = "";
        salary = 0;
        journey = 0;
    }
    
    /// SETTING
    
    public void set_job_name(String job_name) {
        this.job_name = job_name;
    }
    
    public void set_salary(double salary) {
        this.salary = salary;
    }
    
    public void set_journey(int journey) {
        this.journey = journey;
    }
    
    /// GETTING
    
    public String get_job_name() {
        return this.job_name;
    }
    
    public double get_salary() {
        return this.salary;
    }
    
    public int get_journey() {
        return this.journey;
    }
    
}

