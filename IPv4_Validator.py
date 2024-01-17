#IP Address Validator
import re

def main():
    print(validate(input("IPv4 Address: ")))

#returns true or false based on IP address
def validate(ip):
    if addie:=re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip, re.IGNORECASE):
        if int(addie.group(1))>255:
            return False
        elif int(addie.group(2))>255:
            return False
        elif int(addie.group(3))>255:
            return False
        elif int(addie.group(4))>255:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()