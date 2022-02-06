/*
  展示中本聰創世區塊中的信息
*/
#include <iostream>
#include <bitcoin/bitcoin.hpp>

int main()
{
    // 創建創世區塊
    bc::chain::block block = bc::chain::block::genesis_mainnet();
    // 創世區塊包含單一的幣基交易
    assert(block.transactions().size() == 1);
    // 取得區塊中的第一個交易
    const bc::chain::transaction& coinbase_tx = block.transactions()[0];
    // 幣基交易 tx 有一個輸入
    assert(coinbase_tx.inputs().size() == 1);
    const bc::chain::input& coinbase_input = coinbase_tx.inputs()[0];
    // 將輸入腳本轉換為其原始形式
    const auto prefix = false;
    const bc::data_chunk& raw_message = coinbase_input.script().to_data(prefix);
    // 轉換為std::string
    std::string message(raw_message.begin(), raw_message.end());
    // 展示訊息
    std::cout << message << std::endl;
    return 0;
}
