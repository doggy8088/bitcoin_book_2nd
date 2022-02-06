from bitcoin.rpc import RawProxy

p = RawProxy()

# Alice's 交易 ID
txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

# 首先, 取得原始十六進制交易數據
raw_tx = p.getrawtransaction(txid)

# 解碼交易數據成JSON物件
decoded_tx = p.decoderawtransaction(raw_tx)

# 印出交易的每個輸出
for output in decoded_tx['vout']:
    print(output['scriptPubKey']['addresses'], output['value'])
