import time
import itertools
from ortools.sat.python import cp_model

def parse_grid(grid_str):
    digits = '123456789'
    return {i: digits if grid_str[i] == '.' else grid_str[i] for i in range(81)}

def create_constraints():
    units = []
    for i in range(9):
        units.append([i * 9 + j for j in range(9)])  # rows
        units.append([i + j * 9 for j in range(9)])  # columns
    for i in range(3):
        for j in range(3):
            units.append([9 * (i * 3 + di) + j * 3 + dj for di in range(3) for dj in range(3)])  # 3x3 boxes
    peers = {i: set(itertools.chain(*[u for u in units if i in u])) - {i} for i in range(81)}
    return units, peers

def ac3(values, peers):
    queue = [(x, y) for x in range(81) for y in peers[x] if len(values[x]) == 1]
    while queue:
        x, y = queue.pop(0)
        if len(values[y]) > 1 and values[x] in values[y]:
            values[y] = values[y].replace(values[x], '')
            if len(values[y]) == 0:
                return None
            if len(values[y]) == 1:
                queue.extend((y, p) for p in peers[y])
    return values

def backtracking(values, peers):
    if values is None:
        return None
    if all(len(values[i]) == 1 for i in range(81)):
        return values
    s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
    for d in values[s]:
        new_values = values.copy()
        new_values[s] = d
        new_values = ac3(new_values, peers)
        result = backtracking(new_values, peers)
        if result:
            return result
    return None

def solve_sudoku(grid_str):
    values = parse_grid(grid_str)
    _, peers = create_constraints()
    values = ac3(values, peers)
    return backtracking(values, peers)

def google_or_sudoku_solver(grid_str):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    cells = [[model.NewIntVar(1, 9, f'cell_{i}_{j}') for j in range(9)] for i in range(9)]
    
    # Row, column, and box constraints
    for i in range(9):
        model.AddAllDifferent(cells[i])
        model.AddAllDifferent([cells[j][i] for j in range(9)])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            model.AddAllDifferent([cells[x][y] for x in range(i, i+3) for y in range(j, j+3)])

    # Initial values
    for i, val in enumerate(grid_str):
        if val != '.':
            model.Add(cells[i // 9][i % 9] == int(val))

    status = solver.Solve(model)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        return [[solver.Value(cells[i][j]) for j in range(9)] for i in range(9)]
    return None

def gpt_sudoku_solver(grid_str):
    values = parse_grid(grid_str)
    _, peers = create_constraints()

    def assign(values, s, d):
        values[s] = d
        for p in peers[s]:
            if d in values[p]:
                values[p] = values[p].replace(d, '')
                if len(values[p]) == 0:
                    return None
        return values

    def search(values):
        if values is None:
            return None
        if all(len(values[i]) == 1 for i in range(81)):
            return values
        s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
        for d in values[s]:
            new_values = assign(values.copy(), s, d)
            result = search(new_values)
            if result:
                return result
        return None

    return search(values)

def solve_sudoku_revised(grid_str):
    values = {i: '123456789' if grid_str[i] == '.' else grid_str[i] for i in range(81)}
    units = []
    for i in range(9):
        units.append([i * 9 + j for j in range(9)])  # row
        units.append([i + j * 9 for j in range(9)])  # col
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            units.append([(i + di) * 9 + (j + dj) for di in range(3) for dj in range(3)])
    peers = {i: set().union(*[set(u) for u in units if i in u]) - {i} for i in range(81)}

    def eliminate(values):
        for s in range(81):
            if len(values[s]) == 1:
                d = values[s]
                for p in peers[s]:
                    if d in values[p]:
                        values[p] = values[p].replace(d, '')
                        if len(values[p]) == 0:
                            return None
        return values

    def only_choice(values):
        for unit in units:
            for d in '123456789':
                dplaces = [s for s in unit if d in values[s]]
                if len(dplaces) == 1:
                    if len(values[dplaces[0]]) > 1:
                        values[dplaces[0]] = d
        return values

    def reduce_puzzle(values):
        stalled = False
        while not stalled:
            before = sum(len(values[s]) for s in range(81))
            values = eliminate(values)
            if values is None: return None
            values = only_choice(values)
            after = sum(len(values[s]) for s in range(81))
            stalled = before == after
        return values

    def search(values):
        values = reduce_puzzle(values)
        if values is None:
            return None
        if all(len(values[i]) == 1 for i in range(81)):
            return values
        s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
        for d in values[s]:
            new_values = values.copy()
            new_values[s] = d
            attempt = search(new_values)
            if attempt:
                return attempt
        return None

    return search(values)

def read_sudoku_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write_sudoku_file(filename, solutions):
    with open(filename, 'a') as file:
        file.write('\nSolutions:\n')
        for sol in solutions:
            file.write(sol + '\n')

# Load and solve puzzles
filename = "myFile.txt"
puzzles = read_sudoku_file(filename)
solutions = []

for idx, puzzle in enumerate(puzzles):
    solutions.append(f"\n--- Puzzle {idx + 1} ---")

    try:
        start = time.time()
        result = solve_sudoku(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"Human-Based CSP: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Human-Based CSP: Error - {str(e)}")

    try:
        start = time.time()
        result = google_or_sudoku_solver(puzzle)
        end = time.time()
        flat = ''.join(str(num) for row in result for num in row) if result else "Failed"
        solutions.append(f"Google OR-Tools: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Google OR-Tools: Error - {str(e)}")

    try:
        start = time.time()
        result = gpt_sudoku_solver(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"GPT-Based Solver: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"GPT-Based Solver: Error - {str(e)}")

    try:
        start = time.time()
        result = solve_sudoku_revised(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"Human-Based Revised: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Human-Based Revised: Error - {str(e)}")

write_sudoku_file(filename, solutions)
