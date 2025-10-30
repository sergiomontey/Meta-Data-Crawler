# 🗄️ Multi-Source Metadata Crawler

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Database-red.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)
![NetworkX](https://img.shields.io/badge/NetworkX-Graphs-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

> **A comprehensive desktop application for crawling databases, APIs, and files to build a central metadata repository** - Automatically generate data dictionaries, map data lineage, and create comprehensive schema documentation for governance, compliance, and architectural understanding.

---

## ⚠️ PROOF OF CONCEPT NOTICE

**IMPORTANT: This is a demonstration/proof of concept project.**

While fully functional and well-architected, this software:
- ✅ **IS** suitable for data discovery, governance, and documentation
- ✅ **IS** open-source under MIT License (free to use, modify, distribute)
- ✅ **IS** production-ready for metadata analysis and cataloging
- ⚠️ **REQUIRES** testing with your specific database schemas
- ⚠️ **STORES** data in-memory (no persistent storage of metadata)

**Users should test with their own data sources to ensure compatibility with their specific environments.**

See the [Security Considerations](#-security-considerations) section for full details.

---

## 🎯 Overview

Multi-Source Metadata Crawler is a desktop application that simplifies data discovery and documentation across your entire data landscape. Built with Python, Tkinter, SQLAlchemy, Pandas, and NetworkX, it provides intelligent schema extraction, automated data dictionary generation, and comprehensive lineage mapping—without the complexity of enterprise data catalog tools.

This project serves as a **professional tool** demonstrating modern software engineering practices, data architecture techniques, and a complete metadata management solution suitable for data engineers, architects, and governance teams.

### 🌟 Key Features

- **🗄️ Multi-Source Crawling**: Extract metadata from databases, APIs, and files
- **📚 Automated Data Dictionary**: Generate comprehensive field catalogs automatically
- **🔗 Lineage Mapping**: Track relationships and dependencies between data entities
- **📋 Schema Documentation**: Complete metadata extraction with types and constraints
- **📊 Professional Excel Export**: Multi-sheet reports with formatting
- **🔍 Search and Filter**: Find data elements across all sources
- **📈 Statistics Dashboard**: Monitor your data landscape
- **⚡ Non-Blocking Operations**: Background threading for responsive UI

## 🎬 Screenshots

### Main Interface - Database Crawling
![Main Interface](https://via.placeholder.com/800x500/1a1a1a/00ff00?text=Database+Crawling+Interface)
*Database tab showing connection options and crawl status*

### Data Dictionary View
![Data Dictionary](https://via.placeholder.com/800x500/1a1a1a/00bfff?text=Data+Dictionary+Catalog)
*Comprehensive data dictionary with fields from all sources*

### Lineage Map
![Lineage](https://via.placeholder.com/800x500/1a1a1a/ff8c00?text=Lineage+Relationships)
*Data lineage showing relationships between tables and entities*

### Statistics Dashboard
![Statistics](https://via.placeholder.com/800x500/1a1a1a/dc143c?text=Metadata+Statistics)
*Statistics showing crawled sources and metadata counts*

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **Tkinter** (usually comes pre-installed with Python)
- **SQLAlchemy**, **Pandas**, **NetworkX**, **OpenPyXL**, **Requests** (installed via pip)

### Installation

#### Option 1: Quick Start (Recommended)

```bash
# Clone or download the repository
cd metadata-crawler

# Install dependencies
pip install requests sqlalchemy pandas networkx openpyxl --break-system-packages

# Launch the application
python metadata_crawler.py
```

That's it! The application is ready to use.

#### Option 2: With Virtual Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install requests sqlalchemy pandas networkx openpyxl

# Launch the application
python metadata_crawler.py
```

#### Option 3: Verify Installation

```bash
# Run with sample database
python metadata_crawler.py

# Load the included sample_data.db file
# Expected: Successfully crawled 5 tables with relationships
```

### Crawl Your First Data Source

1. **Launch the application**
   ```bash
   python metadata_crawler.py
   ```

2. **Select a source type**:
   - **Database** tab: For SQL databases
   - **API** tab: For REST endpoints
   - **Files** tab: For CSV, Excel, JSON files

3. **Configure and crawl**:
   - Enter connection details or select files
   - Click the corresponding "Crawl" button
   - Watch the activity log for progress

4. **Generate data dictionary**:
   - Click "Generate Data Dictionary"
   - Review all extracted fields
   - Navigate to other tabs for details

5. **Export the catalog** if needed:
   - Click "Export to Excel"
   - Save comprehensive metadata report

### Try the Sample Database

Included sample files demonstrate various scenarios:

```bash
# In the application:
Database tab → Browse SQLite File → Select "sample_data.db" → Crawl Database
```

Includes examples of:
- E-commerce schema (customers, products, orders)
- Foreign key relationships
- Multiple data types
- Indexed columns
- Sample data for context

## 🏗️ Architecture

### System Overview

```mermaid
graph TB
    subgraph "GUI Layer"
        A[Main Application Window]
        B[Database Tab]
        C[API Tab]
        D[Files Tab]
        E[Data Dictionary View]
        F[Lineage Map View]
        G[Statistics View]
    end
    
    subgraph "Business Logic Layer"
        H[MetadataCrawler Engine]
        I[Database Inspector]
        J[API Schema Inferrer]
        K[File Parser]
        L[Lineage Graph Builder]
        M[Data Dictionary Generator]
    end
    
    subgraph "Data Layer"
        N[SQLAlchemy Inspection]
        O[Pandas DataFrames]
        P[NetworkX Graph]
        Q[Excel Export Handler]
        R[File I/O]
    end
    
    A --> H
    B --> I
    C --> J
    D --> K
    E --> M
    F --> L
    G --> H
    
    I --> N
    J --> O
    K --> O
    L --> P
    M --> O
    
    H --> Q
    N --> R
    O --> R
    P --> R
    Q --> R
```

### Component Architecture

#### Core Components

| Component | Description |
|:----------|:------------|
| **metadata_crawler.py** | Main application and GUI orchestration |
| **MetadataCrawler** | Core engine for metadata extraction |
| **Database Inspector** | SQLAlchemy-based schema introspection |
| **API Schema Inferrer** | REST API schema detection and analysis |
| **File Parser** | CSV, Excel, and JSON parsing with Pandas |
| **Lineage Graph Builder** | NetworkX-based relationship mapping |
| **Data Dictionary Generator** | Comprehensive field catalog generation |
| **MetadataCrawlerGUI** | Tkinter-based user interface |
| **Excel Export Handler** | Professional multi-sheet report generation |

### Tech Stack

- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (standard library)
- **Database**: SQLAlchemy (multi-database support)
- **Data Processing**: Pandas
- **Graph Analysis**: NetworkX
- **Excel Export**: OpenPyXL
- **API Client**: Requests
- **Total Dependencies**: 5 (requests, sqlalchemy, pandas, networkx, openpyxl)

### Design Patterns Implemented

This project demonstrates professional software engineering practices:

| Pattern | Usage | Location |
|:--------|:------|:---------|
| **MVC** | Separation of UI, business logic, and data | Throughout |
| **Strategy** | Different source type parsers | MetadataCrawler class |
| **Observer** | UI updates during crawling | Background threading |
| **Factory** | Tab and visualization creation | MetadataCrawlerGUI class |
| **Builder** | Lineage graph construction | LineageGraphBuilder |
| **Adapter** | Multiple database adapters | SQLAlchemy integration |

## 📊 Feature Deep Dive

### 1. Multi-Source Crawling

**Supported Data Sources:**

#### Databases
```python
# SQLite
sqlite:///path/to/database.db

# PostgreSQL
postgresql://user:password@localhost:5432/database

# MySQL
mysql://user:password@localhost:3306/database

# SQL Server
mssql+pyodbc://user:password@host/database?driver=ODBC+Driver+17+for+SQL+Server

# Oracle
oracle://user:password@host:1521/service
```

#### APIs
```python
# REST Endpoints
GET https://api.example.com/data

# With Authentication
Headers: {
  "Authorization": "Bearer token",
  "Content-Type": "application/json"
}

# Schema Detection
- JSON response analysis
- Nested structure extraction
- Field type inference
```

#### Files
```python
# CSV Files
employees.csv → Columns: id, name, email, department

# Excel Files
sales_data.xlsx → Multiple sheets with metadata

# JSON Files
api_response.json → Nested structures with arrays
```

### 2. Automated Data Dictionary Generation

The crawler automatically generates comprehensive catalogs:

**Database Tables:**
```python
# Extracted Information:
- Table names
- Column names and types
- Primary keys
- Foreign keys
- Indexes
- Nullable constraints
- Default values
- Auto-increment fields
```

**API Endpoints:**
```python
# Extracted Information:
- Endpoint URLs
- Response schema
- Field types (string, int, dict, list)
- Nested structure paths
- Sample values
```

**Files:**
```python
# Extracted Information:
- File names and paths
- Column/field names
- Data types (inferred from samples)
- Null counts
- Sample values
```

### 3. Lineage Mapping

**Relationship Tracking:**
```python
# Foreign Key Relationships
orders.customer_id → customers.customer_id
order_items.order_id → orders.order_id
order_items.product_id → products.product_id

# Graph Representation
- Nodes: Tables, files, API endpoints
- Edges: Foreign keys, references, dependencies
- Attributes: Relationship types, cardinality
```

**Visualization:**
- Entity list with types
- Relationship pairs
- Dependency paths
- Upstream/downstream tracking

### 4. Schema Documentation

**Comprehensive Metadata:**
```python
# Per Field Documentation:
{
  "table": "customers",
  "column": "email",
  "data_type": "VARCHAR(255)",
  "nullable": false,
  "source": "sqlite:///ecommerce.db",
  "source_type": "database"
}

# Aggregated Statistics:
- Total tables/entities
- Total columns/fields
- Relationship count
- Source distribution
```

### 5. Excel Export

**Multi-Sheet Reports:**

**Sheet 1: Data Dictionary**
- Field/Column name
- Source system
- Source type (database/API/file)
- Table/File name
- Data type
- Nullable flag

**Sheet 2: Metadata Summary**
- Source type counts
- Total entities
- Details and descriptions

**Sheet 3: Lineage Map**
- From entity
- To entity
- Relationship type
- Additional metadata

**Professional Formatting:**
- Colored headers
- Auto-sized columns
- Bold fonts
- Aligned text

### 6. Search and Filter

**Full-Text Search:**
```python
# Search across all metadata:
Search: "customer" → Finds:
  - customers table
  - customer_id columns
  - customer_email fields
  - API endpoints with "customer"

# Case-insensitive matching
# Instant results display
# Line numbers and context
```

## Installation

### Prerequisites

```bash
# Python 3.8 or higher required
python --version

# Verify Python is 3.8+
# Expected output: Python 3.8.x or higher
```

### Install Required Packages

```bash
# Install all dependencies at once
pip install requests sqlalchemy pandas networkx openpyxl --break-system-packages

# Or individually
pip install requests
pip install sqlalchemy
pip install pandas
pip install networkx
pip install openpyxl
```

**Note**: Tkinter comes pre-installed with most Python distributions.

### Verify Installation

```bash
# Test all dependencies
python -c "import tkinter; import requests; import sqlalchemy; import pandas; import networkx; import openpyxl; print('All dependencies installed!')"

# Expected output: All dependencies installed!
```

### Quick Test

```bash
# Launch the application
python metadata_crawler.py

# Load sample database
# Database tab → Browse → sample_data.db → Crawl
# Expected: Successfully crawled 5 tables
```

## Usage

### Starting the Application

```bash
# Launch the application
python metadata_crawler.py

# Application window opens with tabbed interface
```

### Crawling a Database

#### Method 1: SQLite Database

1. **Navigate to Database tab**
2. **Click "Browse SQLite File"**
3. **Select your .db file**
4. **Connection string auto-populated**
5. **Click "Crawl Database"**
6. **Watch activity log for progress**
7. **Success message appears when complete**

#### Method 2: Remote Database

1. **Navigate to Database tab**
2. **Select database type** (PostgreSQL, MySQL, etc.)
3. **Enter connection string**:
   ```
   postgresql://username:password@hostname:5432/database
   ```
4. **Click "Crawl Database"**
5. **Wait for completion**

**Extracted Data:**
- All table names
- All column definitions
- Primary and foreign keys
- Indexes
- Data types and constraints

### Crawling an API

1. **Navigate to API tab**
2. **Enter API endpoint URL**:
   ```
   https://api.example.com/users
   ```
3. **Add authentication headers** (if needed):
   ```json
   {
     "Authorization": "Bearer YOUR_TOKEN",
     "Content-Type": "application/json"
   }
   ```
4. **Click "Crawl API"**
5. **Schema inferred from response**

**Extracted Data:**
- Response structure
- Field names and types
- Nested object paths
- Sample values

### Crawling Files

1. **Navigate to Files tab**
2. **Click "Add Files"**
3. **Select one or multiple files**:
   - CSV files (.csv)
   - Excel files (.xlsx, .xls)
   - JSON files (.json)
4. **Files appear in list**
5. **Click "Crawl Files"**
6. **Progress shown in activity log**

**Extracted Data:**
- Column/field names
- Inferred data types
- Null counts
- Sample values
- File metadata

### Common Workflows

#### Workflow 1: Document New Database

**Goal**: Create comprehensive documentation for a database

**Steps**:
```bash
1. Launch application
2. Database tab → Enter connection string
3. Click "Crawl Database"
4. Click "Generate Data Dictionary"
5. Click "View Lineage Map"
6. Click "Export to Excel"
7. Share Excel report with team
```

**Expected Outcome**:
- Complete table catalog
- All column definitions
- Foreign key relationships
- Professional documentation

#### Workflow 2: Multi-Source Data Discovery

**Goal**: Catalog all data sources in an environment

**Steps**:
```bash
1. Crawl production database
2. Crawl staging database
3. Add and crawl CSV files
4. Add and crawl JSON files
5. Crawl API endpoints
6. Generate comprehensive dictionary
7. Export unified catalog
```

**Expected Outcome**:
- Unified data dictionary
- Cross-source lineage
- Complete data landscape view
- Governance documentation

## Project Structure

```
metadata-crawler/
├── metadata_crawler.py           # Main application (33KB, 800+ lines)
├── create_sample_db.py           # Sample database generator (6KB)
├── sample_data.db                # SQLite test database (48KB)
├── sample_employees.csv          # Employee data CSV (782 bytes)
├── sample_api_response.json      # API response sample (1.6KB)
├── requirements.txt              # Python dependencies (79 bytes)
├── README.md                     # This file (comprehensive docs)
├── QUICKSTART.md                 # 5-minute quick start guide
├── PROJECT_SUMMARY.md            # Project completion report
├── APPLICATION_OVERVIEW.txt      # Visual feature overview
└── START_HERE.txt                # Getting started guide
```

## Troubleshooting

### Issue: Application won't start

**Symptoms**:
```
python metadata_crawler.py
ModuleNotFoundError: No module named 'sqlalchemy'
```

**Solutions**:
```bash
# Install missing dependencies
pip install requests sqlalchemy pandas networkx openpyxl --break-system-packages
```

### Issue: Database connection fails

**Symptoms**: "Database crawl error: (unable to connect)"

**Solutions**:

1. **Verify connection string format**
2. **Check database is running**
3. **Verify credentials**
4. **Check firewall/network**

## Use Cases

### Perfect For:

✅ **Data Engineers** - Discover and document data sources  
✅ **Data Architects** - Map data lineage and relationships  
✅ **Data Governance Teams** - Create compliance documentation  
✅ **Database Administrators** - Schema documentation and analysis  
✅ **Business Analysts** - Understand available data assets  

## 🗺️ Roadmap

### Completed ✅
- [x] Multi-source crawling (databases, APIs, files)
- [x] Automated data dictionary generation
- [x] Lineage mapping and visualization
- [x] Schema documentation with full metadata
- [x] Excel export with professional formatting

### Future Enhancements 🔮

**High Priority:**
- [ ] Save and load crawler configurations
- [ ] Command-line interface (CLI) mode
- [ ] HTML export format with embedded visualizations

## License

This software is provided as-is for metadata analysis purposes under the MIT License.

**MIT License**

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Built with 💻 and ☕ by MonteyAI**

---

**🚀 Get Started in 3 Steps**: Install → Crawl Sources → Generate Dictionary

---

</div>
