import torch
import torch.nn as nn
import torch.optim as optim

# Define the UNet model (Generator)
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        # Example layers
        self.conv1 = nn.Conv2d(3, 64, kernel_size=4, stride=2, padding=1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.conv1(x))
        return x

# Define the Discriminator model
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        # Example layers
        self.conv1 = nn.Conv2d(3, 64, kernel_size=4, stride=2, padding=1)
        self.leaky_relu = nn.LeakyReLU(0.2)
        self.fc = nn.Linear(64 * 128 * 128, 1)  # Adjust dimensions as needed

    def forward(self, x):
        x = self.leaky_relu(self.conv1(x))
        x = x.view(x.size(0), -1)  # Flatten the tensor
        x = self.fc(x)
        return x

# Instantiate the models
generator = UNet()
discriminator = Discriminator()

# Create optimizers for the models
optimizer_g = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_d = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

print("Models and optimizers initialized successfully.")
