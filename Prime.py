# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import thread

#Prime Counter
isStart=False
class PrimeCommand(sublime_plugin.WindowCommand):
	prime = 1
	def run(self):
		global isStart
		if isStart:
			isStart = False;
			self.prime = 1
		else:
			isStart = True
			self.increment()
	def description(self, args):
		return "prime counter."
	def increment(self):
		if isStart == True:
			self.prime = self.next_prime(self.prime)
			sublime.status_message("Let's calm down and count the prime..."+str(self.prime))
			sublime.set_timeout(lambda:self.increment(), 1000)
	def next_prime(self, now):
		p = now
		while True:
			is_prime = True
			p = p+1
			div_max = p/2
			if div_max < 2:
				return p
			for i in range(2, div_max+1):
				if p%i == 0:
					is_prime = False
					break
			if is_prime==True:
				return p
