def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mova o disco 1 da torre {source} para a torre {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Mova o disco {n} da torre {source} para a torre {target}")
    hanoi(n - 1, auxiliary, target, source)

def torre_de_hanoi(num_disks, start_tower, end_tower):
    towers = {
        'A': list(range(num_disks, 0, -1)),  # Start with all disks on start_tower
        'B': [],
        'C': []
    }

    def mover_disco(source, target):
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Mova o disco {disk} da torre {source} para a torre {target}")

    def hanoi(n, source, target, auxiliary):
        if n == 1:
            mover_disco(source, target)
            return
        hanoi(n - 1, source, auxiliary, target)
        mover_disco(source, target)
        hanoi(n - 1, auxiliary, target, source)

    print("Estado inicial das torres:")

    hanoi(num_disks, start_tower, end_tower, {'A', 'B', 'C'}.difference({start_tower, end_tower}).pop())

torre_de_hanoi(5, 'A', 'C')
