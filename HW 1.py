# HW 1:

print(5 // 2)
print(10 * 5 - 3 //2)
print(3 ** 2)
print(3.0 ** 2)
print(2 ** 4 / (4 + 4))
print(5 % 2)
print(1 + 2 + 3 % 2)
print(True or False or True and False or False)
print(not (not False))
print(not (not (not False)))
print(True and False or True and False and False)
print(42 != 4)
print(9 != 9)
print(4 != '4')
print(not 7 < 7)
print(3 > 7 and 7 <= 10)

course = "CS9"
print(bool(course == "CS8" or "CS16"))

print(course == "CS8" or course == "CS16")

print(4 ** (5 // 2) / 2 == 8)

print([8, 9, 10] + [100, 100, 100])
print([7] * 3)
print([3, 3] * 2)
print([2, 9, 10, 100][2:4])
print('cat' in ['cat', 'dog', 'bat', 'rat'])
print(not 'rat' in ['cat', 'dog', 'bat', 'rat'])
print([5, 4, 3, 2, 1].pop())
print(['cat', 'dog', 'bat', 'rat'].pop()) # RETURNS 'rat', but prints rat
print([5, 4, 3, 2, 1].pop(2))
print(['cat', 'dog', 'bat', 'rat'].index('bat'))

my_pets = ['cat', 'dog', 'bat', 'rat']
my_pets.remove('rat')
print(my_pets)

print(['cat', 'dog', 'bat', 'rat'].remove('rat'))
print(list(range(4)))
print(list(range(-2, 4, 2)))
print(list(range(10, 5, -2)))
print(list(range(2, 5)))

var_a = "cs9"
var_b = "hello!     how are you?"
var_c = "ucsb"

print(var_c.upper()) # RETURNS 'UCSB', but prints UCSB
print(var_a.islower())
print(var_b.split())
print(var_b.split("!"))
print(var_a.find("9"))
print(var_a.index('s'))

var_s = {2, "4", 6}
var_t = {2, 4, 6}
var_u = { "CA": "Sacramento", "NV": "Carson City",
          "AZ": "Phoenix", "WA": "Olympia", "OR": "Salem" }

print(len(var_s | var_t)) # | unions the two sets and duplicates are removed
print(var_s - var_t)      # - takes elements from the first set that aren't in
                          # the second
print(var_s & var_t)      # & take only the elements that appear in both sets
print(4 in var_s)
print(var_u["NV"])
print(len(var_u["AZ"]))
print(var_u["WA"][1:5])
print("sa" in var_u["CA"])
print("OR" in var_u)
print(var_u.get("AZ"))

def f(n):
    while n < 10:
        if n < 3:
            n = n + 2
        elif n < 6:
            return n
        if n < 10:
            n = n + 5
            return n
    return n

print(f(2))
print(f(5))
print(f(7))
print(f(9))
print(f(100))

def count_odds(my_list):
    count = 0
    for num in my_list:
        if num % 2 != 0:
            count += 1

    return count

assert count_odds([1, 2, 3]) == 2
assert count_odds([]) == 0
assert count_odds([3, 3, 5]) == 3
assert count_odds([6, 7, 7, 7]) == 3
assert count_odds([7]) == 1
