def collatz_map_on_linear(coeff):
	if coeff[0] % 2:
		print(f"Collatz map behavior cannot be predicted when the leading coefficient is odd")
		return None
	if coeff[1] % 2:
		return [3*coeff[0]//2 , (3*coeff[1]+1)//2]
	else:
		return [coeff[0]//2, coeff[1]//2]

def generate_inequality(k = 5):
	left_side = ""
	right_side = ""
	for i in range(1, 2**k):
		coeff = [2**k, i]
		for _ in range(k):
			coeff = collatz_map_on_linear(coeff)
		A = coeff[0]
		B = coeff[1]*2**k - coeff[0]*i
		left_side += (f"{A}^[\Omega_[{i},{k}]]").replace("[", "{").replace("]", "}")
		right_side += (f"({A}+{B}m^[-1])^[\Omega_[{i}, {k}]] ").replace("[", "{").replace("]", "}")
	print(f"$$ {left_side} < {2**k}^[\Omega] < {right_side} $$".replace("[", "{").replace("]", "}"))

generate_inequality(3)
