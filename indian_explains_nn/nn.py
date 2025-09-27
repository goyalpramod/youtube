import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import numpy as np

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        # Input layer expects a flattened 28x28 image, which is 784
        self.fc1 = nn.Linear(28 * 28, 1024)
        self.fc2 = nn.Linear(1024, 1024)
        self.fc3 = nn.Linear(1024, 1024)
        self.fc4 = nn.Linear(1024, 1024)
        # Output layer for 10 classes (digits 0-9)
        self.fc5 = nn.Linear(1024, 10)

    def forward(self, x):
        # Flatten the input image from 28x28 to a 1D tensor of 784 elements
        x = torch.flatten(x, 1)
        
        # Pass through the hidden layers with ReLU activation
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        
        # Pass through the output layer
        x = self.fc5(x)
        
        # Apply log_softmax for a classification problem
        return F.log_softmax(x, dim=1)

def train(model, train_loader, optimizer, criterion, device):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'Train Step: {batch_idx}\tLoss: {loss.item():.6f}')

def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item()  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print(f'\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} ({100. * correct / len(test_loader.dataset):.0f}%)\n')

def generate_activations(model, dataset, device, num_samples=100):
    model.eval().to(device)
    activations = {
        'input': [],
        'fc1': [],
        'fc2': [],
        'fc3': [],
        'fc4': [],
        'output': []
    }
    
    with torch.no_grad():
        for i in range(num_samples):
            # Get a sample image and its label
            x, y = dataset[i]
            x = x.to(device).unsqueeze(0)  # Add a batch dimension
            
            # Record the input
            activations['input'].append(np.abs(x.cpu().squeeze().numpy()))
            
            # Pass through the layers and record activations
            x = torch.flatten(x, 1)
            
            x = F.relu(model.fc1(x))
            activations['fc1'].append(np.abs(x.cpu().squeeze().numpy()))

            x = F.relu(model.fc2(x))
            activations['fc2'].append(np.abs(x.cpu().squeeze().numpy()))

            x = F.relu(model.fc3(x))
            activations['fc3'].append(np.abs(x.cpu().squeeze().numpy()))
            
            x = F.relu(model.fc4(x))
            activations['fc4'].append(np.abs(x.cpu().squeeze().numpy()))
            
            # Final layer (fc5) - note: no ReLU before softmax
            x = F.log_softmax(model.fc5(x), dim=1)
            activations['output'].append(np.abs(x.cpu().squeeze().numpy()))

    # Convert lists to NumPy arrays
    for key in activations:
        activations[key] = np.array(activations[key])
    
    # Save to a compressed .npz file
    np.savez('activity.npz', **activations)
    print("Activations saved to activity.npz")

if __name__ == "__main__":
    # 1. Hyperparameters and Device Setup
    epochs = 10
    lr = 0.01
    batch_size = 64
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    
    # 2. Data Loading and Transformation
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)
    
    # 3. Model, Optimizer, and Loss Function Initialization
    model = NeuralNetwork().to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = F.nll_loss
    
    # 4. Training Loop
    # for epoch in range(1, epochs + 1):
    #     print(f"--- Epoch {epoch} ---")
    #     train(model, train_loader, optimizer, criterion, device)
    #     test(model, test_loader, criterion, device)
        
    # 5. Save the trained model
    # torch.save(model.state_dict(), "mnist.pth")
    # print("Model saved to mnist.pth")

    # 6. Generate and save the layer activations for visualization
    generate_activations(model, train_dataset, device)