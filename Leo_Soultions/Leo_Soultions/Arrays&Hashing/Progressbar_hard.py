""" 87. Console-based Python Progress Bar - Hard
In a console application, you need to display a progress bar to visualize the completion status of an ongoing process. The progress bar should be rendered in a single line.

The task consists of two parts:

Part 1

You are given a total number of tasks n, and a list of task completion times in seconds tasks[] where tasks[i] denotes the completion time of i-th task.

Write a function render_progress_bar(n: int, tasks: List[int]) -> str that takes the number of tasks and the task completion times as input, and returns the final state of the progress bar as a string. The progress bar should update every second.

The progress bar must consist of 50 characters:

The '#' character represents a completed portion of the tasks.
The '-' character represents an uncompleted portion of the tasks.
Each '#' character represents 2% of the total tasks. Thus, every time tasks corresponding to 2% or more of the total are completed, a '#' should replace a '-' in the progress bar. The progress bar should be updated from left to right.

For example, if n = 100 and tasks = [2,2,2,2,2,...], your function should return '##################################################' as each task corresponds to 2% of the total, and all tasks are completed.

Part 2

Next, upgrade your function to animate_progress_bar(n: int, tasks: List[int]) -> None that animates the progress bar in console. It should print the progress bar to the console and update it every second as the tasks are completed.

For example, if n = 5 and tasks = [2,2,2,2,2], the function would print:

arduino
Copy code
'#---------' (after 1 sec)
'##--------' (after 2 sec)
'###-------' (after 3 sec)
'####------' (after 4 sec)
'#####-----' (after 5 sec)
Constraints:

1 <= n <= 500
1 <= tasks[i] <= 5, where 0 <= i < n
Note:

Consider the completion of tasks synchronous, i.e., one task starts after the completion of the previous task. The order of tasks is the same as in the input list.

This problem will test your ability to work with real-time updates, console outputs, and proportional representations.

Here are steps to think through this problem:

Understand the size and nature of the tasks.
Calculate the total number of tasks and the percentage of completion each task contributes to.
Use a loop to iterate through the task completion times.
In each iteration, update the progress bar according to the completion status of tasks.
In the case of the animated progress bar, use a sleep function to pause execution of the script for the duration of each task.
Print the updated progress bar after each task is completed.
Continue until all tasks are completed and the progress bar is fully filled.
"""