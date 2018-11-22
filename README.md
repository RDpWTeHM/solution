# solution
需求 - solution 合集



[TOC]



## running_wait-time

考虑一种需求，client 向 server 发送一个请求，server 因为某种原因没有回复，或者回复失败。client 接受失败后等待一段时间；第二次再次请求，仍然失败，此时你想要根据连续失败次数延长等待时间；在每一次成功之后确定等待的时间不变（比如为 0）。

有几种方案可以实现这种需要，根据 python 的**闭包**特性，编写一个 function 而非编写 class 就可以实现这个需求。[^1]

详细见 *running_wait-time/* 目录。



------



## Reference

[^1]: *Fluent Python* （流畅的 Python）&7.6

