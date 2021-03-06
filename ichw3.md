# 高速缓存存储器简介

## 结构

高速缓存存储器是存在于主存与CPU之间的一级存储器， 由静态存储芯片(SRAM)组成，容量比较小但速度比主存高得多， 接近于CPU的速度。
主要由三大部分组成：

- Cache存储体：存放由主存调入的指令与数据块。
- 地址转换部件：建立目录表以实现主存地址到缓存地址的转换。
- 替换部件：在缓存已满时按一定策略进行数据块替换，并修改地址转换部件。

一个通用的高速缓存存储器中含有S=2<sup>s</sup>个sets；每个set含有E个lines（称为cache line)；每个cache line又包含1位valid bit、t位tag、B=2<sup>b</sup>字节的cache block。

通常我们说的cache line 64位、32位，实际上说的是cache line中cache block是64位或32位。

![cache's structure](https://github.com/zivpei/ichw/blob/master/062318599121326.png
)

假设我们的存储器地址空间的长度为m位，即共有M=2<sup>m</sup>个不同的地址。每个cache line的大小为2<sup>b</sup>字节，故内存中的cache line个数为2<sup>m-b</sup>。将这些cache lines分配到2<sup>s</sup>个sets里，则每个set平均得到2<sup>m-b-s</sup>个cache lines，可想而知应该有2<sup>m-b-s</sup>个tags来标记它们，于是tag的长度t=m-b-s。

## 工作原理

 高速缓存存储器通常由高速存储器、联想存储器、替换逻辑电路和相应的控制线路组成。

高速存储器如前文所述地被划分为行和列的存储单元组。

联想存储器用于地址联想，有与高速存储器相同行数和列数的存储单元。当主存储器某一列某一行存储单元组调入高速存储器同一列某一空着的存储单元组时，与联想存储器对应位置的存储单元就记录调入的存储单元组在主存储器中的行号。

当中央处理器存取主存储器时，硬件首先自动对存取地址的列号字段进行译码，以便将联想存储器该列的全部行号与存取主存储器地址的行号字段进行比较：若有相同的，表明要存取的主存储器单元已在高速存储器中，称为命中，硬件就将存取主存储器的地址映射为高速存储器的地址并执行存取操作；若都不相同，表明该单元不在高速存储器中，称为脱靶，硬件将执行存取主存储器操作并自动将该单元所在的那一主存储器单元组调入高速存储器相同列中空着的存储单元组中，同时将该组在主存储器中的行号存入联想存储器对应位置的单元内。

当出现脱靶而高速存储器对应列中没有空的位置时，便淘汰该列中的某一组以腾出位置存放新调入的组，这称为替换。确定替换的规则叫替换算法，常用的替换算法有:最近最少使用算法（LRU）、先进先出法（FIFO）和随机法（RAND）等。替换逻辑电路就是执行这个功能的。另外，当执行写主存储器操作时，为保持主存储器和高速存储器内容的一致性，对命中和脱靶须分别处理。
