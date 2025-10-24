

import logging

logging.basicConfig(filename="myfile.log", filemode="w",
                level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(name)s : %(message)s")

# name = "Jack"
# logging.error("%s raised an error", name)

def diff(x, y):
    return x - y

a = 20
b = 10

logging.debug(f"Difference of {a} and {b} is :{diff(a, b)}")
logging.info(f"Difference of {a} and {b} is {diff(a, b)}")

a = 30
b = 20

logging.error(f"The difference of {a} and {b} is :{diff(a, b)}")
logging.critical(f"The difference of {a} and {b} is :{diff(a, b)}")
