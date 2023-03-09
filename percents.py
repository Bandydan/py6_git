sdlkvjaskjv
as;lva;lsva;ldsnv
a;lkdsvn;lskdnvdslknv

result = int(input("Givee mee a begin num: "))
plus = int(input("Givee mee a plus num: "))
months = int(input("Givee mee a months num: "))

for month in range(1, months + 1):
	percent = result * 0.15/12
	tax = percent * 0.18
	war = percent * 0.015
	percent -= war + tax
	print(f"{month}: We added {percent:.2f} to {result:.2f}")
	result += percent
	print(f"Now it is {result:.2f}")
	result += plus
	print(f"After adding {plus} we have {result:.2f}")

print(f"After {months} months we have {result:.2f}")

