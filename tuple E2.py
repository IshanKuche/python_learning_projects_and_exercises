def main():
    grid = {
        (0,0) : "start",
        (1,2) : "wall",
        (2,3) : "treasure",
        (3,3) : "end"
    }
    x,y = get_coordinates()
    result = search_coordinate(x,y,grid)
    conclusion = get_response(result,grid)
    print(conclusion)
    
def get_response(result):
    if result == None:
        return "Empty"
    else:
        return result


def get_coordinates():
    x_coordinate = get_user_prompt("Enter X coordinates: ")
    y_coordinate = get_user_prompt("Enter Y coordinates: ")
    return x_coordinate,y_coordinate


def get_user_prompt(prompt):
    while True:
        value = int(input(prompt))
        if value:
            return value
        elif value == 0:
            return value
        else:
            continue

def search_coordinate(x,y,grid):
    hunt = grid.get((x,y),None)
    return hunt

if __name__ == "__main__":
    main()
