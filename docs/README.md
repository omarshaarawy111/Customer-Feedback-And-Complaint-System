# Social Listening App - Documentation

Welcome to the comprehensive documentation for the Social Listening App. This documentation will help you get started with social media analytics, understand all features, and optimize your social listening workflows.

## 📚 Documentation Sections

### 🚀 Getting Started
- **[Installation Guide](installation.md)** - Complete setup instructions for all platforms
- **[Quick Start](#quick-start)** - Start analyzing social data in 5 minutes

### 👤 User Documentation
- **[User Guide](user-guide.md)** - Complete feature documentation and analytics workflows
- **[Data Formats](data-formats.md)** - CSV/Excel templates and data specifications
- **[Best Practices](best-practices.md)** - Social listening optimization and analytics tips

### 🔧 Technical Documentation
- **[API Reference](api-reference.md)** - Code documentation and module reference
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## Quick Start

1. **Install the app**: Follow the [Installation Guide](installation.md)
2. **Prepare your data**: Use templates from [Data Formats](data-formats.md)
3. **Upload and analyze**: Follow steps in the [User Guide](user-guide.md)
4. **Generate reports**: Export professional HTML reports
5. **Optimize insights**: Apply [Best Practices](best-practices.md)

## 🎯 What Can This App Do?

### Core Analytics Features
- **📊 Data Upload**: Support for CSV/Excel files with social listening data
- **🔍 Advanced Filtering**: Multi-dimensional data filtering capabilities
- **📈 Interactive Visualizations**: Dynamic charts with Plotly integration
- **📋 Professional Reports**: Generate branded HTML reports for stakeholders
- **🎨 Custom Branding**: Configurable color schemes and logo integration

### Supported Analysis Types
| Analysis Type | Input Data | Output |
|---------------|------------|---------|
| Trend Analysis | Time-series mentions | Line charts + insights |
| Brand Comparison | Multi-brand data | Comparative visualizations |
| Sentiment Analysis | Classified mentions | Pie charts + metrics |
| Geographic Analysis | Location-tagged data | Maps + regional insights |
| Channel Performance | Platform-specific data | Multi-chart dashboards |

## 🏗️ Application Architecture

```
Social Listening App
├── Authentication Layer (auth.py)
├── Data Processing Engine (file_utils.py)
├── Visualization Components (visualizations.py)
├── Report Generation (report_utils.py)
└── User Interface (Streamlit + Components)
```

## 📊 Data Requirements

### Minimum Data Schema
```csv
Date,Brand,Country,Type,Type_Detail,Contact_Way,Mentions,Engagement,Sentiment
2024-01-01,BrandA,USA,Social,Facebook,Organic,150,1200,Positive
2024-01-01,BrandB,UK,Social,Twitter,Paid,89,890,Neutral
```

### Supported Data Sources
- **CSV Files**: UTF-8 encoding recommended
- **Excel Files**: .xlsx and .xls formats
- **Data Size**: Optimized for datasets up to 100,000+ records
- **Multi-sheet**: Excel workbooks with multiple data sheets

## 🎨 Visualization Capabilities

### Available Chart Types
- **📊 Bar Charts**: Brand comparison, channel performance
- **🥧 Pie Charts**: Sentiment distribution, share of voice
- **📈 Line Charts**: Trend analysis over time
- **🗺️ Maps**: Geographic distribution (coming soon)
- **📋 Tables**: Detailed data views with sorting/filtering

### Interactive Features
- Hover tooltips with detailed information
- Zoom and pan capabilities
- Dynamic filtering and real-time updates
- Export charts as PNG/HTML
- Responsive design for all screen sizes

## 🔐 Security & Authentication

### Login System
- **Username**: `social listening`
- **Password**: `1234`
- Session management with automatic timeout
- Secure file upload handling

### Data Privacy
- Files processed locally (not stored permanently)
- No data transmission to external servers
- Automatic cleanup of temporary files
- User session isolation

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.9 or higher
- **RAM**: 2GB available memory
- **Storage**: 200MB free disk space
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)
- **Network**: Local network access (localhost:8501)

### Recommended Specifications
- **Python**: 3.10+ for optimal performance
- **RAM**: 4GB+ for large datasets
- **Storage**: 500MB+ for data files and exports
- **CPU**: Multi-core processor for faster processing
- **Display**: 1920x1080 resolution for best experience

## 🚨 Before You Start

### Data Preparation Checklist
- [ ] **Data Quality**: Clean and consistent data format
- [ ] **Column Headers**: Match required schema
- [ ] **Date Format**: Use standard date formats (YYYY-MM-DD)
- [ ] **File Size**: Ensure file size is manageable (<50MB recommended)
- [ ] **Encoding**: Use UTF-8 encoding for international characters

### Environment Setup
- [ ] **Python Installation**: Version 3.9+ installed
- [ ] **Virtual Environment**: Created and activated
- [ ] **Dependencies**: All packages installed via requirements.txt
- [ ] **Assets**: Nestlé logo placed in assets/ directory
- [ ] **Browser**: Modern browser available

## 📈 Key Metrics and KPIs

The app automatically calculates and displays:

### Social Listening Metrics
- **Total Mentions**: Overall brand mention count
- **Engagement Rate**: Average engagement per mention
- **Sentiment Score**: Overall sentiment distribution
- **Share of Voice**: Brand comparison metrics
- **Trend Growth**: Period-over-period changes

### Performance Indicators
- **Response Time**: How quickly trends are identified
- **Data Freshness**: Recency of analyzed data
- **Coverage**: Geographic and platform coverage
- **Accuracy**: Data quality and completeness metrics

## 🔄 Workflow Overview

### Typical Analysis Workflow
```
1. Data Upload → 2. Quality Check → 3. Filter Application → 4. Visualization → 5. Report Generation
```

### Advanced Analytics Workflow
```
1. Multi-source Data → 2. Data Merging → 3. Advanced Filtering → 4. Comparative Analysis → 5. Executive Reporting
```

## 🎯 Best Use Cases

### Brand Monitoring
- Track brand mentions across social platforms
- Monitor brand sentiment in real-time
- Identify trending topics and conversations
- Compare performance against competitors

### Campaign Analysis
- Measure social media campaign effectiveness
- Track hashtag performance and reach
- Analyze audience engagement patterns
- ROI calculation for social media spend

### Crisis Management
- Real-time monitoring of brand sentiment
- Identify potential PR issues early
- Track crisis response effectiveness
- Generate emergency reports for stakeholders

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/omarshaarawy111/Social_Listening/issues)
- **Email the developer**:(mailto:omar.shaarawy@eg.nestle.com)
- **Discussions**: [GitHub Discussions](https://github.com/omarshaarawy111/Social_Listening/discussions)
- **Documentation**: You're reading it!
- **Team**: Web & Search Team - NBS Cairo

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Next Steps**: Start with the [Installation Guide](installation.md) to set up your social listening environment.

---

**Version**: 1.0.0 Beta  
**Last Updated**: August 20, 2025  
**Developed by**: Web & Search Team - NBS Cairo 