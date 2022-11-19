''' 
Python program to implement DFA that accepts the following-
Even number of 0's and even number of 1's with ∑ = {0, 1} 
'''

def isAccepted(s):
     
    # Start state of DFA
    start = 0
 
    # Final state of DFA
    final = 0
 
    # Previous state of DFA
    previous = 0
 
    # Loop to iterate through the string entered by user
    for i in range(len(s)):
         
        if ((s[i] == '0' and previous == 0) or (s[i] == '1' and previous == 3)):
            final = 1
        elif ((s[i] == '0' and previous == 3) or (s[i] == '1' and previous == 0)):
            final = 2
        elif ((s[i] == '0' and previous == 1) or (s[i] == '1' and previous == 2)):
            final = 0
        elif ((s[i] == '0' and previous == 2) or (s[i] == '1' and previous == 1)):
            final = 3
 
        # Update the previous state
        previous = final

    # Condition when final state is reached
    if (final == 0):
        print("\nThe entered string is accepted.")
         
    # Otherwise
    else:
        print("\nThe entered string is not accepted.")
 
if __name__ == '__main__':

    s = input("\nEnter a string to be checked: ")
 
# Function call to check whether the entered string is accepted or not accepted
isAccepted(s)




''' 
Instructions for execution:-
> On compiling and running the code, the user will be asked to enter a string.
> The user must enter a string consisting of 0's and 1's when the above message is displayed.
> Depending on whether the entered string is accepted or not by the DFA, an appropriate message is going to be displayed.



Examples of outputs:-

1)  Enter a string to be checked: 00101
    The entered string is not accepted.

2)  Enter a string to be checked: 001100
    The entered string is accepted.

'''