#!/usr/bin/env python3

def main():
    f = open('maze', 'r')
    maze = f.read().split('\n')
    f.close()
    snake = {'x': 0, 'y': 0, 'facing': 'l'}
    nodes = []
    for l in range(0, len(maze)):
        for c in range(0, len(maze[l])):
            if maze[l][c] == 'S':
                snake['x'] = c
                snake['y'] = l
    nodes.append({'x': snake['x'], 'y': snake['y']})
    print('Starting snake at x: {}, y: {}'.format(snake['x'], snake['y']))
    while True:
        if maze[snake['y']][snake['x']] == 'Z':
            break
        elif snake['facing'] != 'l' and maze[snake['y']][snake['x']+1] == ' ':
            snake['x'] += 1
            snake['facing'] = 'r'
            nodes.append({'x': snake['x'], 'y': snake['y']})
        elif snake['facing'] != 'd' and maze[snake['y']-1][snake['x']] == ' ':
            snake['y'] -= 1
            snake['facing'] = 'u'
            nodes.append({'x': snake['x'], 'y': snake['y']})
        elif snake['facing'] != 'r' and maze[snake['y']][snake['x']-1] == ' ':
            snake['x'] -= 1
            snake['facing'] = 'l'
            nodes.append({'x': snake['x'], 'y': snake['y']})
        elif snake['facing'] != 'u' and maze[snake['y']+1][snake['x']] == ' ':
            snake['y'] += 1
            snake['facing'] = 'd'
            nodes.append({'x': snake['x'], 'y': snake['y']})
        else:
            break #go back to the last node with 2 possible ways, if unchecked
        print(snake)

if __name__ == "__main__":
    main()
