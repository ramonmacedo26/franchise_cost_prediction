# Franchise Cost Prediction

This project predicts the initial cost of a franchise based on annual frequency using a linear regression model.

## Structure
- **data/**: Contains the dataset (`slr12.csv`).
- **app/**: Contains the main Streamlit application (`main.py`).
- **notebooks/**: Jupyter notebooks for data analysis (if needed).

## How to Run
1. Clone this repository.
2. Navigate to the `app` directory and run the Streamlit app:
    ```bash
    streamlit run main.py
    ```
3. Upload your dataset or use the example provided in the `data/` folder.

## Example Dataset
The example dataset (`slr12.csv`) contains two columns:
- `FrqAnual`: Annual Frequency
- `CusInic`: Initial Cost
