t = "1"
e = "00"
a = "0010"
k = "0110"
c = "1010"
r = "1110"
teacrate = t+e+a+c+r+a+t+e
eatcake = e+a+t+c+a+k+e
takecare = t+a+k+e+c+a+r+e
retake = r+e+t+a+k+e
if teacrate == "1001001100010100010111000":
    print("The answer is: TEACRATE - " + teacrate)
elif eatcake == "1001001100010100010111000":
    print("The answer is: EATCAKE - " + eatcake)
elif takecare == "1001001100010100010111000":
    print("The answer is: TAKECARE - " + takecare)
elif retake == "1001001100010100010111000":
    print("The answer is: RETAKE - " + retake)
