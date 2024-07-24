# Simple Element Builder

## Overview

The Simple Element Builder is a Python-based project designed to automate the creation of geometric elements within cadwork 3d. 
It utilizes a structured approach to read geometry and attribute data, construct elements based on this data, and assign attributes to these elements dynamically.


[![Python Tests](https://github.com/cwapi3d/simpleElementBuilder/actions/workflows/mockTest.yml/badge.svg)](https://github.com/cwapi3d/simpleElementBuilder/actions/workflows/mockTest.yml)

## Requirements

- Python 3.10 or higher
- cadwork 3d
- CSV files containing geometry and attribute data

```csv
"id","element_type","width","height","length"
1, 0,100,240,5000
2, 1,1250,15,2500
3, 0,300,240,5000
```

```csv	
"id","name","color","user1"
1,"beam1",5,"factory"
2,"plate1",3,"factoryXY"
3,"beam3",5,"factory"
```

## Installation

Clone the repository to your local machine into the `userprofil_30\3d\API.x64\` directory:
    
 ```bash
 git clone https://github.com/cwapi3d/simpleElementBuilder.git
 ```

## Run from command line

Navigate to `cadwork.dir` and run the following command:

```bash
ci_start.exe path\to\your\testFile.3d /PLUGIN=simpleElementBuilder
```
