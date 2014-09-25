public class mainJ {
    public static void main(String[] args){
	int n = 2520;
	int check = 1;
	while(check>0){
	    n += 20;
	    check = 0;
	    for(int i = 1; i <= 20; i++)
		check += (n%i)==0 ? 0 : 1;
	}
	System.out.println(n);
    }

}
