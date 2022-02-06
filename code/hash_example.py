# 在雜湊算法的輸入中疊代nonce的例子。

from __future__ import print_function
import hashlib

text = "I am Satoshi Nakamoto"

# 從0到19疊代nonce
for nonce in range(20):

    # 將nonce添加到文本的末尾
    input_data = text + str(nonce)

    # 計算輸入的SHA-256雜湊(文本+nonce)
    hash_data = hashlib.sha256(input_data).hexdigest()

    # 顯示輸入和散列結果
    print(input_data, '=>', hash_data)
