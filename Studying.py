"""
Studying.py: Just general info on Python language.
"""
# no imports
__author__ = 'kyrylo'

'''
Types
int - limited by physical memory limit (unmodifyible)
str - Unicode (unmodifyible)
[]
datatype(type)
str(type) - applicable to any type

Оператор = – это не оператор присваивания значения переменной, как
в некоторых других языках программирования. Оператор = связывает
ссылку на объект с объектом, находящимся в памяти. Если ссылка на
объект уже существует, ее легко можно связать с другим объектом,
указав этот объект справа от оператора =. Если ссылка на объект еще
не существует, она будет создана оператором =.

Dynamic type control

type(reference)

GC

TypeError

('',) - tuple - ordered unmodifiable object sequence
[] - list modifiable

len(type)

[].append(reference)
[].insert(ref)
[].remove(ref)

None
is not None

Unicode is used for strings in Python

Sequence of operators is possible in Python: 0 <= a <= 10

in
not in

and or - returns operand, defining the result (not Boolean)
not - estimates operand in boolean context and returns Boolean always

x == False if x is False, None, empty sequence or collection or 0

suite in Python is programming block
keyword 'pass' could be used in place of suite

: is used everywhere where suite should begin

if x:
    suite
elif y:
    suite
else:
    suite

while x:
    suite

break
continue

for x in iterable:
    suite

try:
    try_suite
except exceptionN [as variableN]:
    exception_suiteN

division operator returns floating point number

// division with trunc

int unmodifiable so int+=int creates new reference

compound operator <operator>= is potentially faster

+ and += are overloaded for strings and lists

+= for lists should have iterable operand

def functionName(arguments):
    suite

function by default returns None

'''