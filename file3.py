import logging
logging.basicConfig(level=logging.DEBUG)
def add(a, b):
   logging.debug(f"a: {a}, b: {b}")
   return a + b
add(2, 3)
