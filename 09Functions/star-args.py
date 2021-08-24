def ensure_correct_info(*args):
	if "Eric" in args and "dev" in args:
		return "Welcome back Eric!"
	return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "Eric", "dev"))

