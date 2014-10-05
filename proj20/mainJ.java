import java.math.BigInteger;

public class mainJ {

    public static void main(String[] argv){
	int n = Integer.parseInt(argv[0]);
	BigInteger sum = BigInteger.ONE;
	for(int i = 2; i < n; i++)
	    sum = sum.multiply(BigInteger.valueOf(i));
	String s = sum.toString(10);
	int tmp = 0;

	for(int i=0; i < s.length();i++)
	    tmp += Integer.parseInt(s.substring(i,i+1));

	System.out.println(tmp);

    }

}
