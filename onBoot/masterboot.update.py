import datetime
print("functional")
date = datetime.time.now()
version = "0.0.0"
boot = open("record\boot.ini", "a")
boot.write("[version[" + version + "]][date["+ date +"]]")
boot.write("\n")
