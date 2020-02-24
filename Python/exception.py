try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple test")

except:
    print("Can't find file to write")

finally:
    print("I am always done!")
