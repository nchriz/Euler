import java.math.BigInteger;

public class mainJ {

    public static void main(String[] argv){
	int n = Integer.parseInt(argv[0]);
	BigInteger sum = BigInteger.ONE;
	for(int i = 2; i < n; i++)
	    sum = sum.multiply(BigInteger.valueOf(i));
	
	System.out.println(sum.toString());

	int tmp = 0;
	while(sum.intValue() > 1){
	    tmp += sum.intValue()%10;
	    sum = sum.divide(BigInteger.valueOf(10));
	}

	System.out.println(tmp);

    }

}
