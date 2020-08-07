The goal is make the program print `password OK`

First, we execute the program:

![exe](img/01.png)

Ok...., well glhf.
 
using objdump to see the functions, you know the drill: 
 
![objdmp](img/02.png)
 
What got our interest here are the <my_secure_test> and <compare_pwd>.


we now check it in gdb, create a breakpoint in the compare_pwd function like the last exercise:

![disassem](img/03.png)

then run it with an argument:

![argument](img/04.png)

We did not see a potential password in the registers or in the stack.


it's ok, we still have ‘my_secure_test’ function to test.

![secure](img/05.png)

![secure](img/06.png)

![secure](img/07.png)

Holy crap! it's too long.
    
it test al, al, if it is equal, we exit?? ok, it is probably in a loop ( *spoiler* not in a loop but if-else statement), can't explain it though. and cmp al to some hex characters.

To make it easier to visualize, we use Cutter program to graph the function (alternatively, you can also use r2 to view the graph: seek to the function then ‘VV’)

![VV](img/08.png)

by isolating cmp instruction using objdmp, then piping it to grep:

![objdmp2](img/09.png)

we will get this, then using python3 converting hex to chr:

![python](img/10.png)

then trying

![pass](img/11.png)

and done.
