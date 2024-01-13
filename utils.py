import plotly.graph_objects as go
import potpourri3d as pp3d


def read_mesh(datafile):
    points = []
    vertices = []

    with open(datafile, "r") as f:
        # how many points?
        n = int(f.readline())
        for _ in range(n):
            _x, _y, _z = map(float, f.readline().split())
            points.append((_x, _y, _z))
        # how many triangles?
        n = int(f.readline())
        for _ in range(n):
            _i, _j, _k = map(int, f.readline().split())
            vertices.append((_i, _j, _k))

    return points, vertices


def draw_path(points, color, dash, name):
    x, y, z = zip(*points)

    line = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode="lines",
        line=dict(
            color=color,
            width=5,
            dash=dash,
        ),
        name=name,
    )

    return line


def create_mesh(points, vertices):
    x, y, z = zip(*points)
    i, j, k = zip(*vertices)

    mesh = go.Mesh3d(
        x=x,
        y=y,
        z=z,
        color="lightpink",
        opacity=0.50,
        i=i,
        j=j,
        k=k,
        name="y",
        # for some reason, hover info in dash is buggy without this
        hovertemplate="x: %{x}<br>y: %{y}<br>z: %{z}<extra></extra>",
    )

    return mesh


def filter_vertices(points, vertices):
    new_points = []
    indices = {}
    j = 0
    for i, (x, y, z) in enumerate(points):
        if z > -8.4:
            indices[i] = j
            new_points.append((x, y, z))
            j += 1

    new_vertices = []
    for i, j, k in vertices:
        if i in indices and j in indices and k in indices:
            new_vertices.append((indices[i], indices[j], indices[k]))

    return new_points, new_vertices


def remove_unreferenced_indices(points, vertices):
    indices = set()
    for i, j, k in vertices:
        indices.add(i)
        indices.add(j)
        indices.add(k)

    new_points = []
    new_indices = {}
    j = 0
    for i in indices:
        new_points.append(points[i])
        new_indices[i] = j
        j += 1

    new_vertices = []
    for i, j, k in vertices:
        new_vertices.append((new_indices[i], new_indices[j], new_indices[k]))

    return new_points, new_vertices


def read_ply(file_name):
    V, F = pp3d.read_mesh(file_name)

    vertices = []
    for t in V:
        x, y, z = tuple(t.tolist())
        vertices.append((x, y, z))

    faces = []
    for t in F:
        i, j, k = tuple(t.tolist())
        faces.append((i, j, k))

    return vertices, faces


def distance_squared(p1, p2) -> float:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx * dx + dy * dy + dz * dz


def distance(p1, p2) -> float:
    return distance_squared(p1, p2) ** 0.5


def path_distance(points) -> float:
    dist = 0.0
    for p1, p2 in zip(points[:-1], points[1:]):
        dist += distance(p1, p2)
    return dist


def nearest_vertex_noddy(x, y, z, vertices) -> int:
    p = [x, y, z]
    min_dist = float("inf")
    min_j = -1
    for j, q in enumerate(vertices):
        d = distance_squared(p, q)
        if d < min_dist:
            min_dist = d
            min_j = j
    return min_j
