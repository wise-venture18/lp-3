# •	DAA-2: Implement job sequencing with deadlines using a greedy method.

def job_sequencing(jobs):

    # Sort jobs according to profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots
    slots = [None] * max_deadline

    total_profit = 0

    # Schedule jobs
    for job in jobs:
        job_id, deadline, profit = job

        # Find latest available slot
        for j in range(min(deadline, max_deadline) - 1, -1, -1):

            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Display scheduled jobs
    print("\nScheduled Jobs:")

    for i in range(max_deadline):
        if slots[i] is not None:
            print(f"Time Slot {i + 1}: {slots[i]}")

    print("\nTotal Profit:", total_profit)


# Main Program
print("===== Job Sequencing with Deadlines =====")

n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    print(f"\nEnter details for Job {i + 1}:")

    job_id = input("Job ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))

    jobs.append((job_id, deadline, profit))

job_sequencing(jobs)

# --- END -------



#========== SAMPLE INPUT =======================
"""
===== Job Sequencing with Deadlines =====

Enter number of jobs: 5

Enter details for Job 1:
Job ID: J1
Deadline: 2
Profit: 100

Enter details for Job 2:
Job ID: J2
Deadline: 1
Profit: 19

Enter details for Job 3:
Job ID: J3
Deadline: 2
Profit: 27

Enter details for Job 4:
Job ID: J4
Deadline: 1
Profit: 25

Enter details for Job 5:
Job ID: J5
Deadline: 3
Profit: 15

Scheduled Jobs:
Time Slot 1: J3
Time Slot 2: J1
Time Slot 3: J5

Total Profit: 142
"""

#========== VIVA Questions =======================
"""
# DAA-2: Job Sequencing with Deadlines Using Greedy Method

## Viva Questions and Answers

### Basic Questions

Q1. What is Job Sequencing with Deadlines?

Ans: It is a scheduling problem in which jobs are arranged to maximize total profit while satisfying their deadlines.

Q2. What is a Greedy Algorithm?

Ans: A greedy algorithm makes the best possible choice at each step to find an optimal solution.

Q3. What is the main objective of Job Sequencing?

Ans: To maximize total profit by scheduling jobs before their deadlines.

Q4. What are the inputs required for this problem?

Ans: Job ID, Deadline, and Profit.

Q5. What is a deadline?

Ans: A deadline is the maximum time by which a job must be completed.

Q6. What is a time slot?

Ans: A time slot is a unit of time allocated to execute one job.

Q7. Can two jobs be scheduled in the same time slot?

Ans: No. Only one job can be scheduled in one time slot.

### Greedy Algorithm Questions

Q8. Why do we use the Greedy method for this problem?

Ans: Because selecting jobs with higher profits first helps maximize the total profit.

Q9. What is the greedy strategy used in this program?

Ans: Sort jobs in descending order of profit and schedule each job in the latest available slot before its deadline.

Q10. Why do we sort jobs in descending order of profit?

Ans: To consider the most profitable jobs first.

Q11. Why do we schedule a job in the latest available slot?

Ans: To keep earlier slots available for jobs having smaller deadlines.

Q12. What happens if no time slot is available for a job?

Ans: That job is skipped and not included in the schedule.

### Program-Related Questions

Q13. What does `jobs.sort(key=lambda x: x[2], reverse=True)` do?

Ans: It sorts the jobs according to profit in descending order.

Q14. What is a lambda function?

Ans: A lambda function is a small anonymous function in Python.

Q15. What does `max(job[1] for job in jobs)` do?

Ans: It finds the maximum deadline among all jobs.

Q16. Why do we use `slots = [None] * max_deadline`?

Ans: It creates empty time slots based on the maximum deadline.

Q17. What does `None` represent in the slots list?

Ans: It represents an empty time slot.

Q18. Explain `range(min(deadline, max_deadline) - 1, -1, -1)`.

Ans: It searches for an available time slot backwards, starting from the latest valid slot.

Q19. Why do we use `break` after scheduling a job?

Ans: Because each job requires only one time slot. Once scheduled, the loop stops checking other slots.

Q20. What does `total_profit += profit` do?

Ans: It adds the profit of the scheduled job to the total profit.

### Complexity-Related Questions

Q21. What is the time complexity of this program?

Ans: O(n log n + nD), where n is the number of jobs and D is the maximum deadline.

Q22. What is the space complexity of this program?

Ans: O(D), for storing the time slots, excluding the input jobs.

Q23. Which part of the program takes the most time?

Ans: Sorting the jobs and searching for available time slots.

### Advanced Questions

Q24. What happens if two jobs have the same profit?

Ans: Either job can be considered first. The final schedule depends on their deadlines and input order.

Q25. What is the maximum number of jobs that can be scheduled?

Ans: At most `min(n, D)` jobs, assuming each job takes one unit of time.

Q26. What is the difference between Greedy and Dynamic Programming?

Ans: Greedy makes the best local choice at each step, whereas Dynamic Programming solves and stores results of smaller subproblems.

Q27. Is every job scheduled in this algorithm?

Ans: No. Only jobs that can fit into an available slot before their deadlines are scheduled.

Q28. Can we improve the time complexity?

Ans: Yes. A Disjoint Set Union (DSU) data structure can be used to find available time slots more efficiently.
"""
