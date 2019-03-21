# Toy-Language-Interpreter



## Getting Started

The goal of this project is to interpret a program written in the toy language specified by the final project [assignment statement](Assignment_Statement.txt) in CISC. 3160 - Programming Languages at Brooklyn College, Spring 2019. The interpreter should be able to:
* detect syntax errors
* report uninitialized variables
* perform the assignments if there are no errors
* print out the values of all the variables after all assignments are done

### Prerequisites

Python v3 is required


### Usage

To parse a toy language program file, the script interpreter_tl.py should be executed with the target program as an argument. To parse a program called program1.toy use the following command:

``` python3 interpreter_tl.py program1.toy```

Multiple programs can be passed to the interpreter for consecutive interpretation. To interpret all example files provided in the test_files directory, use the following command:

```python3 interpreter_tl.py test_files/test1.toy test_files/test2.toy test_files/test3.toy test_files/test4.toy test_files/test5.toy```

## Authors

Michael Aleksa

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to Professor Neng-Fa Zhou

