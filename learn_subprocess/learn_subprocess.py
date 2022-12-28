import subprocess as sp

cmd = ['grep','-i','cod'] # grep -i cod some_file
ps = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE)
ps.stdin.write(b"CADe\n")
ps.stdin.write(b"Code\n")
ps.stdin.write(b"COde\n")
ps.stdin.write(b"CoDe\n")
ps.stdin.close()
print(ps.stdout.read().decode())
ps.wait()