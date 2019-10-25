#!/usr/bin/env python3
from random import random

def canMove(maze, snake, f, x, y):
    return snake['f'] != f and maze[snake['y']+y][snake['x']+x] != '#'

def replaceChar(string, i, char):
    s = ''
    for j in range(len(string)):
        if j != i:
            s += string[j]
        else:
            s += char
    return s

def _fc(maze, x, y):
    if maze[y][x] != '#':
        return 1
    else:
        return 0

def countFaces(m, x, y):
    return _fc(m, x+1, y) + _fc(m, x-1, y) + _fc(m, x, y+1) + _fc(m, x, y-1)

def main():
    f = open('maze', 'r')
    maze = f.read().split('\n')
    f.close()
    snake = {'x': 0, 'y': 0, 'f': 'l'}
    nodes = []
    for l in range(len(maze)):
        for c in range(len(maze[l])):
            if maze[l][c] == 'S':
                snake['x'] = c
                snake['y'] = l
    nodes.append(snake.copy())
    print('Starting snake at x: {}, y: {}'.format(snake['x'], snake['y']))
    while True:
        if maze[snake['y']][snake['x']] == 'Z':
            break
        elif canMove(maze, snake, 'l', 1, 0) or canMove(maze, snake, 'd', 0, -1) or canMove(maze, snake, 'r', -1, 0) or canMove(maze, snake, 'u', 0, 1):
            if canMove(maze, snake, 'l', 1, 0) and random() >= 0.5:
                snake['x'] += 1
                snake['f'] = 'r'
                nodes.append(snake.copy())
            elif canMove(maze, snake, 'd', 0, -1) and random() >= 0.5:
                snake['y'] -= 1
                snake['f'] = 'u'
                nodes.append(snake.copy())
            elif canMove(maze, snake, 'r', -1, 0) and random() >= 0.5:
                snake['x'] -= 1
                snake['f'] = 'l'
                nodes.append(snake.copy())
            elif canMove(maze, snake, 'u', 0, 1) and random() >= 0.5:
                snake['y'] += 1
                snake['f'] = 'd'
                nodes.append(snake.copy())
        else:
            for i in reversed(range(len(nodes))):
                if countFaces(maze, nodes[i]['x'], nodes[i]['y']) > 1:
                    maze[nodes[i+1]['y']] = replaceChar(maze[nodes[i+1]['y']], nodes[i+1]['x'], '#')
                    snake = nodes[i].copy()
                    nodes.append(snake.copy())
                    break
        print(snake)
        #for m in maze:
        #    print(m)
        #input()

if __name__ == "__main__":
    main()
