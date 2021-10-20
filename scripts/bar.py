"""
"bar" == "Build And Run"
This is pritty basic script that builds C++ file with g++ and puts executable to build folder.
"""
import os
import argparse
import pathlib


# TODO: Refactor 
class Gpp(object):

	filepath: str
	destpath: str

	def __init__(self, filepath: str, destpath: str) -> None:
		self.filepath = filepath
		self.destpath = destpath

	def build(self) -> int:
		print(f"[INFO]: Starting building process of {self.filepath}. Dest path: {self.destpath}")
		return os.system(f"g++ {self.filepath} -o {self.destpath}")

	def run(self) -> int:
		print(f"[INFO]: Running executable {self.destpath}")
		return os.system(self.destpath)


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("filepath")
	parser.add_argument("--destpath")
	args = parser.parse_args()

	if args.destpath is None:
		args.destpath = fr".\build\{pathlib.Path(args.filepath).stem}.exe"  # TODO: get filename with sys.path
	
	gpp = Gpp(args.filepath, args.destpath)
	
	build_res = gpp.build()
	if not build_res:
		run_res = gpp.run()
		return run_res
	else:
		return build_res


if __name__ == "__main__":
	raise SystemExit(main())
