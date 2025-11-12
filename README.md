# 📊 Adidas Sales Dashboard

An interactive data visualization dashboard built with Streamlit to analyze Adidas sales data across different retailers, regions, and time periods.

##Dataset

**Kaggle Dataset**

## 🎯 Features

- **Real-time Sales Analytics**: Interactive visualizations of Adidas sales data
- **Multiple Chart Types**: 
  - Bar charts for retailer comparison
  - Line graphs for time-series analysis
  - Dual-axis charts for sales vs units sold
  - Treemap for regional and city-level insights
- **Data Export**: Download filtered data as CSV files
- **Responsive Design**: Wide layout optimized for desktop viewing
- **Interactive Filters**: Expandable sections to view detailed data

## 📸 Dashboard Sections

### 1. Total Sales by Retailers
Bar chart showing sales performance across different retail partners (Foot Locker, Walmart, Sports Direct, West Gear, Kohl's, Amazon).

### 2. Total Sales Over Time
Line chart tracking sales trends over months and years.

### 3. Sales and Units Sold by State
Dual-axis chart comparing total sales (bars) with units sold (line) across different states.

### 4. Regional and City Analysis
Interactive treemap showing sales distribution across regions and cities.

## 🚀 Live Demo

[View Live Dashboard](https://your-deployed-app-url.streamlit.app)

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **PIL (Pillow)**: Image handling
- **Python**: Backend programming

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/adidas-sales-dashboard.git
cd adidas-sales-dashboard
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

## 📦 Requirements

Create a `requirements.txt` file with:
```txt
streamlit==1.28.0
pandas==2.1.0
openpyxl==3.1.2
plotly==5.17.0
pillow==10.0.0
```

## 🎮 Usage

1. **Run the application**
```bash
streamlit run app.py
```

## 📁 Project Structure
```
adidas-sales-dashboard/
│
├── app.py                  # Main application file
├── Adidas.xlsx            # Sales data (Excel file)
├── adidas_logo.webp       # Company logo
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## 📊 Data Format

The dashboard expects an Excel file (`Adidas.xlsx`) with the following columns:
- `Retailer`: Name of the retail partner
- `InvoiceDate`: Date of sale
- `TotalSales`: Total sales amount
- `UnitsSold`: Number of units sold
- `State`: US state
- `Region`: Geographic region
- `City`: City name

## 🎨 Customization

### Modify Colors
Edit the Plotly template in `app.py`:
```python
template='gridon'  # Options: 'plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn'
```

## 🚀 Deployment

### Deploy to Streamlit Cloud

## 📝 To-Do / Future Enhancements

- [ ] Add date range filters
- [ ] Implement user authentication
- [ ] Add more chart types (pie charts, heatmaps)
- [ ] Export dashboard as PDF
- [ ] Add real-time data refresh
- [ ] Mobile responsive design
- [ ] Dark mode toggle

## 👤 Author

**Andile Ntshangase**
- Email: vuyiswaandile176@gmail.com

## 🙏 Acknowledgments

- Adidas for the inspiration
- Streamlit community for excellent documentation
- Plotly for powerful visualization tools

⭐ **i keep motivated by developing new skills** ⭐

Made with ❤️ and Python
