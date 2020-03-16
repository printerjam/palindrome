
string = 'adskjfhaaaaenmeawprunxczujweflkjdrurshdshmadamlsakmamaddamamjdsalkqwbkqw'
#string = 'aaaaaa'

palindrome = { 'word': '', 'position_begin': 0, 'posistion_end': 0 }

def stop_process(substring_begin, substring_end):
    if substring_begin < 0 or substring_end > len(string):
        return True

    return False

def palindrome_check(substring_begin,substring_end):
    global palindrome
    substring = string[substring_begin:substring_end]
    while substring == substring[::-1]:
        if len(substring) > len(palindrome):
            palindrome['word'] = substring
            palindrome['position_begin'] = substring_begin
            palindrome['position_end'] = substring_end

        substring_begin = substring_begin-1
        substring_end = substring_end+1

        if stop_process(substring_begin, substring_end):
            break

        substring = string[substring_begin:substring_end]

for i in range(1, len(string)):

    if stop_process(i-1, i+2):
        break
    palindrome_check(i-1, i+2)
    palindrome_check(i, i+2)

print('\nString ['+str(len(string))+']: '+string)
print('Position: '+string[:palindrome.get('position_begin')]+'\033[1m\033[4m'+palindrome.get('word')+'\033[0m'+string[palindrome.get('position_end'):])
print('Palindrome ['+str(len(palindrome.get('word')))+']: '+palindrome.get('word')+'\n')
