# [Blum '81] Coin Flipping by Telephone

This is the Python implementation of the [Blum coin-flipping protocol.](https://www.cs.cmu.edu/~mblum/research/pdf/coin/)

### Sample run

```
pip3 install -r requirements.txt
```

**Bob**:
```
$ python3 bob.py
N = 756490599664322449213833011934085934891729476169
x2 ? 40509115015847360040670018286719210126028088623
j_guess = -1
x ? 90806192710269355608557082872437065203797177274
Outcome = Tails
```

**Alice**:
```
$ python3 alice.py
N ? 756490599664322449213833011934085934891729476169
x2 = 40509115015847360040670018286719210126028088623
j_guess ? -1
x = 90806192710269355608557082872437065203797177274
Outcome = Tails
```

## Let's flip some coins!

My coin-flipping number is 1001566002234152341231810327395747847813363152601. It's publication date is Feb 21, 2022. 

To proceed with the protocol, you are welcome to open Issue here or tweet me at @atamyrat.

Bonus points if you can flip all coins heads up.

