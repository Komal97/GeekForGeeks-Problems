'''
https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1},
{1, 2, 2, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 2, 2, 0},
{1, 1, 1, 1, 1, 2, 1, 1},
{1, 1, 1, 1, 1, 2, 2, 1},
 };

 x=4, y=4, color=3 

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1}, 
{1, 3, 3, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 3, 3, 0},
{1, 1, 1, 1, 1, 3, 1, 1},
{1, 1, 1, 1, 1, 3, 3, 1}, };
Input:
3
3 4
0 1 1 0 1 1 1 1 0 1 2 3
0 1 5
2 2
1 1 1 1
0 1 8
4 4 
1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4
0 2 9

Output:
0 5 5 0 5 5 5 5 0 5 2 3
8 8 8 8
1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4
'''


# similar to rat in maze
# just change specific pixel value to another given(k)
def flood_fill(mat, pix, x, y, k, n, m):
    if x < 0 or y < 0 or x == n or y == m or mat[x][y] != pix:
        return
    
    mat[x][y] = k
    flood_fill(mat, pix, x-1, y, k, n, m)
    flood_fill(mat, pix, x, y-1, k, n, m)
    flood_fill(mat, pix, x+1, y, k, n, m)
    flood_fill(mat, pix, x, y+1, k, n, m)
    
if __name__ == '__main__':
    t = int(input())
    while t:
        n, m = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        x, y, k = list(map(int, input().split()))
        
        a = 0
        mat = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[a]
                a += 1
            
        pix = mat[x][y]
        flood_fill(mat, pix, x, y, k, n, m)
        mat = [j for i in mat for j in i]
        print(*mat, sep = ' ')
        t -= 1

