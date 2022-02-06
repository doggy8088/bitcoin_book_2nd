from bitcoin.rpc import RawProxy

p = RawProxy()

# Alice的交易所在的區塊
blockheight = 277316

# 獲得區塊的雜湊值
blockhash = p.getblockhash(blockheight)

# 根據雜湊值檢索區塊
block = p.getblock(blockhash)

# tx元素包含塊中的所有交易ID
transactions = block['tx']

block_value = 0

# 遍歷區塊中的每個交易ID
for txid in transactions:
    tx_value = 0
    # 使用ID檢索原始交易數據
    raw_tx = p.getrawtransaction(txid)
    # 解析交易數據
    decoded_tx = p.decoderawtransaction(raw_tx)
    # 遍歷交易的所有輸出
    for output in decoded_tx['vout']:
        # 累加交易的輸出
        tx_value = tx_value + output['value']

    # 累計到區塊的所有輸出
    block_value = block_value + tx_value

print("Total value in block: ", block_value)
