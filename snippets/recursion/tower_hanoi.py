def tower_hanoi(n, start_pole, dest_pole, temp_pole):
    # easiest case: just one disk
    if n == 1:
        print(f"Move disc {n} from {start_pole} to {dest_pole}")
        return

    tower_hanoi(n - 1, start_pole, temp_pole, dest_pole)
    print(f"Move disk {n} from {start_pole} to {dest_pole}")
    tower_hanoi(n - 1, temp_pole, dest_pole, start_pole)

tower_hanoi(3, "A", "B", "C")
