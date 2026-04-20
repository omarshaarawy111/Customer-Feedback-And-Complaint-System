# Data Formats Guide - Social Listening App

Complete guide to data format requirements, templates, and best practices for the Social Listening App.

## 📊 Overview

The Social Listening App supports CSV and Excel files with social media monitoring data. This guide covers required data formats, optional fields, and optimization tips for the best analysis experience.

---

## 📋 Required Data Schema

### Minimum Required Columns

**Essential Fields** (must be present):
```csv
Date,Brand,Country,Mentions,Sentiment
2024-01-15,BrandA,USA,150,Positive
2024-01-15,BrandB,UK,89,Neutral
2024-01-15,BrandC,Canada,234,Negative
```

### Complete Data Schema

**Full Schema** (recommended for comprehensive analysis):
```csv
Date,Year,Quarter,Month,Brand,Country,Type,Type_Detail,Contact_Way,Mentions,Engagement,Reach,Sentiment,Keywords,Platform,Campaign,Influencer_Tier,Cost,Impressions
```

### Field Descriptions

#### **Temporal Fields**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Date` | Date | Analysis date | YYYY-MM-DD | 2024-01-15 |
| `Year` | Integer | Year value | YYYY | 2024 |
| `Quarter` | String | Quarter designation | Q1/Q2/Q3/Q4 | Q1 |
| `Month` | String | Month name | Full/Abbreviated | January, Jan |

#### **Brand and Geographic Fields**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Brand` | String | Brand identifier | Text | BrandA, Nike, Coca-Cola |
| `Country` | String | Country name | Full/ISO Code | USA, United States, US |
| `Region` | String | Geographic region | Text | North America, Europe |
| `City` | String | City name | Text | New York, London |

#### **Platform and Content Fields**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Type` | String | Media type | Category | Social, News, Blog, Forum |
| `Type_Detail` | String | Specific platform | Platform name | Facebook, Twitter, Instagram |
| `Platform` | String | Platform identifier | Text | FB, TW, IG, LI |
| `Contact_Way` | String | Engagement method | Category | Organic, Paid, Influencer |

#### **Performance Metrics**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Mentions` | Integer | Mention count | Number | 150, 89, 234 |
| `Engagement` | Integer | Total engagement | Number | 1250, 456, 789 |
| `Reach` | Integer | Audience reach | Number | 15000, 8900, 23400 |
| `Impressions` | Integer | Total impressions | Number | 50000, 25000 |
| `Clicks` | Integer | Click count | Number | 125, 67, 89 |
| `Shares` | Integer | Share count | Number | 45, 23, 67 |
| `Comments` | Integer | Comment count | Number | 78, 34, 56 |
| `Likes` | Integer | Like count | Number | 234, 156, 345 |

#### **Sentiment and Quality**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Sentiment` | String | Sentiment classification | Positive/Neutral/Negative | Positive |
| `Sentiment_Score` | Float | Numerical sentiment | -1.0 to 1.0 | 0.75, -0.23, 0.12 |
| `Emotion` | String | Emotion category | Text | Joy, Anger, Fear, Surprise |
| `Relevance` | Float | Content relevance | 0.0 to 1.0 | 0.95, 0.67, 0.82 |

#### **Campaign and Attribution**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Campaign` | String | Campaign identifier | Text | Summer2024, BlackFriday |
| `Campaign_Type` | String | Campaign category | Text | Product Launch, Awareness |
| `Keywords` | String | Associated keywords | Comma-separated | running shoes, fitness, sport |
| `Hashtags` | String | Hashtags used | Comma-separated | #justdoit, #fitness, #run |

#### **Influencer and Cost**
| Field | Type | Description | Format | Example |
|-------|------|-------------|--------|---------|
| `Influencer_Tier` | String | Influencer level | Category | Nano, Micro, Macro, Mega |
| `Influencer_Name` | String | Influencer identifier | Text | @fitness_guru, @tech_reviewer |
| `Cost` | Float | Associated cost | Currency | 1250.50, 89.99 |
| `Cost_Currency` | String | Currency code | ISO Code | USD, EUR, GBP |

---

## 📁 File Format Specifications

### CSV Files

**Encoding Requirements**:
- **Encoding**: UTF-8 (preferred) or UTF-8 BOM
- **Delimiter**: Comma (,)
- **Quote Character**: Double quotes (")
- **Line Endings**: Unix (LF) or Windows (CRLF)

**CSV Example**:
```csv
Date,Brand,Country,Type,Type_Detail,Contact_Way,Mentions,Engagement,Sentiment
2024-01-15,BrandA,USA,Social,Facebook,Organic,150,1250,Positive
2024-01-15,BrandA,USA,Social,Instagram,Paid,89,756,Neutral
2024-01-15,BrandB,UK,News,BBC,Organic,45,890,Negative
2024-01-16,BrandA,Canada,Social,Twitter,Influencer,234,2100,Positive
```

**CSV Best Practices**:
- Include headers in the first row
- Use consistent date formats throughout
- Avoid special characters in text fields
- Escape commas within data fields with quotes
- Keep file size under 50MB for optimal performance

### Excel Files

**Supported Formats**:
- **Excel 2007+**: .xlsx (recommended)
- **Excel 97-2003**: .xls (legacy support)
- **Multiple Sheets**: Supported, will use first sheet by default

**Excel Example Structure**:
```
Sheet1: "Social_Listening_Data"
Row 1: Headers
Row 2+: Data

Optional Sheets:
- "Metadata": Data source information
- "Dictionary": Field definitions
- "Summary": Pre-calculated metrics
```

**Excel Best Practices**:
- Use the first sheet for main data
- Avoid merged cells in data area
- Use standard date formatting
- Remove empty rows and columns
- Keep formatting simple (no complex styling)

---

## 📝 Data Templates

### Basic Template

**Minimum Viable Dataset**:
```csv
Date,Brand,Country,Mentions,Sentiment
2024-01-01,BrandA,USA,125,Positive
2024-01-01,BrandA,UK,87,Neutral
2024-01-01,BrandA,Canada,156,Positive
2024-01-02,BrandA,USA,134,Neutral
2024-01-02,BrandA,UK,92,Negative
```

### Standard Template

**Recommended Dataset Structure**:
```csv
Date,Year,Quarter,Month,Brand,Country,Type,Type_Detail,Contact_Way,Mentions,Engagement,Reach,Sentiment,Keywords,Campaign
2024-01-15,2024,Q1,January,BrandA,USA,Social,Facebook,Organic,150,1250,15000,Positive,"running shoes,fitness",Summer2024
2024-01-15,2024,Q1,January,BrandA,USA,Social,Instagram,Paid,89,756,8900,Neutral,"athletic wear,sport",Summer2024
2024-01-15,2024,Q1,January,BrandB,UK,News,BBC,Organic,45,890,23400,Negative,"controversy,issues",Crisis2024
```

### Advanced Template

**Enterprise Dataset Structure**:
```csv
Date,Year,Quarter,Month,Brand,Country,Region,City,Type,Type_Detail,Platform,Contact_Way,Mentions,Engagement,Reach,Impressions,Clicks,Shares,Comments,Likes,Sentiment,Sentiment_Score,Emotion,Keywords,Hashtags,Campaign,Campaign_Type,Influencer_Tier,Influencer_Name,Cost,Cost_Currency
```

---

## 🔍 Data Validation Rules

### Required Field Validation

**Date Field**:
- Must be valid date format
- Supported formats: YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY, MM-DD-YYYY
- No future dates beyond current date
- No dates before 2000-01-01

**Numeric Fields**:
- Must contain only numbers (integers or decimals)
- No negative values for counts (mentions, engagement, reach)
- Reasonable ranges (mentions: 1-1,000,000)

**Text Fields**:
- Maximum length: 255 characters per field
- No HTML tags or special formatting
- Consistent naming conventions

### Data Quality Checks

**Completeness Check**:
```python
# Required fields must have values
required_fields = ['Date', 'Brand', 'Country', 'Mentions', 'Sentiment']
# Check for missing values in required columns
```

**Consistency Check**:
```python
# Brand names should be consistent
# Country names should use standard format
# Sentiment values must be: Positive, Neutral, Negative
```

**Range Validation**:
```python
# Mentions: 1 to 1,000,000
# Engagement: 0 to 10,000,000  
# Sentiment_Score: -1.0 to 1.0
# Reach: 0 to 100,000,000
```

---

## 📊 Sample Data Sets

### Demo Dataset 1: Multi-Brand Comparison
```csv
Date,Brand,Country,Type,Type_Detail,Mentions,Engagement,Sentiment
2024-01-01,Nike,USA,Social,Instagram,245,2100,Positive
2024-01-01,Adidas,USA,Social,Instagram,189,1750,Positive
2024-01-01,Puma,USA,Social,Instagram,123,980,Neutral
2024-01-01,Nike,UK,Social,Facebook,156,1200,Positive
2024-01-01,Adidas,UK,Social,Facebook,134,1050,Neutral
```

### Demo Dataset 2: Campaign Analysis
```csv
Date,Brand,Country,Campaign,Campaign_Type,Mentions,Engagement,Sentiment,Cost
2024-01-01,BrandX,USA,SpringLaunch,Product,125,1200,Positive,5000
2024-01-02,BrandX,USA,SpringLaunch,Product,156,1450,Positive,5000
2024-01-03,BrandX,USA,SpringLaunch,Product,189,1680,Positive,5000
2024-01-04,BrandX,USA,SpringLaunch,Product,134,1320,Neutral,5000
```

### Demo Dataset 3: Geographic Analysis
```csv
Date,Brand,Country,Region,City,Mentions,Engagement,Sentiment
2024-01-01,GlobalBrand,USA,North America,New York,89,750,Positive
2024-01-01,GlobalBrand,USA,North America,Los Angeles,76,680,Positive
2024-01-01,GlobalBrand,UK,Europe,London,123,980,Neutral
2024-01-01,GlobalBrand,France,Europe,Paris,67,590,Positive
2024-01-01,GlobalBrand,Germany,Europe,Berlin,45,420,Negative
```

---

## ⚡ Optimization Tips

### Performance Optimization

**Data Size Management**:
- **Optimal Size**: 1,000-10,000 rows for best performance
- **Maximum Size**: 100,000 rows (may experience slowdown)
- **Large Datasets**: Consider data sampling or aggregation

**Column Optimization**:
- Include only necessary columns
- Use consistent data types
- Avoid excessive text fields
- Pre-calculate derived metrics when possible

### Data Preparation Best Practices

**Pre-Processing Steps**:
1. **Remove Duplicates**: Check for duplicate records
2. **Standardize Names**: Use consistent brand/country names
3. **Clean Text**: Remove special characters and HTML
4. **Validate Dates**: Ensure consistent date formats
5. **Check Ranges**: Verify numeric values are reasonable

**Data Cleaning Checklist**:
- [ ] All required columns present
- [ ] No empty rows or columns
- [ ] Consistent date formats
- [ ] Valid sentiment values
- [ ] Numeric fields contain only numbers
- [ ] Brand names standardized
- [ ] Country names consistent
- [ ] File size within limits

### Common Data Issues

**Issue**: Date format inconsistencies
```csv
# Problem:
Date
01/15/2024
15-01-2024
2024-01-15

# Solution: Use consistent format
Date
2024-01-15
2024-01-15
2024-01-15
```

**Issue**: Inconsistent brand names
```csv
# Problem:
Brand
Nike
NIKE
nike
Nike Inc.

# Solution: Standardize naming
Brand
Nike
Nike
Nike
Nike
```

**Issue**: Invalid sentiment values
```csv
# Problem:
Sentiment
Good
Bad
OK
Excellent

# Solution: Use standard values
Sentiment
Positive
Negative
Neutral
Positive
```

---

## 📋 Data Dictionary

### Standard Field Definitions

**Core Metrics**:
- **Mentions**: Total number of brand mentions across all sources
- **Engagement**: Total interactions (likes, comments, shares, clicks)
- **Reach**: Unique audience size exposed to content
- **Impressions**: Total number of times content was displayed

**Calculated Metrics**:
- **Engagement Rate**: (Engagement ÷ Reach) × 100
- **Share of Voice**: (Brand Mentions ÷ Total Market Mentions) × 100
- **Sentiment Ratio**: Positive Mentions ÷ (Positive + Negative Mentions)

**Derived Fields**:
- **Week**: Calculated from Date field
- **Day of Week**: Monday, Tuesday, etc.
- **Time Period**: Morning, Afternoon, Evening (if timestamp available)

### Industry-Specific Schemas

**Retail/E-commerce**:
```csv
Date,Brand,Product_Category,Channel,Mentions,Sales_Impact,Sentiment
```

**Technology**:
```csv
Date,Brand,Product,Feature,Platform,Mentions,Sentiment,Bug_Reports
```

**Healthcare/Pharma**:
```csv
Date,Brand,Product,Indication,Source_Type,Mentions,Sentiment,Adverse_Events
```

---

## 🚀 Getting Started with Your Data

### Step-by-Step Data Preparation

1. **Export from Social Listening Tool**:
   - Export data from your monitoring platform
   - Choose CSV or Excel format
   - Include all relevant time periods

2. **Format Validation**:
   - Open file in spreadsheet application
   - Check column headers match requirements
   - Verify data types and formats

3. **Data Cleaning**:
   - Remove empty rows and columns
   - Standardize text values
   - Validate date formats
   - Check for missing required fields

4. **Upload and Test**:
   - Upload a small sample first (100-500 rows)
   - Verify data loads correctly
   - Check visualizations display properly
   - Upload full dataset once validated

### Quick Validation Checklist

Before uploading your data:
- [ ] File format is CSV or Excel
- [ ] All required columns present
- [ ] Date column uses consistent format
- [ ] Numeric columns contain only numbers
- [ ] Sentiment uses standard values
- [ ] No HTML or special formatting
- [ ] File size under 50MB
- [ ] Brand names are consistent

---

**Ready to upload your data?** Return to the [User Guide](user-guide.md) to start your analysis!