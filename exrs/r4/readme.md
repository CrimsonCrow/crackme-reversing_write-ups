The goal is make the program print `password OK`

First, we execute the program:

![exe](img/01.png)

Oh.. plaintext again, just like r1


Using strings program, piping it to less

![strings](img/02.png)
 
we get this line of text, which is too many text, by what I mean of too many,
using wc:

![wc](img/03.png)
    
yup.. that many.

objdump the functions

![objdump](img/04.png)

there is a <check_password> function avail.

disassembling the <check_password> function using gdb:

![check_passwd](img/05.png)

OK, I lost it. I don't understand any of it.
    
    TO BE CONTINUED..
    
Mission: create a bruteforce check program.

since there are too many possible password, I decided to create a python bruteforce test.

first we redirect the output of “strings ./r4” to pass.txt

![pr4](img/06.png)

we clean it, remove the unnecessary strings

![txt](img/07.png)

python code:

![python](img/08.png)

thank you python3 documentation, stackoverflow, and this [site](https://www.thecrowned.org/brute-force-crackme-file-password-python) for the code reference

![output](img/09.png)

and here is the python output. that attemp number tho.
