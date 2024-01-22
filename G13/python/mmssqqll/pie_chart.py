import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Your data (replace this with your actual data)
sizes = [20, 30, 50]
labels = ['Small', 'Medium', 'Large']

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Save the plot to a BytesIO object
svg_output = BytesIO()
plt.savefig(svg_output, format='svg')
plt.close()

# Get the SVG data as a string
svg_data = svg_output.getvalue().decode('utf-8')

print(svg_data)

# You can save the SVG data to a file or embed it in HTML, etc.
# For example, if you're working with a web framework like Flask, you might pass this SVG data to your template.

# If you want to embed the SVG directly in an HTML file, you can use an <img> tag with a data URI:
# <img src="data:image/svg+xml;base64,SVG_DATA" alt="Pie Chart">
