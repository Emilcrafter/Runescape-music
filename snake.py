"""The first line of input contains a single integer 𝑛
n
 (1≤𝑛≤100
1
≤
n
≤
100
) representing the number of polygons to be painted. Following this are 𝑛
n
 lines each describing a painted polygon. Each polygon description starts with an integer 𝑚
m
 (3≤𝑚≤20
3
≤
m
≤
20
) indicating the number of sides in the polygon, followed by 𝑚
m
 pairs of integers 𝑥
x
 𝑦
y
 (0≤𝑥,𝑦≤1000)
0
≤
x
,
y
≤
1
000
)
 specifying the coordinates of the vertices of the polygon in consecutive order. Polygons may be concave but no polygon will cross itself. No point on the canvas will be touched by more than two polygon border segments.

 Output
Display both the total amount of paint used and the amount of canvas covered. Your answers must have a relative or absolute error of at most 10−6
10
−
6
.

sample input :
3
8 7 10 7 17 10 20 17 20 20 17 20 10 17 7 10 7
4 0 0 0 8 8 8 8 0
4 3 3 3 13 13 13 13 3

sample output:
315.00000000 258.50000000

"""


def polygon_area(x, y):
    area = 0
    for i in range(len(x) - 1):
        area += x[i] * y[i + 1] - x[i + 1] * y[i]
    return area / 2


def main():
    n = int(input())
    total_area = 0
    total_paint = 0
    for i in range(n):
        m = int(input())
        x = []
        y = []
        for j in range(m):
            x_y = input().split()
            x.append(int(x_y[0]))
            y.append(int(x_y[1]))
        total_area += polygon_area(x, y)
        total_paint += polygon_area(x, y) / (max(x) - min(x)) * (max(y) - min(y))
    print(total_paint, total_area)


if __name__ == '__main__':
    main()