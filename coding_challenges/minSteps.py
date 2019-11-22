"""
Leetcode #650: 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing
the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

24 ms faster than 98% of submissions
12.7 MB less than 100% of submissions
"""
def minSteps(n):
    nsteps=0
    rem=n-1
    cp=i=1
    while i<n:
        if rem%i==0:
            nsteps+=2
            cp=i
        else:
            nsteps+=1
        rem-=cp
        i+=cp
    return nsteps
