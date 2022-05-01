Python Microservices and AWS Codebuild Video tutorial https://youtu.be/YB-_FsssK8E


`black` keeps python code up to a standard format.

`fire` My preferred command line tool 
`click` Command line tool

`pylint` disable extra verbose test because I only care about warning and error messages. 

`pytest` Give me some verbose output and run test code script for my coverage.

`textblob` simple nlp processing 

Run `black` to test code format 

Add python libraries 

```shell
make install 

python -m textblob.download_corpora
```

```sh
#format code
black *.py mylib/*.py
All done! ✨ 🍰 ✨
6 files left unchanged.
```

Run `lint` to test for bad code 

```sh 
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

`./cli-fire.py --help` To get command help 

Run `./cli-fire.py wiki "terry gilliam"`
Terrence Vance Gilliam (; born 22 November 1940) is an American-born British film director, screenwriter, animator, actor, comedian and former member of the Monty Python comedy troupe.

Test `./cli-fire.py --search_wiki "terry gilliam"`
Terry Gilliam
Terry Gilliam filmography
Brazil (1985 film)
Monty Python

Run `pytest` to test coverage

```shell
Name                Stmts   Miss  Cover
---------------------------------------
mylib/__init__.py       0      0   100%
mylib/logic.py         12      5    58%
---------------------------------------
TOTAL                  12      5    58%


```


Fastapi 

Run `python main.py` and navigate to host provided from `uvicorn`. This URL should be `http:0.0.0.0:8081`

Textblob for nlp processing 

Docker 

```shell
make build

docker image ls ## Find image id used in next step 

make run
```