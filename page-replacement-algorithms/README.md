
# Page Replacement Algorithms

## Objective
The objective of this code is to learn and analyze the most common page replacement algorithms presented in the operating systems class who is an obligatory subject in the computer science course at UFRJ.

## Description
The algorithms implemented were: 
- First in, first out (FIFO)
- Optimal (OPT)
- Least recently used (LRU)

The program receives a file with a reference string chosen by you (example 1, 2 or 3) and the number of frames that you want. With this information, the program simulates the paging mechanism, considering that the sequence of required pages by this "fake" process is given by the reference string, and calculates the number of page faults for each algorithm.  

## Using the code
To run this code you'll just need to get Python installed. I used Python 3.x to write the code, so I think that if you use 2.x version, you have to make some changes in the code.<br>
To execute the program, you'll use this command line in your console:
```
python trabalho1SO.py example1.txt 4
```
Where the first file is the program, the second is the file with the reference string (example1.txt, example2.txt or example3.txt) and the last argument is the number of frames that you want to simulate. <br>
If you have a problem with the path, you can run the code using the full path of python and/or the source code on your PC.
Running this example command line, you should get the result:
```
4 quadros, 24 refs: FIFO: 12 PFs, LRU: 11 PFs, OPT: 9 PFs
```
## Built with
- Windows 10 
- IDLE (Python 3.5.2)
- Python language

## Authors
- Tainá Lima
