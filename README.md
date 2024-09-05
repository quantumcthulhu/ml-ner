# NER Training Workflow

1. Run the default model:
   ```bash
   python3 try_default_model.py
   ```
Result:
```
------------------------------------------------------------
South Korea Unveils Guideline for Regulating Cryptocurrencies as Securities - DailyCoin.
  - GPE: 'South Korea' (start: 0, end: 11)
------------------------------------------------------------
Authorities in South Korea plan to define cryptocurrencies as financial securities in their regulatory framework.

  - GPE: 'South Korea' (start: 15, end: 26)
------------------------------------------------------------
Binance Coin (BNB) Price Staring at 23% Drop After Paxos Stops Minting BUSD.
  - PERSON: 'Binance Coin' (start: 0, end: 12)
  - PERSON: 'Staring' (start: 25, end: 32)
  - PERCENT: '23%' (start: 36, end: 39)
------------------------------------------------------------
The Binance Coin (BNB) price is correcting after a massive upward movement in Jan and some bad news from Paxos.

  - ORG: 'The Binance Coin (BNB' (start: 0, end: 21)
  - DATE: 'Jan' (start: 78, end: 81)
  - PERSON: 'Paxos' (start: 105, end: 110)
------------------------------------------------------------
Crypto scammers feel the chill: Revenue drops 46% in 2022 — Chainalysis.
  - PERCENT: '46%' (start: 46, end: 49)
  - DATE: '2022' (start: 53, end: 57)
------------------------------------------------------------
According to a crime report from blockchain data firm Chainalysis, crypto scam revenue dropped 46% in 2022, with noticeable drops occurring following the collapse of TerraLuna and FTX.

  - PERCENT: '46%' (start: 95, end: 98)
  - DATE: '2022' (start: 102, end: 106)
  - GPE: 'TerraLuna' (start: 166, end: 175)
  - ORG: 'FTX' (start: 180, end: 183)
------------------------------------------------------------
Dubai Prohibits Privacy Coins Like Monero Under New Crypto Rules.
  - ORG: 'Dubai Prohibits Privacy' (start: 0, end: 23)
  - PERSON: 'Monero' (start: 35, end: 41)
------------------------------------------------------------
The issuance of anonymity-enhancing crypto are banned under the Emirate's new regulations for digital assets.

  - ORG: 'Emirate' (start: 64, end: 71)
------------------------------------------------------------
OpenSea Unveils New Suite of Tools for NFT Creators - DailyCoin.
  - ORG: 'OpenSea Unveils New Suite' (start: 0, end: 25)
------------------------------------------------------------
OpenSea has announced a series of new tools to be rolled out on the marketplace for NFT creators.
  - ORG: 'OpenSea' (start: 0, end: 7)
  - ORG: 'NFT' (start: 84, end: 87)
------------------------------------------------------------
Read more.

------------------------------------------------------------
Only 31% of Staked Ether May Be Profitable: Binance Research.
  - PERCENT: 'Only 31%' (start: 0, end: 8)
  - ORG: 'Staked Ether May Be Profitable: Binance Research' (start: 12, end: 60)
------------------------------------------------------------
Around 2 million ETH were staked when prices were in the range of $400 to $600.
  - CARDINAL: 'Around 2 million' (start: 0, end: 16)
  - ORG: 'ETH' (start: 17, end: 20)
  - MONEY: '$400 to $' (start: 66, end: 75)
  - MONEY: '600' (start: 75, end: 78)
------------------------------------------------------------
These stakers are are some of the strongest Ethereum believers, according to Binance Research.

  - ORG: 'Ethereum' (start: 44, end: 52)
  - ORG: 'Binance Research' (start: 77, end: 93)
------------------------------------------------------------
What the U.S. Congress Decides on Crypto Will Ultimately Overstepping their authority | Blockchain News.
  - ORG: 'the U.S. Congress Decides' (start: 5, end: 30)
  - PERSON: 'Blockchain News' (start: 88, end: 103)
------------------------------------------------------------
Jake Chervinsky, the Blockchain Association's chief policy officer, criticized the SEC's enforcement-based regulation and urged Congress to regulate the sector.

  - PERSON: 'Jake Chervinsky' (start: 0, end: 15)
  - ORG: 'the Blockchain Association's' (start: 17, end: 45)
  - ORG: 'SEC' (start: 83, end: 86)
  - ORG: 'Congress' (start: 128, end: 136)
------------------------------------------------------------
France’s top modern art museum to display CryptoPunks, Autoglyphs NFTs.
  - GPE: 'France' (start: 0, end: 6)
  - PERSON: 'CryptoPunks' (start: 42, end: 53)
  - NORP: 'Autoglyphs' (start: 55, end: 65)
------------------------------------------------------------
The Centre Pompidou announced plans for a permanent exhibition focusing on NFTs.

------------------------------------------------------------
Snoop Dogg revealed as co-founder of Web3-powered livestream platform.
------------------------------------------------------------
American rapper Snoop Dogg is set to launch a Web3-based live streaming service named “Shiller,” which will connect creators of nonfungible token projects, artists and brands with their “Enthusiasts.”
  - NORP: 'American' (start: 0, end: 8)
  - PERSON: 'Snoop Dogg' (start: 16, end: 26)
  - ORG: 'Shiller' (start: 87, end: 94)
------------------------------------------------------------
Shillers can be paid in cryptocurrency in NFTs, which can then be converted to fiat.

------------------------------------------------------------
Jump Crypto unveils critical vulnerability on Binance’s BNB Chain.
  - PERSON: 'Jump Crypto' (start: 0, end: 11)
  - ORG: 'Binance’s BNB Chain' (start: 46, end: 65)
------------------------------------------------------------
Jump Crypto discovered a vulnerability in the Binance BNB Beacon Chain.
  - PERSON: 'Jump Crypto' (start: 0, end: 11)
  - ORG: 'the Binance BNB Beacon Chain' (start: 42, end: 70)
```   

2. Fetch articles for training:
   ```bash
   python3 fetch_articles_for_train.py
   ```

3. Use LLM with a prompt and training articles:
   ```bash
   ask LLM using prompt.txt on train_articles.txt
   # Then save the result:
   cat > train_entities.txt
   ```

4. Create training data:
   ```bash
   python3 create_train_data.py > train_data.txt
   ```

5. Train the model:
   ```bash
   python3 train.py
   ```

### Training Log

```
Starting training for fold 1...
Training model for fold 1...
Training completed for fold 1 in 95.94 seconds.
Evaluating model for fold 1...
Evaluation completed for fold 1 in 0.40 seconds.
Fold 1 completed in 97.47 seconds.
Fold 1 - F1: 0.7898089171974522, Model saved to cv_models/model_fold_1
Starting training for fold 2...
Training model for fold 2...
Training completed for fold 2 in 92.56 seconds.
Evaluating model for fold 2...
Evaluation completed for fold 2 in 0.38 seconds.
Fold 2 completed in 94.09 seconds.
Fold 2 - F1: 0.8481481481481482, Model saved to cv_models/model_fold_2
Starting training for fold 3...
Training model for fold 3...
Training completed for fold 3 in 92.88 seconds.
Evaluating model for fold 3...
Evaluation completed for fold 3 in 0.37 seconds.
Fold 3 completed in 94.21 seconds.
Fold 3 - F1: 0.8839103869653768, Model saved to cv_models/model_fold_3
Starting training for fold 4...
Training model for fold 4...
Training completed for fold 4 in 91.69 seconds.
Evaluating model for fold 4...
Evaluation completed for fold 4 in 0.37 seconds.
Fold 4 completed in 93.04 seconds.
Fold 4 - F1: 0.832699619771863, Model saved to cv_models/model_fold_4
Starting training for fold 5...
Training model for fold 5...
Training completed for fold 5 in 93.37 seconds.
Evaluating model for fold 5...
Evaluation completed for fold 5 in 0.38 seconds.
Fold 5 completed in 94.72 seconds.
Fold 5 - F1: 0.8380281690140845, Model saved to cv_models/model_fold_5
Best model is from fold 3 with F1 score: 0.8839103869653768
Best model saved to best_model
```

6. Try the best model:
   ```bash
   python3 try_best_model.py
   ```

Result:
```
------------------------------------------------------------
South Korea Unveils Guideline for Regulating Cryptocurrencies as Securities - DailyCoin.
------------------------------------------------------------
Authorities in South Korea plan to define cryptocurrencies as financial securities in their regulatory framework.
------------------------------------------------------------

Binance Coin (BNB) Price Staring at 23% Drop After Paxos Stops Minting BUSD.
  - EXCHANGE: 'Binance' (start: 1, end: 8)
  - TOKEN: 'BNB' (start: 15, end: 18)
  - COMPANY: 'Paxos' (start: 52, end: 57)
  - TOKEN: 'BUSD' (start: 72, end: 76)
------------------------------------------------------------
The Binance Coin (BNB) price is correcting after a massive upward movement in Jan and some bad news from Paxos.
  - EXCHANGE: 'Binance' (start: 4, end: 11)
  - TOKEN: 'BNB' (start: 18, end: 21)
  - COMPANY: 'Paxos' (start: 105, end: 110)
------------------------------------------------------------

Crypto scammers feel the chill: Revenue drops 46% in 2022 — Chainalysis.
  - COMPANY: 'Chainalysis' (start: 61, end: 72)
------------------------------------------------------------
According to a crime report from blockchain data firm Chainalysis, crypto scam revenue dropped 46% in 2022, with noticeable drops occurring following the collapse of TerraLuna and FTX.
  - COMPANY: 'Chainalysis' (start: 54, end: 65)
  - EXCHANGE: 'FTX' (start: 180, end: 183)
------------------------------------------------------------

Dubai Prohibits Privacy Coins Like Monero Under New Crypto Rules.
------------------------------------------------------------
The issuance of anonymity-enhancing crypto are banned under the Emirate's new regulations for digital assets.
------------------------------------------------------------

OpenSea Unveils New Suite of Tools for NFT Creators - DailyCoin.
  - COMPANY: 'OpenSea' (start: 1, end: 8)
  - TECHNOLOGY: 'NFT' (start: 40, end: 43)
------------------------------------------------------------
OpenSea has announced a series of new tools to be rolled out on the marketplace for NFT creators.
  - COMPANY: 'OpenSea' (start: 0, end: 7)
  - TECHNOLOGY: 'NFT' (start: 84, end: 87)
------------------------------------------------------------
Read more.
------------------------------------------------------------

Only 31% of Staked Ether May Be Profitable: Binance Research.
  - TOKEN: 'Ether' (start: 20, end: 25)
  - EXCHANGE: 'Binance' (start: 45, end: 52)
------------------------------------------------------------
Around 2 million ETH were staked when prices were in the range of $400 to $600.
  - TOKEN: 'ETH' (start: 17, end: 20)
------------------------------------------------------------
These stakers are are some of the strongest Ethereum believers, according to Binance Research.
  - BLOCKCHAIN: 'Ethereum' (start: 44, end: 52)
  - EXCHANGE: 'Binance' (start: 77, end: 84)
------------------------------------------------------------

What the U.S. Congress Decides on Crypto Will Ultimately Overstepping their authority | Blockchain News.
  - TECHNOLOGY: 'Blockchain' (start: 89, end: 99)
------------------------------------------------------------
Jake Chervinsky, the Blockchain Association's chief policy officer, criticized the SEC's enforcement-based regulation and urged Congress to regulate the sector.
  - TECHNOLOGY: 'Blockchain' (start: 21, end: 31)
  - REGULATORY: 'SEC' (start: 83, end: 86)
------------------------------------------------------------

France’s top modern art museum to display CryptoPunks, Autoglyphs NFTs.
  - TECHNOLOGY: 'NFTs' (start: 67, end: 71)
------------------------------------------------------------
The Centre Pompidou announced plans for a permanent exhibition focusing on NFTs.
  - TECHNOLOGY: 'NFTs' (start: 75, end: 79)
------------------------------------------------------------

Snoop Dogg revealed as co-founder of Web3-powered livestream platform.
  - TECHNOLOGY: 'Web3' (start: 38, end: 42)
------------------------------------------------------------
American rapper Snoop Dogg is set to launch a Web3-based live streaming service named “Shiller,” which will connect creators of nonfungible token projects, artists and brands with their “Enthusiasts.”
  - TECHNOLOGY: 'Web3' (start: 46, end: 50)
  - COMPANY: 'Shiller' (start: 87, end: 94)
------------------------------------------------------------
Shillers can be paid in cryptocurrency in NFTs, which can then be converted to fiat.
  - TECHNOLOGY: 'NFTs' (start: 42, end: 46)
------------------------------------------------------------

Jump Crypto unveils critical vulnerability on Binance’s BNB Chain.
  - COMPANY: 'Jump Crypto' (start: 1, end: 12)
  - EXCHANGE: 'Binance' (start: 47, end: 54)
  - BLOCKCHAIN: 'BNB Chain' (start: 57, end: 66)
------------------------------------------------------------
Jump Crypto discovered a vulnerability in the Binance BNB Beacon Chain.
  - COMPANY: 'Jump Crypto' (start: 0, end: 11)
  - BLOCKCHAIN: 'Binance BNB' (start: 46, end: 57)
  - COMPANY: 'Chain' (start: 65, end: 70)
```