"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Input: hour = 12, minutes = 30
Output: 165

Input: hour = 3, minutes = 30
Output: 75

Input: hour = 3, minutes = 15
Output: 7.5

Input: hour = 4, minutes = 50
Output: 155

Input: hour = 12, minutes = 0
Output: 0

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        if hour == 12 :
            min_diff = (11 * minutes)/12
            ac_d = min_diff * 6

        
        else:
            h_m = hour * 5
            h_cg = minutes / 12
            
            if h_m < minutes:
                abs_d = minutes - h_m
                abs_d = abs(abs_d - h_cg)
                
            else :
                abs_d = h_m - minutes
                abs_d += h_cg
            
            ac_d = abs_d * 6
            
        return min(ac_d , 360 - ac_d)
