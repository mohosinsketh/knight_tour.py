import random

# Knight moves (8 directions)
moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def to_index(x, y):
    # Convert coordinates (x,y) to 1–25 numbering
    return y * 5 + x + 1

# Recursive backtracking to find tours
def knight_tour(x, y, visited):
    if len(visited) == 25:
        return [visited[:]]
    tours = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (nx, ny) not in visited:
            tours.extend(knight_tour(nx, ny, visited + [(nx, ny)]))
            if len(tours) >= 100:
                return tours
    return tours

print("⏳ Generating knight tours...")

# Start from top-left corner (0,0)
tours = knight_tour(0, 0, [(0, 0)])

print(f"✅ Found {len(tours)} tours")

# Format tours into simple number lists
formatted_tours = [", ".join(str(to_index(x, y)) for x, y in t) for t in tours[:100]]

# Save to text file
with open("knight_tour_5x5_100.txt", "w") as f:
    f.write("\n".join(formatted_tours))

print("📄 Saved as knight_tour_5x5_100.txt")
