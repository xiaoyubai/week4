import turtle


def searchFrom(maze, startRow, startColumn):

    maze.updatePosition(startRow, startColumn)

    # Check for base cases:
    # 1. we have run into an obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE:
        return False

    # 2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED:
        return False

    # 3. Success, an outside edge not occupied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)

    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

class Maze:

    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = -rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'tan')
        self.t.color('black', 'blue')

    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))

    def dropBreadcrumb(self, color):
        self.t.dot(color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color  ='red'

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or row == self.rowsInMaze - 1 or
                col == 0 or col == self.columnsInMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]

def main():
    PART_OF_PATH = '0'
    TRIED = '.'
    OBSTACLE = '+'
    DEAD_END = '-'

    myMaze = Maze('maze2.txt')
    myMaze.drawMaze()
    myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

    searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

if __name__ == '__main__':
    main()
