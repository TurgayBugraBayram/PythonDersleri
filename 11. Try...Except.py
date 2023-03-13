# try:
#     #hata veribliecek kodlar
# except:
#     #eger hata var ise calisir

# a = int("merhaba")

# try:
#     a = int("merhaba")
#     print("try calisti")
# except:
#     print("except calisti")
#
# print("bitti")


# try:
#     a = int("123")
#     b = int("merhaba")
#     print("try calisti")
# except ValueError:
#     print("hata olustu")

# try:
#     a = int(input("Sayi1 : "))
#     b = int(input("Sayi2 : "))
#     print(a / b)
# except ValueError:
#     print("sadece sayi giriniz")
# except ZeroDivisionError:
#     print("Bir sayi sifira bolunmez")

# try:
#     a = int(input("Sayi1 : "))
#     b = int(input("Sayi2 : "))
#     print(a / b)
# except (ValueError,ZeroDivisionError):
#     print("sadece sayi giriniz")
#     print("Bir sayi sifira bolunmez")

# try:
#     a = int(input("Sayi1 : "))
#     b = int(input("Sayi2 : "))
#     print(a / b)
# except ValueError:
#     print("sadece sayi giriniz")
# except ZeroDivisionError:
#     print("Bir sayi sifira bolunmez")
# finally:
#     print("finally calisti")

# def terscevir(metin):
#     if (type(metin) != str):
#         raise ValueError("Lutfen dogru str giriniz")
#     else:
#         return metin[::-1]
#
# try:
#     print(terscevir(12))
# except ValueError:
#     print("Fonksiyonda bir hata olustu")


# raise ZeroDivisionError("0'a bolunmez")

try:
    a = int(input("Sayi1 : "))
    b = int(input("Sayi2 : "))
    print(a / b)
except ValueError:
    print("sadece sayi giriniz")
except ZeroDivisionError:
    print("Bir sayi sifira bolunmez")
else:
    print("else calisti") # else sadece try calisir ise calisir

"""
AssertionError	        if statement fails.assert
AttributeError	        if attribute assignment or reference fails.
EOFError	            if the functions hits end-of-file condition.input()
FloatingPointError	    if a floating point operation fails.
GeneratorExit	        Raise if a generator's method is called.close()
ImportError	            if the imported module is not found.
IndexError	            if index of a sequence is out of range.
KeyError	            if a key is not found in a dictionary.
KeyboardInterrupt	    if the user hits interrupt key (Ctrl+c or delete).
MemoryError	            if an operation runs out of memory.
NameError	            if a variable is not found in local or global scope.
NotImplementedError	    by abstract methods.
OSError	                if system operation causes system related error.
OverflowError	        if result of an arithmetic operation is too large to be represented.
ReferenceError	        if a weak reference proxy is used to access a garbage collected referent.
RuntimeError	        if an error does not fall under any other category.
StopIteration	        by function to indicate that there is no further item to be returned by iterator.next()
SyntaxError	by parser   if syntax error is encountered.
IndentationError	    if there is incorrect indentation.
TabError	            if indentation consists of inconsistent tabs and spaces.
SystemError	            if interpreter detects internal error.
SystemExit	            by function.sys.exit()
TypeError	            if a function or operation is applied to an object of incorrect type.
UnboundLocalError	    if a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	        if a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	    if a Unicode-related error occurs during encoding.
UnicodeDecodeError	    if a Unicode-related error occurs during decoding.
UnicodeTranslateError	if a Unicode-related error occurs during translating.
ValueError	            if a function gets argument of correct type but improper value.
ZeroDivisionError	    if second operand of division or modulo operation is zero.
"""

