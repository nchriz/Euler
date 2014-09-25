public class mainJ{

    public static void main(String[] args){
	int a = 0, b = 0;
	for(int i = 1; i <= 100; i++){
	    a += i*i;
	    b += i;
	}
	System.out.println(b*b-a);
    }

}
