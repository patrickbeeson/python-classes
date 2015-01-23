#!/usr/local/bin/python3
""" Contains functions to manipulate number representations. """

def commafy(val):
    if len(val) < 4:
        return val
    out = []
    while val:
        out.append(val[-3:])
        val = val[:-3]
    return ",".join(reversed(out))

def commareal(val):
    if "." in val:
        before, after = val.split(".", 1)
    else:
        before, after = val, "0"
    return "{0}.{1}".format(commafy(before), (after))

if __name__ == "__main__":
    for i in [0, 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890]:
        print(i, ":", commafy(str(i)), ":", commareal("{0:.2f}".format(i/1000)))
