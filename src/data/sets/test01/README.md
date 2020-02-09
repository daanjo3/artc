# Test01: Brill labs dataset (87750 items)

## Data set characteristics
- **Item count:** 88750
- **Image format:** JPG

### Top-level iconclass distribution
```
{
    "0": 40, 
    "1": 22779, 
    "2": 67902, 
    "3": 70054, 
    "4": 145271, 
    "5": 12001, 
    "6": 37069, 
    "7": 15629, 
    "8": 9110, 
    "9": 11513
}
```

## Notes

- Iconclasses can apparently contain a textual description between brackets: `25F23(LION)`.
- Iconclasses can also contain a number between brackets: `44A1(+4)`
- Iconclasses can contain ":" to break the code: `61B:31D14`
- Some of the listed iconclasses are in fact textual descriptions: `Susanna en de ouderlingen`

## Data.json datastructure
```
{
  "IIHIM_1956438510.jpg": [
    "31A235",
    "31A24(+1)",
    "61B(+54)",
    "61B:31A2212(+1)",
    "61B:31D14"
  ],
  "IIHIM_-859728949.jpg": [
    "41D92",
    "25G41"
  ], ...
}
```