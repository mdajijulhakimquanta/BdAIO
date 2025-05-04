import sys
def count_passwords(s):
    count = 0
    n = len(s)
    i = 0
    while i < n:
        on_lower = False
        on_upper = False
        on_digit = False
        j = i
        while j < n:
            c = s[j]
            if c.islower():
                on_lower = True
            elif c.isupper():
                on_upper = True
            elif c.isdigit():
                on_digit = True
            if on_lower and on_upper and on_digit:
                count += 1
                i = j  # the next start will be j+1
                break
            j += 1
        i += 1
    return count

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(count_passwords(line))