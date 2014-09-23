public class mainJ {
    public static void main(String[] args){
	double n = 4.0 * Math.pow(10,6);
	int x = 1, y = 1;
	int sum = 0;

	while(y < n){
	    y = y + x;
	    x = y - x;

	    sum += ((y%2)==0) ? y : 0;
	}
	System.out.println(sum);
    }
}
