# Overview

Use this tool to find a sequence of bytes in a binary file. 

```
$ python3 find_bytes.py -i test/input -r "\x54\xbd\x53\x85\x97\x7c"

[00000360] 57bb 2f1b 5a15 5c8c 3e14 d42c a0a6 714d | ..4...i}"..j{w7.
[00000370] f0b5 34a9 bced 697d 22d8 af6a 7b77 37d7 | ..o..}..j.T.S.. 
[00000380] eb0f 6f89 19a6 7dfb e86a 0154 bd53 8597 | |..nR..q...5@. 
[00000390] 7cab 976e 521c f2d6 710b 1ccf e535 40fe | .Dh...*..NAO.>. 
[000003a0] b744 6893 dfdd 2a01 884e 1641 4f12 3ea2 | ......9....r... 
[000003b0] fb9d 82d9 c6fd 39e5 b8d6 9272 d8de f718 
```

# Known Issues
- Python 2 isn't supported
- Reads entire file into memory for processing
