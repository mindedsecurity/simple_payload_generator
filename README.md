# Simple Payload Generator

A "simple" tool/library that can be used to generate a set of binary payloads according to a template.
The payload can be used for fuzzing or unit testing.

## The Template Engine

This library allows to create custom multiple payloads using a templating format.

In particular it's possible to use the following special sequences:

 * RANGE:    *{R[min,max,pack_format]}* : Creates a sequence of numbers from min to max and encodes it using the struct.pack format ('B','>H' etc). It will create (max-min) payloads (for pack format see https://docs.python.org/3/library/struct.html). 
 * RANDOM:   *{r{bytesequence_length, ar_len}}*: Creates an array of 'ar_len' length where each element is a randome sequence of bytes of 'bytesequence_length' length
 * ARRAY:    *{[n1, n2, n3 ...]}*: Adds to the payload  the numbers and will create a set of payload according to the length of the array. 
 * FROM FILE: *{@/path/to/file}*: using @ char the sequence will be taken from a file.
 * CONSTANT:  *00-FF*: will create a single byte. 

See the examples in the next paragraphs.

Feel free to ask for new features! PRs are absoultely welcome :) 

## From Bash

When directly called from command line, it will output each payload in \xHH hex format, with each payload separated by a newline.

```
$ python3 payload_generator.py '0001{[0,3]}'
\x00\x01\x00
\x00\x01\x03
```

```
$ python3 payload_generator.py '0001{R[0,3,">H"]}FF{r[3,2]}00'
\x00\x01\x00\x00\xff\xf8\x27\xc9\x00
\x00\x01\x00\x01\xff\xf8\x27\xc9\x00
\x00\x01\x00\x02\xff\xf8\x27\xc9\x00
\x00\x01\x00\x03\xff\xf8\x27\xc9\x00
\x00\x01\x00\x00\xff\x72\x2c\xcf\x00
\x00\x01\x00\x01\xff\x72\x2c\xcf\x00
\x00\x01\x00\x02\xff\x72\x2c\xcf\x00
\x00\x01\x00\x03\xff\x72\x2c\xcf\x00
```

Another example:

```
$ python3 payload_generator.py  '{[0,1]}0A{R[0,1,"B"]}FF{R[1,2,">H"]}0E{[0,4]}DD'
\x00\x0a\x00\xff\x00\x01\x0e\x00\xdd
\x01\x0a\x00\xff\x00\x01\x0e\x00\xdd
\x00\x0a\x01\xff\x00\x01\x0e\x00\xdd
\x01\x0a\x01\xff\x00\x01\x0e\x00\xdd
\x00\x0a\x00\xff\x00\x02\x0e\x00\xdd
\x01\x0a\x00\xff\x00\x02\x0e\x00\xdd
\x00\x0a\x01\xff\x00\x02\x0e\x00\xdd
\x01\x0a\x01\xff\x00\x02\x0e\x00\xdd
\x00\x0a\x00\xff\x00\x01\x0e\x04\xdd
\x01\x0a\x00\xff\x00\x01\x0e\x04\xdd
\x00\x0a\x01\xff\x00\x01\x0e\x04\xdd
\x01\x0a\x01\xff\x00\x01\x0e\x04\xdd
\x00\x0a\x00\xff\x00\x02\x0e\x04\xdd
\x01\x0a\x00\xff\x00\x02\x0e\x04\xdd
\x00\x0a\x01\xff\x00\x02\x0e\x04\xdd
\x01\x0a\x01\xff\x00\x02\x0e\x04\xdd
```


A more advanced use from the command line is the following Bash script which loops over each payload and converts it to its binary version:

```
for i in `python3 ./payload_generator.py '{R[1,11,"B"]}0a65'` ; do 
echo -ne "$i" |xxd ;
done
```

will output:

```
00000000: 010a 65                                  ..e
00000000: 020a 65                                  ..e
00000000: 030a 65                                  ..e
00000000: 040a 65                                  ..e
00000000: 050a 65                                  ..e
00000000: 060a 65                                  ..e
00000000: 070a 65                                  ..e
00000000: 080a 65                                  ..e
00000000: 090a 65                                  ..e
00000000: 0a0a 65                                  ..e
00000000: 0b0a 65                                  ..e

```

## As a Library

Here's an example to use it as a python library:

```
from payload_generator import PayLoadGenerator

template = '{[0,6]}0A{R[0,1,"B"]}FF{R[1,2,">H"]}0E{[0,4]}DD'
payloads = Payload_Generator(template)

for pl in payloads:
    print(pl)

```

See the Examples folder.

# WARNING

To make it more powerful, the library uses the eval python function. This means that the template it self should NOT be left in control by untrusted parties.
You have been warned :D


# Contribs

Feel free to ask for new features! PRs are absoultely welcome :) 

# Social

Do you want to tag the project? Use #SPG 