import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

def latex_to_png(latex_str):
	fig = plt.figure(figsize=(4, 0.5))
	plt.axis("off")
	plt.text(0.0,0.0,f"${latex_str}$",size=30,ha="center",va="center")
	pdf_path = "result.pdf"
	png_path = "result.png"
	plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.0)
	plt.close()
	images = convert_from_path(pdf_path)
	images[0].save(png_path, "PNG")



latex_to_png("\\theta = atan(\\frac{opp}{adj})")




