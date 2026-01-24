class Solution {
    private String removeExtraSpace(String s) {
        if (s == " " && s == "") {
            return s;
        }
        char[] c = s.toCharArray();
        int left = 0, right = c.length - 1;
        while (left < right && c[left] == ' ') {
            left++;
        }
        while (right >= 0 && c[right] == ' ') {
            right--;
        }
        int totalLen = c.length - (left + (c.length -1 - right));
        return new String(c, left, totalLen);
    }

    public String reverseWords(String s) {

        String[] fruits1 = s.split(" ");
        String ans = "";
        for (int i = fruits1.length - 1; i >= 0; i--) {
            // System.out.println( "amrit" + fruits1[i]);
            String spaceRemovedString = removeExtraSpace(fruits1[i]);
            ans += spaceRemovedString;
            if (i != 0) {
                ans += " ";
            }
        }
        return ans;
    }
}
public class test {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String input = "  hello world  ";
        String output = sol.reverseWords(input);
        System.out.println("Reversed words: '" + output + "'");
    }
}