# File manipulationa and searching

## TODO 
- Cleaning a file: splitting into chuncks, replacing characters
- Searching within a file (see lecture)
- Counting numbers of word in file

<!-- 
## analisi del testo e ricerca
# - costruzione di indici per evitare di dover ricontare le parole
# - eliminazione delle parole piÃ¹ comuni (con frequenze molto/troppo alte, con stopwords)
# - estrazione delle parole (rimpiazzando i nonalpha con spazi)
# - ricerca di file che parlano di piÃ¹ di certe parole
# - importanza delle parole nei file    = tf_i * idf
#    - tf_i  = # presenze / # parole del file                           # frequenza nel file iesimo
#    - idf   = log( # di file / # di file che contengono la parola )    # inverso della frequenza nei documenti
 -->

 ## Reading files

Files can be opened in Python using the function ```open```, then specifying mode (i.e. reading, writing) and encoding. 

The expression ```with open(file) as f``` **automatically closes the file** after use (otherwise, the file must be closed explicitly by using the ```close()``` method)

 ```python
 with open("file.txt", encoding="utf-8") as f:
     f = f.readlines()
```

### JSON
JSON files contains data. They can be loaded into Python, then a common workflow is to convert them into dictionaries for additional manipulation (deserialization).

First thing, the library ```json``` must be imported

```python
import json

# Open JSON data file into a list of dictionaries
with open('data.json') as data:
    d = json.load(data)

```

Other useful methods are ```json.loads()```, which parse a  JSON string into a dictionary.

## Writing files

Basic writing of files can be done in a similar way as how you read files.
**NOTE** The method ```writelines()``` actually writes everything on a single line! **Make sure to add new lines and spacing as required!

```python

lines = ["Volli volli,",  "fortissimamente", "volli"]

with open("output.txt", "w") as out:
    out.writelines(s + '\n' for s in lines)

```
### Writing JSON

Writing to a JSON file is very simial 


```python
import json

data = [
    {"name": "Alice", "age": 31},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 38 },
]

with open("output.json", "w") as out:
    json.dump(data, out)
```
### Writing CSV

CSV is another common data format. 

The following snippet illustrates how to write data stored in **list of lists** as CSV

```python

# Import CSV library necessary
import csv

# Add Header
header = ["name", "age"]
# Add data
data = [
        ["Alice", 31],
        ["Bob", 24],
        ["Charlie", 30]
        ]

with open("data.csv", "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(data)
```

The following snippet shows how to write data stored in **dictionary** format in CSV.

```python
import csv

header = ['name', 'age']
data = [
    {"name": "Alice", "age": 31},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 38 },
]

with open("data.csv", "w", encoding="utf-8", newline="") as out:
    writer = csv.DictWriter(out, fieldnames = header)
    writer.writeheader()
    writer.writerows(data)


```

## Parsing and cleaning input from file

**Removing whitespace**


```python
def remove_space(file):
    """Remove all whitespace from file."""
    cleaned = []
    
    with open(file, 'r', encoding="utf=8") as f:
        for line in f:
            if not line.isspace():
                cleaned.append(line.split())
        return cleaned

            
f = remove_space("file.txt")
print(f"remove_space: {f}\n") # File as a list of lists of strings, each line a new 


```
**Keeping only numbers from file**
```python
def keep_numbers(file):
    """Get all ints in the file text."""
    cleaned = []    
    with open(file, "r", encoding="utf-8") as f:
        f = f.readlines()
        for line in f:
            filtered = list(map(int, filter(lambda x: x.isnumeric(), line)))
            if len(filtered) > 0:
                strings = "".join(list(map(str, filtered)))
                cleaned.append(int(strings))                
    return cleaned
        
f = keep_numbers("file.txt")
print(f'keep_numbers: {f}\n') # File returns as list of ints, no whitepsace
```

**Keeping only alphabetic characters**


```python
def keep_alphanumeric(file):
    """Get all string in text file."""
    cleaned = []
    with open(file) as f:
        for line in f:
            line = line.split()
            if not len(line) == 0:
                line = list(line[0])
                line = list(map(str, filter(lambda x: x.isalpha(), line)))
                line = "".join(line)
                if not line == "":
                    cleaned.append("".join(line))
    return cleaned
                

f = keep_alphanumeric("file.txt")
print(f"keep_alphanumeric: {f}\n")
```

**Removing special characters**

```python
TODO
```


#### Replacing characters

**Replace single characters with ```replace```**

```python
TODO
``` 

**Replacing multiple characters with ```maketrans```**

```python
TODO
``` 


### Snippets from previous psets (for reference)

```python 
'''
Code from HW4
'''
def read_poem(inputfilename):
    '''
    Read a poem, remove empty lines, remove any special characters except hyphens and apostrophes

    '''
    poem = []
    with open(inputfilename, encoding="utf8") as f:
        for line in f:
            if not line.isspace(): 
                filter_line = [word if word.isalpha() else ' ' for word in line]
                alpha_line = ''.join(filter_line)
                poem.append(alpha_line.split())
    return poem
```

```python
'''
Code from HW6
'''
def clean_file(inputfilename):
    """
    Read file, split it at spaces and commas, convert text in int, and group inputs in tuples of len 5
    """
    with open(inputfilename) as f:
        lst = []
        for line in f:
            line = "".join(line.split())
            line = line.split(",")
            filtered = list(map(int, filter(lambda x: x.isnumeric(), line))) 
            split_filtered = [tuple(filtered[i:i+5]) for i in range(0, len(filtered), 5)]
            lst.append(split_filtered)
        return lst

```