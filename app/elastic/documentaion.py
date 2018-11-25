import sys

out = sys.stdout
fname = "doc.txt"

sys.stdout = open(fname, "w")

import es_connection
help(es_connection)

sys.stdout.close()

sys.stdout = out