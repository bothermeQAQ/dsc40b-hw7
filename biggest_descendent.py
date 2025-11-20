def biggest_descendent(graph, root, value):
    biggest = {}

    def dfs(u):
        m = value[u]
        for v in graph.neighbors(u):
            if v not in biggest:
                child_big = dfs(v)
            else:
                child_big = biggest[v]
            if child_big > m:
                m = child_big
        biggest[u] = m
        return m

    dfs(root)
    return biggest