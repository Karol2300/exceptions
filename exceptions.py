user_input = "ala"

try:
    x = [2, 3][int(user_input) // 1]

except ValueError:

     raise IndexError("No data")

except ZeroDivisionError:
    x = "lol"
except TypeError:
    x = "float"
except IndexError:
    x = "idx"
print(x)