import numpy as np
import pyvista as pv
from pyvistaqt import BackgroundPlotter
import torch
from torch import nn
import torch.nn.functional as F
from PyQt5 import QtWidgets, QtCore

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 1024)
        self.fc2 = nn.Linear(1024, 1024)
        self.fc3 = nn.Linear(1024, 1024)
        self.fc4 = nn.Linear(1024, 1024)
        self.fc5 = nn.Linear(1024, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return F.log_softmax(x, dim=1)

class NeuralNetworkVisualizer(QtWidgets.QMainWindow):
    def __init__(self, model_path='mnist.pth', activity_path='activity.npz'):
        super().__init__()
        
        # Load model and data
        self.model = NeuralNetwork()
        self.model.load_state_dict(torch.load(model_path, map_location='cpu'))
        self.model.eval()
        self.activity = np.load(activity_path)
        
        # Setup UI
        self.setup_ui()
        
        # Setup visualization
        self.setup_visualization()
        
        # Animation state
        self.current_frame = 0
        self.animation_timer = QtCore.QTimer()
        self.animation_timer.timeout.connect(self.update_animation)
        self.rotation_enabled = True
        
    def setup_ui(self):
        """Setup the user interface"""
        self.setWindowTitle("Neural Network Visualization - MNIST")
        
        # Create central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        
        # Create plotter
        self.plotter = BackgroundPlotter()
        self.plotter.set_background([0, 0, 0])  # Pure black background
        layout.addWidget(self.plotter)
        
        # Control panel
        controls = QtWidgets.QWidget()
        controls_layout = QtWidgets.QHBoxLayout(controls)
        
        # Play/Pause button
        self.play_button = QtWidgets.QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_animation)
        controls_layout.addWidget(self.play_button)
        
        # Frame slider
        self.frame_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.frame_slider.setMinimum(0)
        self.frame_slider.setMaximum(min(99, len(self.activity['input']) - 1))
        self.frame_slider.valueChanged.connect(self.on_frame_change)
        controls_layout.addWidget(self.frame_slider)
        
        # Frame label
        self.frame_label = QtWidgets.QLabel("Frame: 0")
        controls_layout.addWidget(self.frame_label)
        
        # Rotation toggle
        self.rotation_checkbox = QtWidgets.QCheckBox("Rotate")
        self.rotation_checkbox.setChecked(True)
        self.rotation_checkbox.stateChanged.connect(self.toggle_rotation)
        controls_layout.addWidget(self.rotation_checkbox)
        
        # Speed control
        self.speed_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setValue(5)
        self.speed_slider.valueChanged.connect(self.update_speed)
        controls_layout.addWidget(QtWidgets.QLabel("Speed:"))
        controls_layout.addWidget(self.speed_slider)
        
        layout.addWidget(controls)
        
    def setup_visualization(self):
        """Setup the 3D visualization"""
        # Generate layer positions
        self.setup_neuron_positions()
        
        # Setup connections
        self.setup_connections()
        
        # Create initial visualization
        self.create_visualization()
        
    def setup_neuron_positions(self):
        """Setup positions for all neurons"""
        def create_layer_positions(shape, center, spread=1.0, jitter=0.0):
            if len(shape) == 2:  # Grid layout
                z, x = np.indices(shape)
                x = (x.ravel() - shape[1]/2) * spread
                z = (z.ravel() - shape[0]/2) * spread
                y = np.ones_like(x) * center[1]
                
                if jitter > 0:
                    x += np.random.rand(len(x)) * jitter
                    z += np.random.rand(len(z)) * jitter
                    y += np.random.rand(len(y)) * jitter * 10
            else:  # Linear layout
                x = (np.arange(shape[0]) - shape[0]/2) * spread
                z = np.zeros_like(x)
                y = np.ones_like(x) * center[1]
            
            return np.column_stack([x + center[0], y, z + center[2]])
        
        # Create positions for each layer
        self.input_pos = create_layer_positions((28, 28), [0, 0, 0], spread=0.8)
        self.fc1_pos = create_layer_positions((32, 32), [0, 20, 0], spread=1.0, jitter=1.0)
        self.fc2_pos = create_layer_positions((32, 32), [0, 40, 0], spread=1.0, jitter=1.0)
        self.fc3_pos = create_layer_positions((32, 32), [0, 60, 0], spread=1.0, jitter=1.0)
        self.fc4_pos = create_layer_positions((32, 32), [0, 80, 0], spread=1.0, jitter=1.0)
        self.output_pos = create_layer_positions((10,), [0, 100, 0], spread=3.0)
        
        # Combine all positions
        self.all_positions = np.vstack([
            self.input_pos, self.fc1_pos, self.fc2_pos, 
            self.fc3_pos, self.fc4_pos, self.output_pos
        ])
        
        # Store layer sizes
        self.n_input = len(self.input_pos)
        self.n_fc1 = len(self.fc1_pos)
        self.n_fc2 = len(self.fc2_pos)
        self.n_fc3 = len(self.fc3_pos)
        self.n_fc4 = len(self.fc4_pos)
        self.n_output = len(self.output_pos)
        
    def setup_connections(self):
        """Setup connections between layers"""
        def get_connections(weight_matrix, threshold, from_start_idx, to_start_idx):
            connections = []
            weights = []
            fr, to = (np.abs(weight_matrix.T) > threshold).nonzero()
            
            # Subsample connections if there are too many
            max_connections = 5000
            if len(fr) > max_connections:
                indices = np.random.choice(len(fr), max_connections, replace=False)
                fr = fr[indices]
                to = to[indices]
            
            for f, t in zip(fr, to):
                connections.append([from_start_idx + f, to_start_idx + t])
                weights.append(abs(weight_matrix[t, f]))
            
            return np.array(connections) if connections else np.empty((0, 2), dtype=int), np.array(weights)
        
        offset = 0
        connections_list = []
        weights_list = []
        
        # Get connections for each layer transition
        conn, w = get_connections(self.model.fc1.weight.detach().numpy(), 0.1, offset, offset + self.n_input)
        connections_list.append(conn)
        weights_list.append(w)
        offset += self.n_input
        
        conn, w = get_connections(self.model.fc2.weight.detach().numpy(), 0.05, offset, offset + self.n_fc1)
        connections_list.append(conn)
        weights_list.append(w)
        offset += self.n_fc1
        
        conn, w = get_connections(self.model.fc3.weight.detach().numpy(), 0.05, offset, offset + self.n_fc2)
        connections_list.append(conn)
        weights_list.append(w)
        offset += self.n_fc2
        
        conn, w = get_connections(self.model.fc4.weight.detach().numpy(), 0.05, offset, offset + self.n_fc3)
        connections_list.append(conn)
        weights_list.append(w)
        offset += self.n_fc3
        
        conn, w = get_connections(self.model.fc5.weight.detach().numpy(), 0.1, offset, offset + self.n_fc4)
        connections_list.append(conn)
        weights_list.append(w)
        
        # Combine all connections
        self.all_connections = np.vstack(connections_list) if connections_list else np.empty((0, 2), dtype=int)
        self.all_weights = np.concatenate(weights_list) if weights_list else np.array([])
        
    def create_visualization(self):
        """Create the initial visualization"""
        # Create point cloud for neurons
        self.neuron_cloud = pv.PolyData(self.all_positions)
        
        # Get initial activations
        self.update_activations(0)
        
        # Add neurons
        self.neuron_actor = self.plotter.add_mesh(
            self.neuron_cloud,
            style='points',
            point_size=8,
            scalars="activation",
            cmap="gray",
            show_scalar_bar=False,
            render_points_as_spheres=True
        )
        
        # Add connections
        if len(self.all_connections) > 0:
            lines = []
            for conn in self.all_connections:
                lines.append(2)
                lines.extend(conn)
            
            self.line_mesh = pv.PolyData(self.all_positions)
            self.line_mesh.lines = np.array(lines)
            
            self.plotter.add_mesh(
                self.line_mesh,
                style='wireframe',
                line_width=0.5,
                opacity=0.1,
                color='gray',
                show_scalar_bar=False
            )
        
        # Add text label only for predicted digit
        # Store as instance variable so we can update it
        self.output_label_actor = None
        self.update_output_label(0)  # Initialize with first frame
        
        # Set initial camera
        self.plotter.camera.position = (150, 50, 0)    # Camera to the side (positive X)
        self.plotter.camera.focal_point = (0, 50, 0)   # Looking at center of network
        self.plotter.camera.up = (0, 0, 1)             # Z-axis up
        self.plotter.camera.zoom(0.8)                  # Adjust zoom to fit
        
        # Store initial camera position
        self.initial_camera_pos = self.plotter.camera_position
        self.rotation_angle = 0
        
    def update_activations(self, frame_idx):
        """Update neuron activations for a given frame"""
        if frame_idx >= len(self.activity['input']):
            return
        
        # Get activations
        act_input = self.activity['input'][frame_idx]
        act_fc1 = self.activity['fc1'][frame_idx]
        act_fc2 = self.activity['fc2'][frame_idx]
        act_fc3 = self.activity['fc3'][frame_idx]
        act_fc4 = self.activity['fc4'][frame_idx]
        act_output = self.activity['output'][frame_idx]
        
        # Normalize and combine
        activations = np.hstack([
            act_input.ravel() / (act_input.max() + 1e-8),
            act_fc1 / (act_fc1.max() + 1e-8),
            act_fc2 / (act_fc2.max() + 1e-8),
            act_fc3 / (act_fc3.max() + 1e-8),
            act_fc4 / (act_fc4.max() + 1e-8),
            act_output / (act_output.max() + 1e-8)
        ])
        
        self.neuron_cloud["activation"] = activations
        
    def update_output_label(self, frame_idx):
        """Update the output label to show only the predicted digit"""
        if frame_idx >= len(self.activity['output']):
            return
        
        # Get the predicted digit (highest activation)
        act_output = self.activity['output'][frame_idx]
        predicted_digit = np.argmax(act_output)
        
        # Remove previous label if it exists
        if self.output_label_actor is not None:
            self.plotter.remove_actor(self.output_label_actor)
        
        # Add label for predicted digit only
        self.output_label_actor = self.plotter.add_point_labels(
            self.output_pos[predicted_digit:predicted_digit+1],
            [str(predicted_digit)],
            point_size=20,
            font_size=48,
            text_color='white',
            font_family='arial',
            show_points=False,
            always_visible=True
        )
        
    def on_frame_change(self, value):
        """Handle frame slider change"""
        self.current_frame = value
        self.frame_label.setText(f"Frame: {value}")
        self.update_activations(value)
        self.update_output_label(value)  # Update the label
        self.plotter.render()
        
    def toggle_animation(self):
        """Start/stop animation"""
        if self.animation_timer.isActive():
            self.animation_timer.stop()
            self.play_button.setText("Play")
        else:
            self.animation_timer.start(100)  # Update every 100ms
            self.play_button.setText("Pause")
            
    def toggle_rotation(self, state):
        """Toggle camera rotation"""
        self.rotation_enabled = state == QtCore.Qt.Checked
        
    def update_speed(self, value):
        """Update animation speed"""
        self.animation_timer.setInterval(200 // value)
        
    def update_animation(self):
        """Update animation frame"""
        # Update frame
        self.current_frame = (self.current_frame + 1) % self.frame_slider.maximum()
        self.frame_slider.setValue(self.current_frame)
        self.update_output_label(self.current_frame)  # Update the label
        
        # Rotate camera if enabled
        if self.rotation_enabled:
            self.rotation_angle = (self.rotation_angle + 2) % 360
            rad = np.radians(self.rotation_angle)
            # Orbit around the Z-axis (vertical) to maintain side view perspective
            self.plotter.camera_position = [
                (150 * np.cos(rad), 50 + 150 * np.sin(rad), 0),  # position
                (0, 50, 0),                                       # focal_point
                (0, 0, 1)                                         # view_up
            ]
        
        self.plotter.render()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = NeuralNetworkVisualizer()
    window.show()
    app.exec_()