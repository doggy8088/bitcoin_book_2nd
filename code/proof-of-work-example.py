#!/usr/bin/env python
# Proof-of-Work 演算法範例

import hashlib
import time

try:
    long        # Python 2
    xrange
except NameError:
    long = int  # Python 3
    xrange = range

max_nonce = 2 ** 32  # 40億


def proof_of_work(header, difficulty_bits):
    # 計算難度目標
    target = 2 ** (256 - difficulty_bits)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header) + str(nonce)).hexdigest()

        # 檢查是否是目標值以下的有效結果
        if long(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hash_result)
            return (hash_result, nonce)

    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce


if __name__ == '__main__':
    nonce = 0
    hash_result = ''

    # 難度從0到31位
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print("Starting search...")

        # 當前時間
        start_time = time.time()

        # 建立一個包含前一個塊的雜湊的新塊
        # 我們偽造一個交易塊 —— 只是一個字串。
        new_block = 'test block with transactions' + hash_result

        # 為新塊找到一個有效的nonce
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # 記錄需要多長時間才能找到結果
        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:

            # 估計每秒的雜湊計算次數
            hash_power = float(long(nonce) / elapsed_time)
            print("Hashing Power: %ld hashes per second" % hash_power)
