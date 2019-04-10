# =============================================================================
# BEGIN OF FILE
# =============================================================================
"""
This file shows how to use 'logging' module, also how to use a dictionary for
emulate cache and can use recursive functions.

It will create two files when it is executed.
1) a log file, indicating relevant info 
2) a cache file, for save data 
"""
# Configure the session
import logging
logging.basicConfig( filename = "ejemplo_fibonacci.log", \
	                 level = logging.DEBUG, \
	                 format = "%(asctime)s|%(levelname)-7s|%(lineno)-5d|%(message)s",
	                 filemode = "w" )
# Levels names : NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
# Levels number: 0, 10, 20, 30, 40, 50
# logging.info("".center(50,"*"))
logging.info("Initiating program.")
# =============================================================================
# MODULES
# =============================================================================
logging.info("Loading modules and functions.") 

from time import time                 # for measure code time
import json                           # for works with json files
import os                             # for type terminal commands
import platform                       # for know the os/system
from collections import OrderedDict   # for create a ordered dictionary
# =============================================================================
# DETAILS
# =============================================================================
# call("clear")
os.system("clear")
print("".center(80,"="))
print(" ".join(" BEGIN OF PROGRAM ").center(80,"-"))
print("".center(80,"="))
start_time = time()           # Start to measure time
# =============================================================================
# BEGIN OF CODE
# =============================================================================
logging.info("Beginning code.")

# ===========================
# Parameters
# ===========================

# Path variables
my_paths = {'file_directory' : os.getcwd(),                                                      \
            'file_python'    : os.path.basename(__file__),                                       \
            'file_log'       : os.path.splitext( os.path.basename(__file__) )[0] + ".log",       \
            'file_cache'     : os.path.splitext( os.path.basename(__file__) )[0] + "_cache.json" }

# ===========================
# Functions
# ===========================

# Create 'fib_cache' for save data ( it is a empty dictionary )
# Note:   The key is character and the value is int
fib_cache = OrderedDict()
# Check if 'fib_cache.json' exists and if exists, load it
try:
	with open( my_paths['file_cache'],"rt" ) as f:
		logging.info("'{}' was founded.".format( my_paths['file_cache'] ) )
		fib_cache = OrderedDict( json.load(f) )
except:
	logging.warning("'{}' was not founded.".format( my_paths['file_cache'] ) )
	# -------------------------------------------------------------------------
	# Note: 
	# The next sentence is a variation for the program. This is because, although 
	# the dictionary has type(key) = int, when we type 'json.dumps(*)', json turn into
	# type(key) = string.
	#
	# Sentence: 
	# fib_cache = { int(x) : y for x in fib_cache.keys() for y in fib_cache.values() }

# Define fibonacci function 
def fib(x):
	"""
	This function compute the n-th number of fibonacci's serie

	The first 10 numbers of the serie are:
	{'1':1 , '2':1, '3':2 , '4':3, '5':5, '6':8, '7':13, '8':21, '9':34, '10':55}
	"""
	# The next line helps to manipulate 'fib_cache'
	global fib_cache 
	# Check if value is in cache
	# if x in fib_cache.keys():
	temp = fib_cache.get(str(x),None)
	if temp != None:
		return temp
	# If value is not in cache, then we check the different cases
	if x == 2 or x == 1:
		answer = 1
	# Do recursivity
	else:
		answer = fib(x-1)+fib(x-2)
	# We put the answer into dictionary
	fib_cache[str(x)] = answer
	return answer

def open_file(path):
	"""
	Open a file from shell depending of the operating system
	"""
	# print "OS: " + platform.system() 
	try:
		if platform.system() == "Darwin":
			os.system("open " + path)
		else:
			os.startfile(path)
	except:
		print("Error: File was not opened")

# ===========================
# Code
# ===========================

# Ask to user until what number he wants calcultate fibonacci function
logging.info("Begins iterations.")
while True:
	try: 
		ans = int(float(input("\nUntil what number do you want calculate? [positive integer]\n> ")))
		if ans <= 0:
			print("The answer must be a positive integer")
	except:
		print("The answer is not a number")
	else:
		print("")
		break

# Do a loop for 
fib_series = {}
time0 = time()
for i in ( k for k in range(1, ans+1) ): # This is a generator!!!!
	logging.debug("Iteration : {}".format(i))
	fib_series[i] = fib(i)
time1 = time()
print "Time elapsed: " + str( time1-time0 ) + "\n"

for i in range(1, min( 5, ans) + 1 ):
	print("Fib({}) = {}".format(i,fib_series[i]))
if ans > 5:
	print("...")
	for i in range( ans-5+1, ans+1):
		print("Fib({}) = {}".format(i,fib_series[i]))
	
# Ask to user if he wants show fib_cache in json format
logging.info("Asking user if he wants show fib_cache in json format.")
if raw_input("\nDo you want review 'fib_cache' in json format? [y|n]\n> ").upper() == "Y":
	print( json.dumps( fib_cache, indent=2, ensure_ascii=True, sort_keys=False) )
	# open_file( my_paths['file_cache'] )

# Save fib_cache to json format
print fib_cache
logging.info("Saving 'fib_cache.json'")
with open(my_paths['file_cache'],"wt") as f:
	json.dump( fib_cache, f, indent=2, ensure_ascii=True, sort_keys=False)

# =============================================================================
# END OF CODE
# =============================================================================
print("".center(80,"="))
print(" ".join(" END OF PROGRAM ").center(80,"-"))
print("".center(80,"="))
logging.info("Endding code.")
finish_time = time()
logging.info("Code finished correctly in {} seconds.".format( finish_time-start_time ))
logging.shutdown()
# =============================================================================
# END OF FILE
# =============================================================================
