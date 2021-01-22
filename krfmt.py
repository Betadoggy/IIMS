# 한글 포매팅 모듈

from wcwidth import wcswidth

def fmt(x, w, align='r'):
    x = str(x)
    l = wcswidth(x)
    s = w - l

    if s<=0:
        return x
    if align == 'l':
        return x + ' ' * s
    if align == 'c':
        sl = s//2
        sr = s - sl
        return ' ' * sl + x + ' ' * sr
    return ' ' * s + x


if __name__ == "__main__":
    print("krfmt.py")