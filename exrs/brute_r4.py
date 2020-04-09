import subprocess

def bruteforce():
    found = 0
    n = 0
    test = ""
    with open('pass.txt', 'r') as file:
        test = file.read().split('\n')
    pwd = ""
    while found == 0:
        pwd = test[n]

        p = subprocess.Popen(["./r4", pwd], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, something = p.communicate()
        out_decoded = stdout.decode('ascii')
        #print(stdout, pwd) #debug

        if "password KO" in out_decoded:
            print('attempt: ' + str(n))
            print('test: ' + pwd)
            print('out: ' + out_decoded)

        if "password OK" in out_decoded:
            print("-------found-------")
            print("attempt: " +str(n))
            print(pwd)
            print(out_decoded)
            found = 1
            break
        n += 1
bruteforce()
