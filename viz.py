import sys
import numpy as np
from PyQt5 import QtWidgets, QtCore
from vispy import scene, app
from vispy.scene import visuals

# -------------------------------
# VisPy Canvas for voxel rendering
# -------------------------------
class VoxelCanvas(scene.SceneCanvas):
    def __init__(self, parent=None):
        super().__init__(keys=None, bgcolor='white', parent=parent, show=True)
        self.unfreeze()

        self.view = self.central_widget.add_view()
        self.view.camera = scene.cameras.TurntableCamera(fov=45, distance=4)

        # Marker visual for voxels
        self.scatter = visuals.Markers(parent=self.view.scene)

        self.freeze()

    def update_voxels(self, data, threshold=0.3):
        """
        data: 3D numpy array of shape (N,N,N), values -1..1
        threshold: only draw voxels with abs(value) > threshold
        """
        # Compute coordinates
        N = data.shape[0]
        xs = np.linspace(-1, 1, N)
        ys = np.linspace(-1, 1, N)
        zs = np.linspace(-1, 1, N)
        X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')

        # Mask for visible voxels
        mask = data > threshold
        points = np.vstack([X[mask], Y[mask], Z[mask]]).T

        # Color voxels based on value
        colors = np.zeros((len(points), 4), dtype=np.float32)
        colors[:, 0] = 0.5 + 0.5*data[mask]  # red channel
        colors[:, 1] = 0.5 + 0.5*data[mask]  # green channel
        colors[:, 2] = 1.0 - 0.5*data[mask]  # blue channel
        colors[:, 3] = 1.0                     # alpha
        colors = np.clip(colors, 0, 1)
        self.scatter.set_data(points, face_color=colors, size=20)

# -------------------------------
# Main PyQt Application
# -------------------------------
class NoiseApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Noise Voxel Visualizer")
        self.resize(1000, 600)

        # Layouts
        hbox = QtWidgets.QHBoxLayout(self)
        self.setLayout(hbox)

        # Left: VisPy Canvas
        self.canvas = VoxelCanvas()
        canvas_widget = self.canvas.native
        hbox.addWidget(canvas_widget, stretch=2)

        # Right: Editor + Button
        editor_layout = QtWidgets.QVBoxLayout()
        self.code_editor = QtWidgets.QPlainTextEdit()
        self.code_editor.setPlainText(
            "def noise(x, y, z):\n"
            "    return np.sin(4*x) * np.cos(4*y) * np.sin(4*z)"
        )
        editor_layout.addWidget(self.code_editor)

        self.update_button = QtWidgets.QPushButton("Update Visualization")
        editor_layout.addWidget(self.update_button)
        editor_layout.addStretch()
        hbox.addLayout(editor_layout, stretch=1)

        # Connect button
        self.update_button.clicked.connect(self.update_plot)

        # Initialize plot
        self.update_plot()

    def update_plot(self):
        # Get code from editor
        code = self.code_editor.toPlainText()

        # Build function safely
        local_ns = {}
        try:
            exec(code, {"np": np}, local_ns)
            func = local_ns["noise"]
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error in noise function:\n{e}")
            return

        # Generate voxel data
        N = 128  # Adjust for speed; 64 or 128 if your GPU is fast
        xs = np.linspace(-1, 1, N)
        ys = np.linspace(-1, 1, N)
        zs = np.linspace(-1, 1, N)
        X, Y, Z = np.meshgrid(xs, ys, zs, indexing='ij')

        # Evaluate noise function
        try:
            data = func(X, Y, Z)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error evaluating noise:\n{e}")
            return

        # Ensure float32 and clamp
        data = np.array(data, dtype=np.float32)
        self.canvas.update_voxels(data, threshold=0)

# -------------------------------
# Run the app
# -------------------------------
if __name__ == "__main__":
    appQt = QtWidgets.QApplication(sys.argv)
    win = NoiseApp()
    win.show()
    sys.exit(appQt.exec_())


# """
def noise(x, y, z):
    
    a = np.array([1, 1, 1, 0.124312])
    b = np.array([1, 1, 1, 4.34224312])
    b *= 4
    a *= 4
    a = np.cos(a[0] * x + a[1] * y + a[2] * z + a[3])
    b = np.cos(b[0] * x + b[1] * y + b[2] * z + b[3])
    a = 1-np.abs(np.sin(-2*(x*y)))
    #a *= np.sin(6*x+-6*y+5*z+0.412)
    return a
    
# """