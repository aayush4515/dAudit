import tabula
import pandas as pd

file_path = '/Users/aayush/Desktop/Projects/dAudit/test.pdf'
output_path = '/Users/aayush/Desktop/Projects/dAudit/output.xlsx'

# # Converts PDF table to an Excel File
def convert_pdf_to_excel(pdf_path, output_path):
    # Use `pages` parameter as 'all' to convert all pages or specify pages like '1,2,3'
    dfs = tabula.read_pdf(pdf_path, pages='1')

    # Check if any dataframes were extracted
    if not dfs:
        print("No tables found in the PDF.")
        return

    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        for i, df in enumerate(dfs):
            df.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)

# Example usage to convert PDF to Excel.
convert_pdf_to_excel(file_path, output_path)
