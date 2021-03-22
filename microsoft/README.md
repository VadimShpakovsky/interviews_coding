Preliminary test before main interview

### riddle
Input: string with a-z and ?.

Output: the same string, but each ? have to be replaced by a-z symbol. The same symbols can't be adjacent. 

Example: 'ab?bc' -> 'ababc' (or 'abzbc'), but not 'abbbc'

### max_sum_pair
Input: array of numbers

Output: max sum of numbers, which are paired by the same sum of digits.

Example: [11, 22, 31] -> 53 (22 + 31)

### frog_hops
History: two frogs try to go away to max distance. They can go only UP (if height of next position >= height of current position). 

Input: array of numbers

Output: max possible distance between frogs

Example: [1, 5, 5, 2, 6] -> 4 


## My results (21/03/2021)
1) **riddle**: correctness: OK, performance: 100% 
2) **max_sum_pair**: correctness: OK, performance: 9%
3) **frog_hops**: correctness: OK, performance: 33%