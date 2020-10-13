import time
import rpyc
import sys

start = time.time()
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

c = rpyc.connect(server, 18861)

# print(c.root)
# print(c.root.get_answer())
# print(c.root.the_real_answer_though)
print(c.root.get_sum(100))

end = time.time()
print(end - start)
