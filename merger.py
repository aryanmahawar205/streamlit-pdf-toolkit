from PyPDF2 import PdfMerger

# Initialize PdfMerger object
merger = PdfMerger()

# Specify the paths to your PDF files
pdf_file1 = 'file1.pdf'
pdf_file2 = 'file2.pdf'

# Append the PDFs to the merger object
merger.append(pdf_file1)
merger.append(pdf_file2)

# Write the merged PDF to a new file
merger.write('merged_output.pdf')

# Close the merger object to save the file
merger.close()

print("PDFs merged")
