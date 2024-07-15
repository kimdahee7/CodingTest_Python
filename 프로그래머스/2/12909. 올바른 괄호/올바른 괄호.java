import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.size() == 0) {
                    stack.push(c);
                }
                else if (stack.peek() == '(') {
                    stack.pop();
                }
            }
        }
        if (stack.size() == 0) {
            return true;
        } else {
            return false;
        }
    }
}