import re


def longest_palindromic(text):
    slen = len(text)
    res = text[0]
    for i in range(slen-1):
        print(i)
        k = 0
        while i + k < slen and i - k >= 0:
            print(i, k, text)
            print(l_n_r(i, k, text))
            if l_n_r(i,k,text) == l_n_r(i,k,text)[::-1]:
                res = l_n_r(i,k,text)
                k += 1
            else:
                k += 1
                break

    print(res)


def l_n_r(i,k,text):
    if len(text) % 2 == 0:
        l = i - k
        r = i
    else:
        l = i - k
        r = i + k
    return text[r:l]


#longest_palindromic("artrartrt")
longest_palindromic("abacada")
longest_palindromic("aaaa")

