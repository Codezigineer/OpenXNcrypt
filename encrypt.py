import os, urllib as u, json as j

def encrypt(ustr):
    """
    Encrypt a string.
    """
    int = j.loads(u.urlopen("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=hex16&size=1024").read())['data'][0]

    return pow(long(ustr.__len__(), long("0x" + int, base=0))

def test():
    i = encrypt("oo")
    ii = encrypt("oo")

    print(i)
    print(ii)