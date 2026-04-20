# User Guide - Social Listening App

Complete guide to analyzing social media data, generating insights, and creating professional reports with the Social Listening App.

## 🎯 Overview

The Social Listening App is designed for marketing professionals, brand managers, and data analysts who need to monitor, analyze, and report on social media performance across multiple brands, platforms, and regions.

## 🚀 Getting Started

### Launch the Application
```bash
# Navigate to project directory
cd Social_Listening

# Activate virtual environment
source social_listening_env/bin/activate  # macOS/Linux
# social_listening_env\Scripts\activate    # Windows

# Start the application
streamlit run src/main.py
```

The application will open at [http://localhost:8501](http://localhost:8501)

### Login Process
1. **Access the app**: Open your browser to the provided URL
2. **Enter credentials**:
   - **Username**: `social listening`
   - **Password**: `1234`
3. **Click Login**: You'll be redirected to the main dashboard

## 🖥️ User Interface Overview

### Main Dashboard Components

#### 1. **Header Section**
- Application title and branding
- User session information
- Navigation breadcrumbs
- Logout option

#### 2. **Sidebar Controls**
- **File Upload Area**: CSV/Excel file upload
- **Filter Controls**: Multi-dimensional data filtering
- **Analysis Options**: Chart type selection
- **Export Controls**: Report generation options

#### 3. **Main Content Area**
- **Metrics Dashboard**: Key performance indicators
- **Interactive Visualizations**: Dynamic charts and graphs
- **Data Tables**: Detailed data views
- **Analysis Insights**: Automated insights and recommendations

#### 4. **Footer Section**
- Application version information
- Developer credits
- Support links

## 📊 Data Upload and Management

### Supported File Formats

**CSV Files**:
- UTF-8 encoding recommended
- Comma-separated values
- Headers in first row
- Maximum file size: 50MB

**Excel Files**:
- .xlsx and .xls formats supported
- Multiple sheets supported
- Named ranges supported
- Maximum file size: 50MB

### Upload Process

1. **Click Upload Area**: In the sidebar, click "Choose a file"
2. **Select File**: Browse and select your data file
3. **Automatic Validation**: App validates file format and structure
4. **Preview Data**: Review uploaded data in preview table
5. **Confirm Upload**: Click "Process Data" to continue

### Data Requirements

**Minimum Required Columns**:
```csv
Date,Brand,Country,Mentions,Sentiment
2024-01-01,BrandA,USA,100,Positive
2024-01-02,BrandB,UK,150,Neutral
```

**Complete Schema** (recommended):
```csv
Date,Year,Quarter,Month,Brand,Country,Type,Type_Detail,Contact_Way,Mentions,Engagement,Reach,Sentiment,Keywords,Platform,Campaign
```

### Data Validation

The app automatically validates:
- **Date Formats**: Accepts multiple date formats (YYYY-MM-DD, MM/DD/YYYY, etc.)
- **Required Fields**: Ensures essential columns are present
- **Data Types**: Validates numeric fields contain numbers
- **Value Ranges**: Checks for realistic data ranges
- **Duplicate Detection**: Identifies and flags duplicate records

## 🔍 Filtering and Analysis

### Available Filters

#### **Temporal Filters**
- **Year**: Select single or multiple years
- **Quarter**: Q1, Q2, Q3, Q4 selection
- **Month**: Individual months or ranges
- **Date Range**: Custom start and end dates

#### **Demographic Filters**
- **Brand**: Single or multi-brand analysis
- **Country**: Geographic filtering
- **Region**: Regional groupings (if available)

#### **Platform Filters**
- **Type**: Social media, news, forums, blogs
- **Type Detail**: Facebook, Twitter, Instagram, LinkedIn, etc.
- **Contact Way**: Organic, paid, influencer

#### **Performance Filters**
- **Mention Range**: Filter by mention count
- **Engagement Range**: Filter by engagement levels
- **Sentiment**: Positive, neutral, negative

### Filter Application

1. **Select Filters**: Use sidebar controls to set filter criteria
2. **Apply Filters**: Click "Apply Filters" button
3. **View Results**: Data automatically updates in visualizations
4. **Reset Filters**: Use "Clear All Filters" to reset

### Advanced Filtering

**Multi-Select Options**:
```python
# Example: Analyze multiple brands
Brands: [BrandA, BrandB, BrandC]
Countries: [USA, UK, Canada]
Sentiment: [Positive, Neutral]
```

**Date Range Combinations**:
```python
# Example: Compare quarterly performance
Q1 2024 vs Q1 2023
January-March vs April-June
Week-over-week analysis
```

## 📈 Visualization Features

### Chart Types Available

#### **1. Bar Charts**
**Use Cases**: Brand comparison, platform performance, country analysis

**Features**:
- Horizontal and vertical orientations
- Stacked and grouped options
- Interactive hover tooltips
- Sort by value or alphabetically

**Example Analysis**:
```
Brand Performance Comparison
- X-axis: Brands (BrandA, BrandB, BrandC)
- Y-axis: Total mentions
- Color: Sentiment (Positive, Neutral, Negative)
```

#### **2. Line Charts**
**Use Cases**: Trend analysis, time-series data, growth tracking

**Features**:
- Multiple series support
- Zoom and pan functionality
- Date range selection
- Trend line indicators
- Seasonal pattern detection

**Example Analysis**:
```
Monthly Mention Trends
- X-axis: Time (months)
- Y-axis: Mention count
- Multiple lines: Different brands
- Annotations: Campaign launches, events
```

#### **3. Pie Charts**
**Use Cases**: Sentiment distribution, share of voice, platform breakdown

**Features**:
- Interactive slice selection
- Percentage and absolute values
- Custom color schemes
- Donut chart option

**Example Analysis**:
```
Sentiment Distribution
- Slices: Positive (45%), Neutral (35%), Negative (20%)
- Colors: Green, Yellow, Red
- Hover: Detailed percentages and counts
```

#### **4. Scatter Plots**
**Use Cases**: Correlation analysis, engagement vs reach, performance mapping

**Features**:
- Bubble size variations
- Color coding by category
- Trend line overlay
- Outlier identification

**Example Analysis**:
```
Engagement vs Reach Analysis
- X-axis: Reach (audience size)
- Y-axis: Engagement rate
- Bubble size: Mention count
- Color: Platform type
```

### Interactive Features

**Zoom and Pan**:
- Mouse wheel to zoom in/out
- Click and drag to pan
- Double-click to reset view

**Data Selection**:
- Click legend items to show/hide series
- Box select for detailed analysis
- Hover tooltips with detailed information

**Export Options**:
- PNG image export
- HTML interactive export
- SVG vector export
- PDF report generation

## 📊 Key Metrics and KPIs

### Automatically Calculated Metrics

#### **Volume Metrics**
- **Total Mentions**: Overall mention count across all sources
- **Unique Sources**: Number of distinct platforms/channels
- **Average Daily Mentions**: Daily average over selected period
- **Peak Mention Day**: Day with highest mention volume

#### **Engagement Metrics**
- **Total Engagement**: Sum of likes, shares, comments
- **Engagement Rate**: Engagement per mention ratio
- **Average Engagement**: Mean engagement per mention
- **Engagement Growth**: Period-over-period change

#### **Sentiment Metrics**
- **Sentiment Score**: Weighted average sentiment
- **Positive Ratio**: Percentage of positive mentions
- **Negative Ratio**: Percentage of negative mentions
- **Sentiment Trend**: Sentiment change over time

#### **Share of Voice**
- **Brand SOV**: Brand's share of total mentions
- **Platform SOV**: Platform distribution percentage
- **Geographic SOV**: Country/region distribution
- **Competitive SOV**: Comparison with competitors

### Custom KPI Configuration

**Metric Customization**:
```python
# Define custom metrics in the app
Custom KPI = (Positive Mentions - Negative Mentions) / Total Mentions
Brand Health Score = (Engagement Rate × 0.4) + (Sentiment Score × 0.6)
Crisis Alert = Negative Mentions > Threshold AND Mention Velocity > Normal
```

## 📋 Report Generation

### HTML Report Features

#### **Automated Report Sections**
1. **Executive Summary**: Key metrics and insights
2. **Trend Analysis**: Time-series visualizations
3. **Brand Performance**: Comparative analysis
4. **Geographic Insights**: Regional performance
5. **Platform Analysis**: Channel-specific metrics
6. **Sentiment Overview**: Sentiment distribution and trends
7. **Recommendations**: Data-driven insights

#### **Report Customization**
- **Company Branding**: Logo and color scheme integration
- **Date Range Selection**: Custom reporting periods
- **Metric Selection**: Choose relevant KPIs
- **Chart Selection**: Include specific visualizations
- **Narrative Text**: Add custom insights and commentary

### Report Generation Process

1. **Configure Report Settings**:
   ```
   Report Title: Q1 2024 Social Listening Report
   Date Range: January 1 - March 31, 2024
   Brands: [BrandA, BrandB]
   Metrics: [Mentions, Engagement, Sentiment]
   ```

2. **Select Visualizations**:
   - Trend charts for mention volume
   - Pie charts for sentiment distribution
   - Bar charts for brand comparison
   - Geographic maps for regional analysis

3. **Generate Report**:
   - Click "Generate Report" button
   - Processing time: 30-60 seconds
   - Download link appears when complete

4. **Export Options**:
   - **HTML**: Interactive web-based report
   - **PDF**: Static document for sharing
   - **PowerPoint**: Presentation-ready slides
   - **Excel**: Data tables with charts

### Report Sharing and Distribution

**Sharing Options**:
- **Email Integration**: Direct email sending
- **URL Generation**: Shareable web links
- **Cloud Storage**: Upload to Google Drive, Dropbox
- **Scheduled Reports**: Automated periodic generation

**Access Control**:
- **Password Protection**: Secure report access
- **Expiration Dates**: Time-limited access
- **View-only Mode**: Prevent data modification
- **Audit Trail**: Track report access and views

## 🔄 Workflow Examples

### Weekly Brand Monitoring

**Objective**: Monitor brand mentions and sentiment weekly

**Steps**:
1. **Upload Data**: Weekly social listening data export
2. **Apply Filters**: 
   - Date: Last 7 days
   - Brand: Your brand only
   - All platforms
3. **Generate Visualizations**:
   - Daily mention trend (line chart)
   - Sentiment distribution (pie chart)
   - Platform performance (bar chart)
4. **Create Report**: Weekly brand health report
5. **Share with Team**: Email to marketing team

### Campaign Performance Analysis

**Objective**: Analyze social media campaign effectiveness

**Steps**:
1. **Upload Campaign Data**: Include campaign tags/identifiers
2. **Filter by Campaign**:
   - Date: Campaign period
   - Campaign ID: Specific campaign
   - Include pre/post periods for comparison
3. **Analyze Performance**:
   - Mention volume before/during/after
   - Engagement rate changes
   - Sentiment impact
   - Geographic reach expansion
4. **Generate Insights**:
   - ROI calculations
   - Audience growth metrics
   - Content performance analysis
5. **Create Executive Report**: Campaign success summary

### Competitive Intelligence

**Objective**: Monitor competitor performance and market share

**Steps**:
1. **Multi-Brand Analysis**:
   - Include your brand + top 3 competitors
   - Same date range and filters
   - All relevant platforms
2. **Comparative Metrics**:
   - Share of voice analysis
   - Engagement rate comparison
   - Sentiment benchmarking
   - Platform preference analysis
3. **Trend Identification**:
   - Growth rate comparisons
   - Seasonal pattern analysis
   - Campaign timing insights
4. **Strategic Report**: Competitive landscape overview

### Crisis Monitoring and Response

**Objective**: Detect and analyze potential PR crises

**Steps**:
1. **Real-time Monitoring**:
   - Upload most recent data
   - Filter for negative sentiment spikes
   - Monitor mention velocity increases
2. **Crisis Detection**:
   - Identify unusual patterns
   - Analyze sentiment trends
   - Track mention sources
3. **Impact Assessment**:
   - Measure sentiment impact
   - Assess reach and virality
   - Identify key influencers/sources
4. **Response Tracking**:
   - Monitor response effectiveness
   - Track sentiment recovery
   - Measure damage control success

## 🎨 Customization Options

### Visual Customization

**Color Schemes**:
- **Corporate Colors**: Match brand guidelines
- **High Contrast**: Accessibility-focused palettes
- **Seasonal Themes**: Holiday or event-specific colors
- **Custom Palettes**: User-defined color combinations

**Chart Styling**:
- **Font Sizes**: Adjustable text sizing
- **Grid Lines**: Show/hide chart grids
- **Background Colors**: Light/dark theme options
- **Animation Effects**: Enable/disable chart animations

### Data Display Options

**Table Formatting**:
- **Sorting Options**: Multi-column sorting
- **Number Formatting**: Currency, percentages, thousands separators
- **Conditional Formatting**: Color-coded values based on thresholds
- **Column Selection**: Show/hide specific data columns

**Chart Configuration**:
- **Axis Labels**: Custom axis titles and formatting
- **Legend Position**: Top, bottom, left, right placement
- **Data Labels**: Show values on chart elements
- **Reference Lines**: Add target or benchmark lines

### Advanced Features

**Data Transformation**:
- **Calculated Fields**: Create custom metrics on-the-fly
- **Aggregation Options**: Sum, average, count, median, percentile
- **Time Grouping**: Daily, weekly, monthly, quarterly aggregation
- **Normalization**: Per capita, indexed, or standardized values

**Alert Configuration**:
- **Threshold Alerts**: Automated notifications for unusual patterns
- **Trend Alerts**: Notifications for significant changes
- **Sentiment Alerts**: Warnings for negative sentiment spikes
- **Volume Alerts**: Notifications for mention volume changes

## 🔧 Performance Optimization

### Large Dataset Handling

**Data Size Limits**:
- **Recommended**: Up to 10,000 records for optimal performance
- **Maximum**: 100,000 records with reduced interactivity
- **Optimization**: Use data sampling for very large datasets

**Performance Tips**:
- **Filter Early**: Apply filters before generating visualizations
- **Limit Date Ranges**: Use shorter time periods for faster processing
- **Batch Processing**: Process large datasets in chunks
- **Cache Results**: Reuse processed data for multiple visualizations

### Browser Optimization

**Recommended Settings**:
- **RAM**: 4GB+ available memory
- **Browser Cache**: Clear cache periodically
- **Extensions**: Disable unnecessary browser extensions
- **Tabs**: Close other browser tabs during analysis

**Troubleshooting Performance**:
- **Slow Loading**: Reduce data size or simplify visualizations
- **Memory Errors**: Restart browser and try smaller datasets
- **Chart Freezing**: Disable animations and reduce chart complexity

## 🆘 Common Issues and Solutions

### Data Upload Issues

**Issue**: File format not recognized
**Solution**: 
- Ensure file is CSV or Excel format
- Check file extension (.csv, .xlsx, .xls)
- Verify file isn't corrupted

**Issue**: Column headers not matching
**Solution**:
- Use exact column names as specified in data format guide
- Remove extra spaces or special characters
- Check for hidden characters or encoding issues

### Visualization Issues

**Issue**: Charts not displaying correctly
**Solution**:
- Check data types in uploaded file
- Ensure numeric columns contain only numbers
- Verify date columns use standard date formats

**Issue**: Performance is slow
**Solution**:
- Reduce dataset size
- Apply more restrictive filters
- Use simpler chart types
- Close other applications

### Report Generation Issues

**Issue**: Report generation fails
**Solution**:
- Check available disk space
- Verify all required data is present
- Try generating smaller reports first
- Clear browser cache and cookies

## 📞 Support and Help

### Getting Help

- **Documentation**: Check other documentation sections
- **Email the developer**:(mailto:omar.shaarawy@eg.nestle.com)
- **Troubleshooting**: See [troubleshooting.md](troubleshooting.md)
- **GitHub Issues**: [Report problems](https://github.com/omarshaarawy111/Social_Listening/issues)


### Best Practices

- **Regular Backups**: Keep copies of important data files
- **Data Quality**: Ensure clean, consistent data before upload
- **Performance Monitoring**: Monitor system resources during analysis
- **Regular Updates**: Keep the application updated to latest version

---

**Ready for advanced analytics?** Check out the [Best Practices](best-practices.md) guide for optimization tips!