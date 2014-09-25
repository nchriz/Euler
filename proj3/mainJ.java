public class mainJ{
    public static void main(String[] args){
        double num = 600851475143d;
	int prime = 2;
	while(prime <= num){
	    if((num%prime)>0)
		prime++;
	    else
		num = num/prime;
	}
	System.out.println(prime);
    }
}
