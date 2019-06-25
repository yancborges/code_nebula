public class Criminal extends Person {
	
	public String date;
    public int days_left;
    public double bail;
    
    public Criminal() {
        super();
        date = "";
        days_left = 0;
        bail = 0;
    }
    
    /// SETTING
    
    public void set_date(String date) {
        this.date = date;
    }
    
    public void set_days_left(int days_left) {
        this.days_left = days_left;
    }
    
    public void set_bail(double bail) {
        this.bail = bail;
    }
    
    
    /// GETTING
    
    public String get_date() {
        return this.date;
    }
    
    public int get_days_left() {
        return this.days_left;
    }
    
    public double get_bail() {
        return this.bail;
    }
}

