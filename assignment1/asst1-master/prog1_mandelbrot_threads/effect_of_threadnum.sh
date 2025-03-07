#!/bin/bash

# 输出结果文件
LOG_FILE="mandelbrot_results.txt"

# 清空日志文件
> $LOG_FILE

# 循环从 1 到 99 的线程数运行 ./mandelbrot
for ((t=1; t<=99; t++)); do
    echo "Running with $t threads..."

    # 运行程序并抓取输出结果
    OUTPUT=$(./mandelbrot -t $t)

    # 将线程数和运行结果保存到日志文件
    echo "Threads: $t" >> $LOG_FILE
    echo "$OUTPUT" >> $LOG_FILE
    echo "------------------------------------" >> $LOG_FILE
done

echo "All runs completed. Results saved to $LOG_FILE."