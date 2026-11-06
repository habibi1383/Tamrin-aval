def tower_of_hanoi(n, source, target, auxiliary):
    if n < 1:
        raise ValueError("n must be >= 1")

    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: Move n-1 disks to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move largest disk to target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move n-1 disks to target
    tower_of_hanoi(n - 1, auxiliary, target, source)


# Test with 3 disks
print("Tower of Hanoi solution for 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')