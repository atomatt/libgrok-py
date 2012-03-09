import libgrok
import sys

g = libgrok.Grok()

for filename in sys.argv[1:]:
    g.add_patterns_from_file(filename)

g.compile(r"^%{NUMBER}$")
print g("200")
print g("404")
