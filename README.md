## Directory file summary script
```shell
The task is to write a CLI tool that is able to generate metrics for a given repository. This tool should be executable as a global command and it should iterate through every file given a starting path, checking what language it is written in, and producing output that tells the user how many files are there of each language.
```

## Execution
#### just download the repometrics folder from the github and paste the downloaded folder into your drive and run the file
####                                   OR
#### copy paste the repometrics.py file from the repometrics folder to the desired folder and to calculate the result
```shell
cd D:\repometrics
python repometrics.py
```

#### Expected sample output

```shell
{'results': [{'language': '.sqlite3', 'path': 'D:\\repometrics\\db.sqlite3'},
             {'language': '.js', 'path': 'D:\\repometrics\\jquery.min.js'},
             {'language': '.js',
              'path': 'D:\\repometrics\\jquery.stellar.min.js'},
             {'language': '.js',
              'path': 'D:\\repometrics\\jquery.waypoints.min.js'},
             {'language': '.js', 'path': 'D:\\repometrics\\main.js'},
             {'language': '.js',
              'path': 'D:\\repometrics\\owl.carousel.min.js'},
             {'language': '.js', 'path': 'D:\\repometrics\\popper.min.js'},
             {'language': '.js', 'path': 'D:\\repometrics\\range.js'},
             {'language': '.js', 'path': 'D:\\repometrics\\scrollax.min.js'},
             {'language': '.html', 'path': 'D:\\repometrics\\login.html'},
             {'language': '.py', 'path': 'D:\\repometrics\\manage.py'},
             {'language': '.py', 'path': 'D:\\repometrics\\repometrics.py'},
             {'language': '.md', 'path': 'D:\\repometrics\\ReadMe.md'},
             {'language': '.txt', 'path': 'D:\\repometrics\\sample.txt'}],
 'summary': {'.html': 0.07142857142857142,
             '.js': 0.5714285714285714,
             '.md': 0.07142857142857142,
             '.py': 0.14285714285714285,
             '.sqlite3': 0.07142857142857142,
             '.txt': 0.07142857142857142}}
```
