import base64

def string_xor(key, pwd):
    res = ''

    for i in range(len(key)):
        res = res+(chr(ord(key[i])^pwd[i]))    
    return res

key = 'c92fcd618967933ac463feb85ba00d5a7ae52842'
pwd = 'VA5QA1cCVQgPXwEAXwZVVVsHBgtfUVBaV1QEAwIFVAJWAwBRC1tRVA=='

print(string_xor(key, base64.b64decode(pwd)))