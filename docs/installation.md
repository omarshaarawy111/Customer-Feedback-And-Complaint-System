# Installation Guide - Social Listening App

Complete installation guide for setting up the Social Listening App on your system.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux Ubuntu 18.04+
- **RAM**: 2GB minimum, 4GB recommended for large datasets
- **Storage**: 200MB free disk space
- **Network**: Internet connection for initial setup

### Required Software
- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)
- **Modern Web Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Git** (optional): For cloning the repository

## 🚀 Installation Methods

### Method 1: Standard Installation (Recommended)

#### Step 1: Clone Repository
```bash
# Using Git
git clone https://github.com/omarshaarawy111/Social_Listening.git
cd Social_Listening

# Or download ZIP from GitHub and extract
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv social_listening_env

# Activate virtual environment
# Windows:
social_listening_env\Scripts\activate
# macOS/Linux:
source social_listening_env/bin/activate
```

#### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
python -c "import streamlit, plotly, pandas; print('✅ Installation successful')"
```

#### Step 4: Set Up Assets
```bash
# Ensure the Nestlé logo is in the correct location
# Place nestle_logo.png in the assets/ directory
cp /path/to/your/nestle_logo.png assets/nestle_logo.png
```

### Method 2: Development Installation

For developers who want to contribute:

```bash
# Clone with development setup
git clone https://github.com/omarshaarawy111/Social_Listening.git
cd Social_Listening

# Create development environment
python -m venv dev_env
source dev_env/bin/activate  # macOS/Linux
# dev_env\Scripts\activate     # Windows

# Install with development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available

# Install in editable mode
pip install -e .
```

## 📦 Dependencies

### Core Dependencies
The application requires the following Python packages:

```
streamlit>=1.28.0
plotly>=5.15.0
pandas>=2.0.0
openpyxl>=3.1.0
xlsxwriter>=3.1.0
jinja2>=3.1.0
```

### Optional Dependencies
For enhanced functionality:
```
# For advanced data processing
numpy>=1.24.0
scipy>=1.10.0

# For additional chart types
matplotlib>=3.7.0
seaborn>=0.12.0

# For data validation
pydantic>=2.0.0
```

## 🧪 Verify Installation

### Test Basic Functionality
```bash
# Start the application
streamlit run src/main.py

# You should see:
# "You can now view your Streamlit app in your browser."
# "Local URL: http://localhost:8501"
```

### Browser Test
1. Open [http://localhost:8501](http://localhost:8501)
2. You should see the Social Listening App login screen
3. Login with credentials:
   - **Username**: `social listening`
   - **Password**: `1234`
4. Try uploading a sample CSV file from the `data/` folder (if available)

### Component Test
```python
# Test individual components
python -c "
from src.components.visualizations import create_bar_chart
from src.file_utils import validate_data_format
print('✅ All components working correctly')
"
```

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file in the project root:
```env
# Application settings
APP_TITLE=Social Listening App
APP_ICON=📊
DEBUG_MODE=false

# Authentication
DEFAULT_USERNAME=social listening
DEFAULT_PASSWORD=1234
SESSION_TIMEOUT=3600

# Data processing
MAX_FILE_SIZE_MB=50
SUPPORTED_FORMATS=csv,xlsx,xls

# Visualization
DEFAULT_COLOR_SCHEME=plotly
CHART_HEIGHT=400
```

### Streamlit Configuration
Create `.streamlit/config.toml` for custom settings:
```toml
[server]
port = 8501
headless = false

[browser]
gatherUsageStats = false
serverAddress = "localhost"

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Logo and Branding Setup
```bash
# Create assets directory if it doesn't exist
mkdir -p assets

# Add your logo (required for proper branding)
# Logo should be PNG format, recommended size: 200x100px
cp your_company_logo.png assets/nestle_logo.png

# Verify logo placement
ls -la assets/
# Should show: nestle_logo.png
```

## 🐛 Troubleshooting Installation

### Common Issues

#### Python Version Issues
```bash
# Check Python version
python --version
# Should show 3.9 or higher

# If using older version, upgrade Python
# Download from python.org or use package manager
```

#### Virtual Environment Issues
```bash
# If venv module not found
pip install virtualenv
virtualenv social_listening_env

# If permission denied
sudo pip install virtualenv  # Linux/macOS
# Run Command Prompt as Administrator (Windows)
```

#### Dependency Installation Problems

**Issue**: Package installation fails
```bash
# Upgrade pip first
pip install --upgrade pip setuptools wheel

# If specific package fails
pip install package_name --upgrade --force-reinstall

# Clear pip cache
pip cache purge
```

**Issue**: Windows-specific compilation errors
```bash
# Install Microsoft Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Or use pre-compiled wheels
pip install --only-binary=all package_name
```

#### Streamlit Issues
```bash
# If Streamlit doesn't start
streamlit --version

# Clear Streamlit cache
streamlit cache clear

# Reset Streamlit configuration
rm -rf ~/.streamlit  # macOS/Linux
rmdir /s "%USERPROFILE%\.streamlit"  # Windows
```

### Port and Network Issues

**Issue**: Port 8501 already in use
```bash
# Find process using port 8501
lsof -i :8501  # macOS/Linux
netstat -ano | findstr :8501  # Windows

# Kill the process or use different port
streamlit run src/main.py --server.port 8502
```

**Issue**: Browser doesn't open automatically
```bash
# Manually open browser and navigate to:
http://localhost:8501

# Or specify browser
streamlit run src/main.py --browser.gatherUsageStats false
```

### Asset and File Issues

**Issue**: Logo not displaying
```bash
# Check file path and permissions
ls -la assets/nestle_logo.png
# File should exist and be readable

# Check file format
file assets/nestle_logo.png
# Should show: PNG image data
```

**Issue**: Sample data files missing
```bash
# Create sample data directory
mkdir -p data

# Add sample CSV file
echo "Date,Brand,Country,Mentions,Sentiment
2024-01-01,BrandA,USA,100,Positive
2024-01-02,BrandB,UK,150,Neutral" > data/sample_data.csv
```

## 🔄 Updating

### Update Application
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Clear any cached data
rm -rf __pycache__
rm -rf src/__pycache__

# Restart application
streamlit run src/main.py
```

### Update Python Packages
```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install package_name --upgrade

# Update all packages (use with caution)
pip freeze | grep -v "^-e" | cut -d = -f 1 | xargs -n1 pip install -U
```

## 🗂️ Directory Structure After Installation

```
Social_Listening/
├── src/                        # Main application code
│   ├── main.py                 # Application entry point
│   ├── auth.py                 # Authentication module
│   ├── file_utils.py          # File processing utilities
│   ├── color_utils.py         # Color scheme management
│   ├── report_utils.py        # Report generation
│   └── components/            # UI components
│       ├── header.py
│       ├── metrics.py
│       ├── sidebar.py
│       ├── visualizations.py
│       └── footer.py
├── assets/                     # Static assets
│   └── nestle_logo.png        # Company logo
├── data/                      # Sample data files (optional)
├── archive/                   # Legacy code (if any)
├── social_listening_env/      # Virtual environment
├── requirements.txt           # Python dependencies
├── .streamlit/               # Streamlit configuration
├── .env                      # Environment variables (optional)
├── README.md                 # Project overview
└── LICENSE                   # License file
```

## 🧹 Uninstallation

### Remove Virtual Environment
```bash
# Deactivate environment
deactivate

# Remove environment folder
rm -rf social_listening_env  # macOS/Linux
rmdir /s social_listening_env  # Windows
```

### Remove Project
```bash
# Remove entire project
cd ..
rm -rf Social_Listening
```

## 🆘 Need Help?

If you encounter issues during installation:

1. **Check Requirements**: Ensure all prerequisites are met
2. **Review Error Messages**: Most errors provide clear guidance
3. **Check Logs**: Look for detailed error information in terminal output
4. **GitHub Issues**: [Report installation problems](https://github.com/omarshaarawy111/Social_Listening/issues)
5. - **Email the developer**:(mailto:omar.shaarawy@eg.nestle.com)

## ✅ Installation Complete!

Once installation is successful:
- 📖 **Next**: Read the [User Guide](user-guide.md)
- 📊 **Prepare Data**: Check [Data Formats](data-formats.md)
- 🚀 **Start Analyzing**: Launch the app with `streamlit run src/main.py`

---

**Installation completed successfully?** Continue to the [User Guide](user-guide.md) to start your social listening analytics!