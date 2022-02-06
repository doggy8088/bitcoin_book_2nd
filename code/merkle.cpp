#include <bitcoin/bitcoin.hpp>

bc::hash_digest create_merkle(bc::hash_list& merkle)
{
    if (merkle.empty())
        return bc::null_hash;
    else if (merkle.size() == 1)
        return merkle[0];

    // 只要有多於1個雜湊，循環繼續
    while (merkle.size() > 1)
    {
        // 如果雜湊值數量為奇數，複製列表中最後一個雜湊值
        if (merkle.size() % 2 != 0)
            merkle.push_back(merkle.back());
        // 列表大小為偶數
        assert(merkle.size() % 2 == 0);

        // 新的雜湊值列表
        bc::hash_list new_merkle;
        // 每次計算兩個
        for (auto it = merkle.begin(); it != merkle.end(); it += 2)
        {
            // 連接兩個雜湊值
            bc::data_chunk concat_data(bc::hash_size * 2);
            auto concat = bc::serializer<
                decltype(concat_data.begin())>(concat_data.begin());
            concat.write_hash(*it);
            concat.write_hash(*(it + 1));
            // 散列
            bc::hash_digest new_root = bc::bitcoin_hash(concat_data);
            // 將雜湊值添加到列表
            new_merkle.push_back(new_root);
        }
        // 替换為新的列表
        merkle = new_merkle;

        // DEBUG 輸出 -------------------------------------
        std::cout << "Current merkle hash list:" << std::endl;
        for (const auto& hash: merkle)
            std::cout << "  " << bc::encode_base16(hash) << std::endl;
        std::cout << std::endl;
        // --------------------------------------------------
    }
    // 最終以一個雜湊值結束，即 merkle root
    return merkle[0];
}

int main()
{
    bc::hash_list tx_hashes{{
        bc::hash_literal("0000000000000000000000000000000000000000000000000000000000000000"),
        bc::hash_literal("0000000000000000000000000000000000000000000000000000000000000011"),
        bc::hash_literal("0000000000000000000000000000000000000000000000000000000000000022"),
    }};
    const bc::hash_digest merkle_root = create_merkle(tx_hashes);
    std::cout << "Result: " << bc::encode_base16(merkle_root) << std::endl;
    return 0;
}
