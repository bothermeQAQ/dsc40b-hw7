def cluster(graph, weights, level):
    visited = set()
    components = []

    if hasattr(graph, "nodes"):
        nodes_iter = graph.nodes
    else:
        nodes_iter = graph.vertices()

    for u in nodes_iter:
        if u not in visited:
            stack = [u]
            visited.add(u)
            comp = set()
            while stack:
                x = stack.pop()
                comp.add(x)
                for y in graph.neighbors(x):
                    if weights(x, y) >= level and y not in visited:
                        visited.add(y)
                        stack.append(y)
            components.append(frozenset(comp))

    return frozenset(components)
