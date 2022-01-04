import argparse


parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
parser.add_argument("-d", dest="is_debug", action='store_true')
args = parser.parse_args()

DEBUG_MODE: bool = args.is_debug


def find_number_factor(n: int) -> list[int]:
	number_factors: list[int] = []
	i: int = 1
	while n != 1:
		div, mod = divmod(n, i)
		if not mod and i != 1:
			if DEBUG_MODE: 
				print(f"{n=} / {i=} -> {div=} {mod=}")
			number_factors.append(i)
			n = div
		i += 1
	return number_factors


def main() -> int:
	print(f"Largest prime number of {args.number} is {max(find_number_factor(args.number))}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())