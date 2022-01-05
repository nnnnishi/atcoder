from math import gcd


def lcm(p, q):
    """
  最小公倍数を求める。
  """
    return (p * q) // gcd(p, q)


def generate_keys(p, q):
    """
  与えられた 2 つの素数 p, q から秘密鍵と公開鍵を生成する。
  """
    N = p * q
    L = lcm(p - 1, q - 1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    return (E, N), (D, N)


def encrypt(plain_text, public_key):
    """
    公開鍵 public_key を使って平文 plain_text を暗号化する。
    """
    E, N = public_key
    plain_integers = [ord(char) for char in plain_text]
    encrypted_integers = [pow(i, E, N) for i in plain_integers]
    encrypted_text = "".join(chr(i) for i in encrypted_integers)

    return encrypted_text


def decrypt(encrypted_text, private_key):
    """
  秘密鍵 private_key を使って暗号文 encrypted_text を復号する。
  """
    D, N = private_key
    encrypted_integers = [ord(char) for char in encrypted_text]
    decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
    decrypted_text = "".join(chr(i) for i in decrypted_intergers)

    return decrypted_text


def sanitize(encrypted_text):
    """
  UnicodeEncodeError が置きないようにする。
  """
    return encrypted_text.encode("utf-8", "replace").decode("utf-8")


if __name__ == "__main__":
    # 2つの大きな素数p,qを用意、それぞれから1ひいて積をとり最小公倍数Lを算出
    # 最小公倍数Lと素なEとp*q公開鍵に
    # 整数Eの法Lのもとでの逆数（モジュラ逆数）Dを秘密鍵に
    public_key, private_key = generate_keys(101, 3259)
    plain_text = "あああ"
    # テキストのE乗の法Nでの剰余が暗号化テキスト
    encrypted_text = encrypt(plain_text, public_key)
    # 暗号化テキストをD乗した法Nの剰余がもとのテキスト
    # テキストのED乗の法Nはテキストの1乗となる -> L=(p-1)(q-1)とするとそうなることが知られている
    # EはDの法Lでの逆数 -> 大きな素数同士の掛け算だとEからDを求めるのは難しい
    decrypted_text = decrypt(encrypted_text, private_key)

    print(
        f"""
秘密鍵: {public_key}
公開鍵: {private_key}

平文:
「{plain_text}」

暗号文:
「{sanitize(encrypted_text)}」

平文 (復号後):
「{decrypted_text}」
"""[
            1:-1
        ]
    )

