# `Compiler Interpreter`

 - ### Using MINGW( it's also g++ ) for Windows
 - ### G++ for Linux or Mac.

 ### `Specific version`
 ```
 g++.exe (MinGW.org GCC-6.3.0-1) 6.3.0
 ```

## `Using Time`

 If you want to see the execution time.

 - ### `Widnows`

 ```bash
 (Measure-Command { g++ program.cpp | Out-Default }).ToString()
 (Measure-Command { ./a.exe | Out-Default }).ToString()
 ```

 - ### `Linux/Mac`

```bash
time g++ program.cpp
time ./a.out
```

 [For More info](https://desiprogrammer.com/blogs/execution-time-of-command-on-windows-command-line)