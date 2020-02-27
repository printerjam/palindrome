"""
After my first attempt at this, I went to look at solutions on the internet to compare and realized this solution is broken.

It will work with palindromes like 'abcba' but not 'abccba'.

Such a stupid mistake. I will try again and update.
"""

string = 'adskjfhaaaaenmeawprunxczujweflkjdrurshdshmadamlsakmamadamamjdsalkqwbkqw'
#string = 'aaaaaa'

palindrome = ''
substring_begin = 0
substring_end = 0

def stop_process(substring_begin, substring_end):
    if substring_begin < 0 or substring_end > len(string):
        return True

    return False

for i in range(1, len(string)):

    substring_begin = i-1    
    substring_end = i+2

    if stop_process(substring_begin, substring_end):
        break

    substring = string[substring_begin:substring_end]
    while substring == substring[::-1]:
        if len(substring) > len(palindrome):
            palindrome = substring
            position_begin = substring_begin
            position_end = substring_end

        substring_begin = substring_begin-1
        substring_end = substring_end+1

        if stop_process(substring_begin, substring_end):
            break

        substring = string[substring_begin:substring_end]

print('\nString ['+str(len(string))+']: '+string)
print('Position: '+string[:position_begin]+'\033[1m\033[4m'+palindrome+'\033[0m'+string[position_end:])
print('Palindrome ['+str(len(palindrome))+']: '+palindrome+'\n')
