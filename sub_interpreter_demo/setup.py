import os
from setuptools import setup, Extension

def main():
    setup(name="subinterpreter_parallelism",
          language="c++",
          version="1.0.0",
          description="Description",
          author="Rishi",
          author_email="contact@rishiraj.me",
          ext_modules=[Extension("subinterpreter_parallelism", ["sub_interpreter_demo/subinterpreter_parallelism.cpp"], language='c++')])

if __name__ == "__main__":
    os.environ["CC"] = "g++"
    main()
