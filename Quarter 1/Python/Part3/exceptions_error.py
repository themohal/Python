#runtime error handling

try:
    5/0
except ZeroDivisionError as f:
    print(f)
else:
    print("no error")
finally:
    print("this will excute whatever happens")
