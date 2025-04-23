
# 📅 CSV Date Filter - Interactive Google Colab Tool

This project provides a **user-friendly interface** to filter data from a `.csv` file by date, directly in **Google Colab**.  
Whether you're a data analyst, a researcher, or just cleaning up your dataset — this tool makes it easy, intuitive, and efficient.

---

## 🚀 Features

✅ Upload-free usage in Google Colab  
✅ Interactive **date input widget** (popup-style)  
✅ Filters your CSV based on an **exact date** (`dd/mm/yyyy`)  
✅ Saves a filtered version of your file  
✅ Shows progress and error messages for user guidance  
✅ Graceful handling of missing files or bad input  

---

## 🎯 How It Works

1. The user is prompted to enter a **target date**.
2. The script:
   - Loads the `file.csv` file
   - Cleans the `date` column (trims whitespace)
   - Converts strings to proper `datetime` format
   - Filters for rows matching the selected date
   - Saves the result as a new file like: `filtrado_01-02-2024.csv`
3. You get a success message and your clean file is ready!

---

## 🧪 Sample Output

```
✅ File 'filtrado_01-02-2024.csv' created successfully with 147 row(s).
```

---

## 📁 Requirements

- Python 3.x
- `pandas`
- `ipywidgets`
- Run the script **inside Google Colab**

To install the required packages in Colab:
```python
!pip install pandas ipywidgets
```

---

## 🔎 Why Use This?

This is perfect for:
- **Daily reports**
- **Filtering transaction logs**
- **Extracting dated records from exports**
- **Replacing Excel filtering with something faster and reproducible**

You can adapt the logic to support:
- Date **intervals**
- **Multiple formats**
- Other **filter conditions**

---

## 🤖 Example Use Case

You're given a massive CSV file of system logs.  
You only want the entries from `"12/03/2024"`.  
Just plug the date in — get a clean, filtered CSV. Done.

---

## 📬 Author

Made with ❤️ for productivity and clarity.  
Feel free to contribute or suggest improvements!

---

> “Filtering data shouldn't be hard — let the script do the heavy lifting.”
