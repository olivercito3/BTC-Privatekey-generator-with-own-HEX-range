# BTC-Privatekey-generator-with-own-HEX-range
This python scrypt is generating BTC private keys and is checking them on blockstream API. You can set your own HEX range for Private Keys to be generated. I found this api can handle about 2-3 windows opened at same time more than 3 gets sometimes lagged or blocked by API for few minutes. This btc private keys generator is inspirated by one more here on github but this one has added HEX range function.
If you wish to support this project you can do it by:

BTC:bc1ql0a25wd5lh50f85eddzzms3spdw3stm9p257rv

ETH:0x8dE25D557f64AbA8fC60Aef13963C2eB95CbEC87

LTC:ltc1qkqy4mzj74ee6wa2yx8allh6yslxw0kedtaye5s

OR

DOGE: DLDauwbLg97GPgeh2T4xr1HY8aR7EuBGMG

# Instructions
Only thing you gonna need is <strong>Python</strong>

1.Download it or use git clone in terminal

2.you need to install few dependecies : `pip install base58 hashlib requests ecdsa`

3.go to folder `cd PKgen_HEXrange-main`

4.last step run it `python start.py`

# Own HEX Range
Default HEX range is set for puzzle #64, If you wish to set own range follow this steps: 

1, open folder `PKgen_HEXrange-main`

2, right click on `start.py` and open with some editor: notepad,notepad++,Atom ...

3, scroll down and find line `ran = r.randrange(415051741658795330514, 830103483316929822451+1)`

4, HEX range is in Decimal numbers so to get your own range, use some convertor and convert your HEX number and put it to decimal 

5, after your numbers are converted put them instead of numbers in step 3, <strong>IMPORTANT</strong> in second number on right you need to leave that `+1` how is it and thats all just save the file and continue by <strong> Instructions </strong> upper in text

