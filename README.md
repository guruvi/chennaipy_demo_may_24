# ChennaiPy Demo May 24
This repository contains artifacts that I presented to Chennai Py on May 24, 2025.

## Slides link
https://docs.google.com/presentation/d/1K5AF9vRN46974N2Aa_Ud702Gki7w3qoGjyVyx9WuXto/edit#slide=id.g35535e1fc0a_0_37

## Pre requisites:
1. Install poetry
2. Python 3.12.10
3. poetry install
4. poetry run jupyter notebook (For threadpool executor and mysterious thread pool file)
5. poetry run python 3_asyncio_example.py
6. poetry run python 4_process_pool_executor.py


## SUB INTERPRETER CODE:
### Sub interpreter reference:
https://github.com/RishiRaj22/PythonParallelism

1. Add benchmarking directory from this folder is treated as a Python source directory. 
    export PYTHONPATH="$PYTHONPATH:`pwd`/sub_interpreter_demo/benchmarking"
2. Ensure that setuptools is available locally. `poetry run python3 sub_interpreter_demo/setup.py install`
3. Run demo code: `poetry run python sub_interpreter_demo/demo.py`

## Thread free execution:
With a python version running 3.13.3t shell execute the below code from the files 5_free_threaded_mode.py

