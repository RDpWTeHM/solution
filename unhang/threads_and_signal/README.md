# Use Threads and Signal make unhang program

*keywords: Threads; signal; hang; Python; Ctrl+C; SIGINT*



## Change Log

### `SIGINT_Ctrl+C.py`

##### Usage

```shell
$ chmod +x ./SIGINT_Ctrl+C.py
$ 
$ ./SIGINT_Ctrl+C.py
......
Ctrl+C
.....
$ 
```

##### Test result

![simple_catch_Ctrl+C=SIGINT_demo](res/simple_catch_Ctrl+C=SIGINT_demo.gif)



### `SIGALRM_calculate-game.py`

#### Usage

```shell
$ chmod +x ./SIGALRM_calculate-game.py
$ 
$ ./SIGALRM_calculate-game.py 
[Debug] prog_pid <- os.getpid(): 28202
!!!!!game start!!!!!
Calculate 10 x 4 = ?: 40
Right!

Calculate 8 x 6 = ?: 48
Right!

Calculate 6 x 5 = ?: 
Oooooops game time up!

Final score: 2

$ 
```

#### Test Result

![set-Alarm_SIGALRM](res/set-Alarm_SIGALRM.gif)

