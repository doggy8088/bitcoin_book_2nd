from bitcoin.rpc import RawProxy

# 與本地Bitcoin Core節點建立連線
p = RawProxy()

# 執行 getblockchaininfo 命令, 將返回資料儲存到info中
info = p.getblockchaininfo()

# 列印info中的blocks內容
print(info['blocks'])
