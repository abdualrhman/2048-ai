## Get started

Navigate to the project forlder and run the program by typing:

```
python3 boardManeger.py
```

## Adjusting the expectimax algorithm depth

The default depth of the algorithm is 5 if there are 5 or more empty cells, otherwise 6.
The depth can be adjusted in the `aotumate()` frunction in `boardManeger.py`

## Adjusting the heurestic function

The heurestic function is implemetented using matrix wieght, and it prioritize moves that merges cells upwards and towards the corner. It can be adjusted in the `getScore()` function in `ai.py`.
