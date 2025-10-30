# Quick Start Guide

## Immediate Testing with Sample Data

The project includes sample data files for immediate testing:

### 1. Sample Database (sample_data.db)

A SQLite database with a complete e-commerce schema:

**Tables:**
- `customers` - Customer information
- `products` - Product catalog
- `orders` - Order records
- `order_items` - Order line items
- `reviews` - Product reviews

**To test:**
1. Launch the application: `python metadata_crawler.py`
2. Go to the "Database" tab
3. Click "Browse SQLite File" and select `sample_data.db`
4. Click "Crawl Database"
5. Click "Generate Data Dictionary" to see all fields
6. Click "View Lineage Map" to see table relationships

### 2. Sample CSV File (sample_employees.csv)

Employee data with columns:
- employee_id, first_name, last_name
- department, salary, hire_date, email

**To test:**
1. Go to the "Files" tab
2. Click "Add Files" and select `sample_employees.csv`
3. Click "Crawl Files"
4. View results in "Data Dictionary" tab

### 3. Sample JSON File (sample_api_response.json)

API response structure with nested user data

**To test:**
1. Go to the "Files" tab
2. Click "Add Files" and select `sample_api_response.json`
3. Click "Crawl Files"
4. View the extracted schema

## Testing API Crawling

Use a public API for testing:

**Example - JSONPlaceholder API:**
1. Go to the "API" tab
2. Enter URL: `https://jsonplaceholder.typicode.com/users`
3. Leave headers empty (no auth needed)
4. Click "Crawl API"

## Complete Workflow Test

1. **Crawl all sources:**
   - Crawl the sample database
   - Add and crawl both sample files
   - Crawl the test API

2. **Generate comprehensive report:**
   - Click "Generate Data Dictionary"
   - Review all 50+ fields from all sources
   - Click "View Lineage Map"

3. **Export results:**
   - Click "Export to Excel"
   - Save as `metadata_report.xlsx`
   - Open in Excel to see 3 sheets:
     - Data Dictionary
     - Metadata Summary
     - Lineage Map

4. **Monitor progress:**
   - Watch the "Activity Log" tab for real-time updates
   - Check "Statistics" tab for counts

## Expected Results

After crawling all sample data:
- **Database**: 5 tables, ~25 columns
- **CSV file**: 1 file, 7 columns
- **JSON file**: ~15 nested fields
- **API** (if tested): Variable fields

**Total**: ~50+ metadata entries across all sources

## File Locations

All files in `/home/claude/`:
- `metadata_crawler.py` - Main application
- `sample_data.db` - Sample database
- `sample_employees.csv` - Sample CSV
- `sample_api_response.json` - Sample JSON
- `create_sample_db.py` - Database generator
- `requirements.txt` - Dependencies
- `README.md` - Full documentation

## Next Steps

1. Test with your own data sources
2. Crawl multiple databases
3. Add production APIs with authentication
4. Export reports for documentation
5. Use for data governance and compliance

## Troubleshooting

**Application won't start:**
```bash
python3 metadata_crawler.py
```

**Missing dependencies:**
```bash
pip install -r requirements.txt --break-system-packages
```

**Can't find sample files:**
- All sample files are in the same directory as the application
- Use absolute paths if needed

## Quick Commands

```bash
# Create fresh sample database
python create_sample_db.py

# Run application
python metadata_crawler.py

# Check Python version (need 3.8+)
python --version
```

Enjoy exploring your metadata!
