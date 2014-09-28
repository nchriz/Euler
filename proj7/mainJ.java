public class mainJ{

    public static boolean[] isPrime(int n){
	int upper = (int) Math.sqrt(n)+1;
	boolean[] primes = new boolean[n];

	for(int i = 2; i <n; i++)
	    primes[i] = true;


	for(int can = 2; can < upper; can++)
	    if(primes[can])
		for(int j = 2*can; j < n; j+=can)
		    primes[j]=false;

	//for(int i = 0; i < n; i++)
	//    System.out.println(primes[i] + " + " + i);
	
	return primes;
    }

    public static void main(String[] args){
        int N = Integer.parseInt(args[0]);
	int[] num = new int[N];
	int tmp = 0;
	long start = System.currentTimeMillis();
	boolean[] primes = isPrime(N);
	for(int i = 0; i < N; i++)
	    if(primes[i]){
		num[tmp] = i;
		tmp++;
	    }
	System.out.println(num[10001]);
	System.out.println(System.currentTimeMillis()-start);
		
    }
}
