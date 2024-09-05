import spacy
from spacy import displacy
nlp = spacy.load("best_model")

nlp.add_pipe('sentencizer')

article = '''South Korea Unveils Guideline for Regulating Cryptocurrencies as Securities - DailyCoin. Authorities in South Korea plan to define cryptocurrencies as financial securities in their regulatory framework.
Binance Coin (BNB) Price Staring at 23% Drop After Paxos Stops Minting BUSD. The Binance Coin (BNB) price is correcting after a massive upward movement in Jan and some bad news from Paxos.
Crypto scammers feel the chill: Revenue drops 46% in 2022 — Chainalysis. According to a crime report from blockchain data firm Chainalysis, crypto scam revenue dropped 46% in 2022, with noticeable drops occurring following the collapse of TerraLuna and FTX.
Dubai Prohibits Privacy Coins Like Monero Under New Crypto Rules. The issuance of anonymity-enhancing crypto are banned under the Emirate's new regulations for digital assets.
OpenSea Unveils New Suite of Tools for NFT Creators - DailyCoin. OpenSea has announced a series of new tools to be rolled out on the marketplace for NFT creators. Read more.
Only 31% of Staked Ether May Be Profitable: Binance Research. Around 2 million ETH were staked when prices were in the range of $400 to $600. These stakers are are some of the strongest Ethereum believers, according to Binance Research.
What the U.S. Congress Decides on Crypto Will Ultimately Overstepping their authority | Blockchain News. Jake Chervinsky, the Blockchain Association's chief policy officer, criticized the SEC's enforcement-based regulation and urged Congress to regulate the sector.
France’s top modern art museum to display CryptoPunks, Autoglyphs NFTs. The Centre Pompidou announced plans for a permanent exhibition focusing on NFTs.
Snoop Dogg revealed as co-founder of Web3-powered livestream platform. American rapper Snoop Dogg is set to launch a Web3-based live streaming service named “Shiller,” which will connect creators of nonfungible token projects, artists and brands with their “Enthusiasts.” Shillers can be paid in cryptocurrency in NFTs, which can then be converted to fiat.
Jump Crypto unveils critical vulnerability on Binance’s BNB Chain. Jump Crypto discovered a vulnerability in the Binance BNB Beacon Chain.'''

doc = nlp(article)
for sent in doc.sents:
    print('-' * 60 + '\n' + sent.text)
    doc = nlp(sent.text)
    if not doc.ents: continue
    for ent in doc.ents:
        print(f"  - {ent.label_}: '{ent.text}' (start: {ent.start_char}, end: {ent.end_char})")
