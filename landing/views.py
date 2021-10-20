from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.

 
def PDF_Viewer(request, pk):
    filepath = os.path.join('static/pdf', pk + ".pdf")
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def Index(request):

    descs = ["A Senior Data Engineering undergraduate student with an interest in all data-related subjects. Always eager to learn and seek new challenges to improve my skills.",
            "Current data engineering student, willing to learn new things related to the world of programming and data analysis, bussines intelligence and data science.",
            "I am currently a data engineering student, passionate to learn about ML, Deep Learning, DevOps, and other technologies. I would like to find a company",
            "A Senior Data Engineering student interested on any data related topics. An special interest on automation, videogames and simulations. Willing to take challanges."
    ]

    args = {
        'name_1': 'Jorge Aque',
        'role_1': 'QA',
        'desc_1': descs[1],
        'img_1': 'foca.png',
        'pdf_1':'JA',
        'name_2': 'Jorge Erosa',
        'role_2': 'CEO of RichIt',
        'desc_2': descs[0],
        'img_2': 'fumadora.png',
        'pdf_2':'JE',
        'name_3': 'Daniel Danilo',
        'role_3': 'Amazon Web Slave',
        'desc_3': descs[2],
        'img_3': '2.jpg',
        'pdf_3':'DD',
        'name_4': 'Jack Robles',
        'role_4': 'Not legal, probably',
        'desc_4': descs[3],
        'img_4': 'halo2.png',
        'pdf_4':'JR',
        'pdfUrl':'pdf-url'
    }

    return render(request, 'index.html', args)