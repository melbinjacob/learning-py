count = 0
def callCounter():
        global count
        count += 1
        print("CallCounter have called " + str(count) + " times")

callCounter()
callCounter()
callCounter()
callCounter()
callCounter()

