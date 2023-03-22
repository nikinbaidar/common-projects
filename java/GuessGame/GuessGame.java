
class Solution {

    static int pick;

    public static int makeGuess(int num) {

        if (num > pick)
            return -1;
        if (num < pick) 
            return 1;

        return 0;

    }

    public static int guessNumber(int lower_limit, int upper_limit) {
        while (lower_limit <= upper_limit) {
            int mid = (int) (lower_limit + (upper_limit - lower_limit) / 2);
            int num = makeGuess(mid);
            if (num == 0) {
                return mid;
            }
            else if(num < 0) {
                upper_limit = mid - 1;
            }
            else  {
                lower_limit = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int lower_limit = 1;
        int upper_limit = 12;
        pick = 4;

        int myGuess = guessNumber(lower_limit, upper_limit);

        System.out.println("pick: " + pick + " Guess: " + myGuess);


    }
}
