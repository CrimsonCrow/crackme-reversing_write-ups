The goal is make the program print `password OK`

First, we execute the program:

![try](img/01.png)

The hint we get in this program is that the password is hidden and used strcmp.

Using the strings program and hoping that the password is there:

![strings](img/02.png)

Unfortunately, we did not see a potential password here in the output.

![string-out](img/03.png)

Using the program objdump, then piping it to grep:

![objdmp](img/04.png)

We get this list of functions. What got our interest are the functions <main>, <compare_pwd>, and <get_pwd>.

We fire up gdb w/ GEF, and disassemble the <compare_pwd> function:

![gdb](img/05.png)

As hinted from the beginning, that the password is hidden using strcmp. We created a breakpoint at the address of calling the strcmp function:

![strcmp](img/06.png)

then, and run the program with argument:

![run](img/07.png)

![registers](img/08.png)

We will see in the stack section the argument we use running the program, and the string “my_m0r3_secur3_pwd” that the program compares our argument.
    
it really looks like the password we are looking for.
   
trying it

![pass](img/09.png)

and done.
