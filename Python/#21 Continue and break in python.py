items = ["eggs", "bananas", "maggie", "stale apples", "bread", "curd"]
Brother_items = []
sister_items = []

for item in items:
    if item != "stale apples":
        print(f"{item} Added to cart")
        Brother_items.append(item)
    else:
        continue    # Continue skips that iteration of the loop and jumps to the next loop.

print(Brother_items)

# Use the debugger to see the continue in action

for item in items:
    if item == "eggs":
        print("No eggs please")
        break       # This completely breaks the loop if the condition is met
    else :
        print(f"{item} Added to cart")
        sister_items.append(item)

print(sister_items)

