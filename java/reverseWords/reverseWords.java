
class Solution {
    public static void main(String[] args) {
        String input;
        Solution obj = new Solution();

        input = "  hello world  ";

        System.out.println("'" + obj.reverseWords(input) + "'");
    }


    public String reverseWords(String s) {

        StringBuilder ans  = new StringBuilder("");
        StringBuilder subStr  = new StringBuilder("");

        for (int i = 0; i < s.length(); i++ ) {

            if( s.charAt(i) != ' ' ) {
                subStr.append(s.charAt(i));
            } 
            
            if ( (s.charAt(i) == ' ' || i == s.length() - 1) && subStr.length() > 0 ) {
                ans.append(subStr.reverse() + " ");
                subStr.setLength(0);
            }
        }

        ans.reverse();

        return ans.toString().trim();
    }
}
