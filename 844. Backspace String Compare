class Solution(object):
    def backspaceCompare(self, s, t):
        # Helper function to process the input string and return the final result
        def process_string(s):
            stack = []  # Create an empty stack to simulate the typing process
            for char in s:
                if char != '#':
                    stack.append(char)  # Push non-backspace characters onto the stack
                elif stack:
                    stack.pop()  # Pop from the stack when a backspace is encountered
            return ''.join(stack)  # Convert the stack to a string and return

        # Process both input strings using the helper function
        processed_S = process_string(s)
        processed_T = process_string(t)

        # Compare the processed strings to check if they are equal
        return processed_S == processed_T
