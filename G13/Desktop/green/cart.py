from math import cos, sin, radians
from rich import print, inspect
#
def dcos(angle):
	return cos(radians(angle))
#
def dsin(angle):
	return sin(radians(angle))
#
class d2():
	def __init__(self,x=0.0,y=0.0):
		self.x = x
		self.y = y
	def al(self,angle=0.0,length=0.0):
		return d2(self.x + dcos(angle)*length, self.y + dsin(angle)*length)
	def show(self):
		print(f"[cyan]{round(self.x,2)}[/cyan]")
		print(f"[yellow]{round(self.y,2)}[/yellow]")

