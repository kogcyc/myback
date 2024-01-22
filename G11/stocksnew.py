from rich import print

lines = []

while True:
	line = input(":")
	if not line:
		break
	lines.append(line)

blist = []
for t in lines:
	blist.append(t.split())

a = float(blist[1][0])
b = float(blist[1][1])
c = float(blist[4][0])
d = float(blist[4][1])
e = float(blist[7][0])
f = float(blist[7][1])


g  = round((a*40+c*240+e*30),0)
h  = round((b*40+d*240+f*30),0)


if h > 0.0:
	#console.print(h,style='bold green')
	print(f"[bold green]{h}[/bold green]")

else:
	print(f"[bold red]{h}[/bold red]")

print(f"[bold yellow]{g}[/bold yellow]")
