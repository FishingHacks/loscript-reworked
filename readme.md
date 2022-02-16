# Loscript

A little language i worked on

For running, put the files in $HOME/programming-language/loscript and add an alias for run_shell.py. For fish: `alias lsc "python3 $HOME/programming-language/loscript/run_shell.py"`

Credit for the start: https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD

Move `/lsc.1.gz` to `/usr/share/man/man1/lsc.1.gz` (root permissions required; Read-Only folder) to get `man lsc`
Alternatively you can also use man <your-installation-path>/lsc.1.gz

`shell.py` is the main program, it will give you the interpreter-interface
`/lanugage/lang.lsc` is supposed to be executed silently at first in strict-mode
`test-lang.py` will log errrors and outputs from `/lanugage/lang.lsc` when it doesn't load correctly

Infos:
Comments: Only multiline-comments between `§`
Operations: `+`(addition/appending), `-`(subtraction/removing), `*`(multiplication/duplicating), `/`(Devision), `%`(module), `//`(flooredDivision),k `^` (Power)
`==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (Less than or equal), `>=` (Greater than or equal)
variables beginning with a hashtag can not be changed and act like consts
Built-in functions can't be overwridden
In strictmode functions can't be overwridden
In strictmode you can't change the variable-type
You need to specify all arguments in strict-mode
`"strict"` in your code activates the strict-mode (currently works only in shell-mode)
`"unstrict"` in your code deactivates the strict-mode (currently works only in shell-mode)
`run(filename)` will run a file


Keywords:
`and or if then else end fun var let continue return break for while to step while`


Built-in functions:
`PRINT(str)` prints with a new line
`PRINTF(str)` prints without a new line
`PRINT_RED(str)` returns str
`INPUT()` returns userinput
`INPUT_INT()` returns userinput as a int
`CLEAR()` clears the console
`IS_NUMBER(value)` returns whether or not the given value is a Number
`IS_STRING(value)` returns whether or not the given value is a String
`IS_LIST(value)` returns whether or not the given value is a List
`IS_FUNCTION(value)` returns whether or not the given value is a Function
`APPEND(list, element)` appends the element to the list
`POP(list)` pops the last item off the list and returns it
`LEN(list)` returns the length of a particular list
`WARN(text)` Gives the user a Warning with the specified Text
`ERROR(text)` Gives the user a Error with the specified Text
`NUMBER(value)` Tries to convert the Value to a number
`STRING(value)` Tries to convert the Value to a string
`THROW_ERROR(error)` throws the Error
`REPR(value)` gives back the Representation of a value
`RANDOM()` gives a random number back
`TO_UPPER(string)` gives the Uppercase string back
`TO_LOWER(string)` gives the Lowercase string back
`IS_GRAPH(string)` returns whether or not the character is graphical
`MATH.POW(num1, num2)` Gives num1 to the power of num2 zurück
`MATH.ROUND(number)` Gives the rounded number back
`MATH.FLOOR(number)` Gives the floored number back
`GETOBJECT(name)` Gives the Object corresponding to the name back

`SYSTEM(command)` executes the command
`GETENV(name)` returns the environment variable
`SETENV(name, value)` sets the environment Variable to the value
`DELENV(name)` deletes the environment variable
`EXIT(code)` exits with the specified code
`EXECPY(code)` executes python-code

Aliases:
For every command exists a corresponding lowercase-command like `math.round()` or `printf()`

`prn`->`PRINT`
`throwError` -> `THROW_ERROR`
`rand` -> `RANDOM`
`RAND` -> `RANDOM`
`prnf` -> `PRINTF`
`upper` -> `TO_UPPER`
`lower` -> `TO_LOWER`
`getObj` -> `GETOBJECT`

Stdlib functions:
`MATH_FULL_DIVIDE(num1, num2)` Returns floored and modulo values back, no recommended use

`math.ceil(num1)` Gets the next highest full integer
`math.neg(num)` Negates the number
`math.abs(num)` Gets the absolute number
`isLower(char)` returns whether or not the character is lowercase
`isUpper(char)` returns whether or not the character is uppercase
`isSpace(char)` returns whether or not the character is a whitespace
`typeof(object)` returns the type of the Object

Of couse, for every mentioned above, there is a correspondenting uppercase function

Function defenition:
1-liner:
fun <name>(<...args>) -> <function-call>

multi-liner:
fun <name>(<...args>)
   §logic...§
end