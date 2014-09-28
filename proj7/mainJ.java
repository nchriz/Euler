public class mainJ{

    public static int isPrime(int n){
	int upper = (int) Math.sqrt(n)+1;
	boolean[] primes = new boolean[n];


	for(int can = 3; can < upper; can++)
	    if(!primes[can])
		for(int j = 2*can; j < n; j+=can)
		    primes[j]=true;

	for(int i = 0; i < n; i++)
	    System.out.println(primes[i] + " + " + i);

	return 1;
    }

    public static int prime(int n){
	int upper = (int) Math.sqrt(n);
	boolean[] sieve = new boolean[n+1];
	for(int i = 2; i <= upper; i++)
	    if(!sieve[i])
	        for(int k = i*i; k <= upper; k+=i)
		    sieve[k] = true;
	int[] intsieve = new int[n];
	for(int i = 3; i <= upper; i++)
	    if(!sieve[i])
		intsieve[i] = i;
	System.out.println(sieve[10]);
	return 1;//sieve[10001];

    }

    public static void main(String[] args){
        int N = Integer.parseInt(args[0]);
	//System.out.println(prime(2*1000000));
	isPrime(N);
    }
}
