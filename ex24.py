print("Let's practice everything.")
print('''You\'d need to know about escape with \\ that do \n newline
and \t tabs,''')

poem = """
\tThe lovely world
with logic so firmly placted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none."""

print("_____"*3)
print(poem)
print("-----"*3)

five=10-2+3-6
print("This should be five: %s" % five)

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/100
	crates = jars/100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans,%d jars, and %d crates." % (beans, jars, crates))

start_point = start_point/10

print("We can also do that this way:")
print("We'd have %d beans,%d jars, and %d crates." % secret_formula(start_point))