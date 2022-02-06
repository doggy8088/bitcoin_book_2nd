# 在雜湊演算法的輸入中迭代nonce的例子。

from __future__ import print_function
import hashlib

text = "I am Satoshi Nakamoto"

# 從0到19迭代nonce
for nonce in range(20):

    # 將nonce新增到文字的末尾
    input_data = text + str(nonce)

    # 計算輸入的SHA-256雜湊(文字+nonce)
    hash_data = hashlib.sha256(input_data).hexdigest()

    # 顯示輸入和雜湊結果
    print(input_data, '=>', hash_data)
