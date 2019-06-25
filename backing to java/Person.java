public class Person {
	
	public String name;
    public String birth;
    public int gender;
    public int freedom;
    public Professional citzen;
    public Criminal reclused;
    
    public Person() {
        name = "";
        birth = "";
        gender = 0;
        freedom = 0;
    }
    
    /// SETTING
    
    public void set_name(String name) {
        this.name = name;
    }
    
    public void set_birth(String birth) {
        this.birth = birth;
    }
    
    public void set_gender(int gender) {
        this.gender = gender;
    }
    
    public void set_freedom(int freedom) {
        if(freedom == 1) {
            this.citzen = new Professional();
        }
        else {
            this.reclused = new Criminal();
        }
        this.freedom = freedom;
    }
    
    /// GETTING
    
    public String get_name() {
        return this.name;
    }
    
    public String get_birth() {
        return this.birth;
    }
    
    public int get_gender() {
        return this.gender;
    }
    
    public int get_freedom() {
        return this.freedom;
    }

    public String toString() {
        return this.name + " " + this.birth + " " + this.gender;
    }
}

