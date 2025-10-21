def info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

print(info(pakistan="karachi",china="bejing",russia="Moscow",india="Delhi"))