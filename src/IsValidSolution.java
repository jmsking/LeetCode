import java.util.HashMap;
import java.util.Map;

/**
* Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
* An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Note that an empty string is also considered valid.
* @author ChenJie
* @date	Oct 3, 2018 9:19:10 PM
*/
public class IsValidSolution {

	private static final Map<String, String> map = new HashMap<>();
	
	public IsValidSolution() {
		map.put(")", "(");
		map.put("]", "[");
		map.put("}", "{");
	}
	
	public boolean isValid(String s) {
		if(s == null) {
			return false;
		}
		Stack stack = new Stack();
		int pair = 0;
        for(int i = 0; i < s.length(); i ++) {
        	String value = s.substring(i, i+1);
        	if(value.equals(")") || value.equals("]") || value.equals("}")) {
        		if(stack.isEmpty()) {
        			return false;
        		}
        		if(stack.front().equals(map.get(value))) {
        			stack.pop();
        			pair --;
        		} else {
        			return false;
        		}
        	} else {
        		stack.push(value);
        		pair ++;
        	}
        }
		return pair == 0;
    }
	
	public static void main(String[] args) {
		String s = "{[]}";
		boolean ans = new IsValidSolution().isValid(s);
		System.out.println(ans);
	}
	
}

class Stack {
	private static final int MAX_SIZE = 10000;
	private String[] items = new String[MAX_SIZE];
	private int top;
	public Stack() {
		top = 0;
	}
	public void push(String value) {
		if(top >= MAX_SIZE) {
			String[] newItems = new String[MAX_SIZE*2];
			for(int i = 0; i < top; i ++) {
				newItems[i] = items[i];
			}
			items = newItems;
		}
		items[top++] = value;
	}
	public boolean isEmpty() {
		return top == 0 ? true : false;
	}
	public void pop() {
		if(!isEmpty()) {
			top --;
		}
	}
	public String front() {
		if(!isEmpty()) {
			return items[top-1];
		}
		return null;
	}
}