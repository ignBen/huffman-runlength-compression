# DNA_Compression
### Info
Implementation of Huffman Code compression and decompression, and Run-length encoding compression and decompression.
Input files should be stored in `DNA_Compression/files` and all files generated by the program (`.bin`and`.txt`) are also outputted here for ease of use.

### Requirements
- Python3
- Pip
	- bitstring
- Terminal

### Usage
Navigate to `DNA_Compression/src` in a terminal window.
#### Huffman
To **compress** a txt file please specify the name of the input file eg.`input.txt`and the desired name of the output file eg.`output.bin`
```
>> python3 Huffman.py ***.txt ***.bin
```
To decompress a bin file please specificy the name of the compressed eg.`compressed.bin` and the desired name of the output file eg.`decompressed`
```
>> python3 Huffman.py ***.bin ***.txt
```
#### Run-Length
The same method follows for Run-Length encoding.
```
>> python3 RunLength.py ***.txt ***.bin
```
```
>> python3 RunLength.py ***.bin ***.txt
```
### Example Data
For convenience a set of sample data has already been put in `DNA_Compression/files`
Other larger data sets such as `fib41.txt` `dblp.xml.00001.txt` `world_leaders.txt` can be found at: `http://pizzachili.dcc.uchile.cl/repcorpus.html`, cannot be uploaded here as file limit for GitHub is 100Mb
| File name                 | Description                                                                           |
|---------------------------|---------------------------------------------------------------------------------------|
| oliver-twist-***.txt      | There are three versions of this file in different languages: English, French, German |
| a-christmas-carol-***.txt | There are three versions of this file in different languages: English, French, German |
| quick-brown-fox.txt       | 'The quick brown fox jumps over the lazy dog'                                         |
| ascii.txt                 | A document containing all ascii characters plus some regular text                     |
| image.txt                 | Used to demonstrate run-length encoding                                               |
 
