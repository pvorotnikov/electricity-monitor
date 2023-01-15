# electricity-monitor
This small script monitors the electricity status as reported by the electricity provider for one or several subscription IDs.

# Development installation

```sh
# Create virtual environment
virtualenv .virtualenv -p python3

# Load it
.\.virtualenv\Scripts\activate          # Windows
source ./.virtualenv/bin/activate       # Bash, zsh
source ./.virtualenv/bin/activate.fish  # fish\

# Install the package
pip install -e .
```

# Build Docker image

```sh
docker build -t electricity-monitor:latest .
```

# Run the monitor using Docker
```sh
docker run --rm -it electricity-monitor:latest electricity monitor <subscription-id>
```