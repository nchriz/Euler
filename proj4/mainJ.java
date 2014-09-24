public class mainJ{

    public static void main(String[] args){
	int tmp = 0;

	for(int i = 999; i > 100; i--)
	    for(int j = 999; j > i; j--)
		if(isPalindrom(i*j) && tmp < i*j){
		    tmp = i*j;
		}
	System.out.println(tmp);
    }

    private static boolean isPalindrom(int x){
	String s = Integer.toString(x);
	for(int i = 0, j = s.length() - 1; i < s.length()/2; i++,j--)
	    if(s.charAt(i)!=s.charAt(j))
		return false;
	return true;
    }
}
