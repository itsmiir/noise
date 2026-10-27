import numpy as np
from vispy import scene, app

canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()
view.camera = 'turntable'

# Generate grid
N = 32
xs = np.linspace(-1, 1, N)
ys = np.linspace(-1, 1, N)
zs = np.linspace(-1, 1, N)
X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')

# Example noise function
data = np.sin(4*X) * np.cos(4*Y) * np.sin(4*Z)

# Threshold to select visible voxels
thresh = 0.3
mask = np.abs(data) > thresh
points = np.vstack([X[mask], Y[mask], Z[mask]]).T
colors = np.zeros((len(points), 4), dtype=np.float32)
colors[:, 0] = 0.5 + 0.5*data[mask]  # red channel by value
colors[:, 3] = 1.0                     # alpha

scatter = scene.visuals.Markers(parent=view.scene)
scatter.set_data(points, face_color=colors, size=3)

app.run()
