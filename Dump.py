import os, sys
try:
    __import__("test").Mind()
except Exception as e:
    exit(str(e))
