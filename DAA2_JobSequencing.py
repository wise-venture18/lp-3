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
