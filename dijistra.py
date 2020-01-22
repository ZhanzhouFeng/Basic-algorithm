from heapq import heappop, heappush

V = [  # 顶点列表
    1, 2, 3, 4, 5, 6]
w = [  # 城市间距离, -1表示无穷大
    [0, 7, 9, -1, -1, 14],
    [7, 0, 10, 15, -1, -1],
    [9, 10, 0, 11, -1, 2],
    [-1, 15, 11, 0, 6, -1],
    [-1, -1, -1, 6, 0, 9],
    [14, -1, 2, -1, 9, 0]]


def Dijkstra(V=V, w=w, start=1, dest=5):
    N = len(V)  # 顶点数
    S = set()
    # 声明没说是堆，但是加入的时候是按照堆得方式加入的
    Q = [(0, V.index(start), str(start))]  # 路径长, 序号, 路径
    v_d = V.index(dest)
    while Q:  # 当Q非空
        d, u, p = heappop(Q)
        if u == v_d:
            print(d, p)
            break  # 可以在找到目的地之后立即终止，也可继续查找完所有最短路径
            # 如果到目的地的距离已经是当前所有距离中最短的，那不可能会有更短的，所以退出
        if u not in S:
            S.add(u)
            v_reached_from_u = [i for i in range(N) if w[u][i] != -1]  # u能到达的顶点
            for v in v_reached_from_u:
                if v not in S:
                    # v是下标，而后面的是顶点号
                    heappush(Q, ((d + w[u][v]), v, ''.join((p, '->', str(V[v])))))  # 到顶点v的某条路径的距离,
            # print(Q)
            # print(S)

Dijkstra()  # 20 1->3->6->5

