
import jinja2
from xhtml2pdf import pisa

"""

df = pd.DataFrame({
    "Common Resistor Vaules": ["100R", "220R", "470R", "680R", "1.0K", "2.2K", "1.2K", "3.3K", "4.7K", "2.0K", "10K",
                               "11K", "15K", "16K", "18K", "20K", "22K", "24K", "27K", "33K", "47K", "68K", "110K",
                               "150K", "220K", "300K", "470K", "680K", "1.0M", "1.2M", "10.0M"],

    "All Capacitor Values": ["10pF", "12pF", "15pF", "18pF", "22pF", "27pF", "33pF", "39pF", "47pF", "56pF", "68pF",
                             "82pF", "100pF", "120pF", "150pF", "180pF", "220pF", "270pF", "330pF", "390pF", "470pF",
                             "560pF", "680pF", "820pF", "1000pF", "1200pF", "1500pF", "1800pF", "2200pF", "2700pF",
                             "3300pF", "3900pF", "4700pF", "5600pF", "6800pF", "8200pF", ".010mF", ".012mF", ".015mF",
                             ".018mF", ".022mF", ".027mF", ".033mF", ".039mF", ".047mF", ".056mF", ".068mF", ".082mF",
                             ".10mF", ".12mF", ".15mF", ".18mF", ".22mF", ".27mF", ".33mF", ".39mF", ".47mF", ".56mF",
                             ".68mF", ".82mF", "1.0mF", "1.2mF", "1.5mF", "1.8mF", "2.2mF", "2.7mF", "3.3mF", "3.9mF",
                             "4.7mF", "5.6mF", "6.8mF", "8.2mF", "10mF", "22mF", "33mF", "47uF"]
})
"""

dimensions = {"75x55": [75, 55], "80x65": [80, 65], "100x75": [100, 75]}

components = {"Capacitors": ["10pF", "12pF", "15pF", "18pF", "22pF", "27pF", "33pF", "39pF", "47pF", "56pF", "68pF",
                             "82pF", "100pF", "120pF", "150pF", "180pF", "220pF", "270pF", "330pF", "390pF", "470pF",
                             "560pF", "680pF", "820pF", "1000pF", "1200pF", "1500pF", "1800pF", "2200pF", "2700pF",
                             "3300pF", "3900pF", "4700pF", "5600pF", "6800pF", "8200pF", ".010mF", ".012mF", ".015mF",
                             ".018mF", ".022mF", ".027mF", ".033mF", ".039mF", ".047mF", ".056mF", ".068mF", ".082mF",
                             ".10mF", ".12mF", ".15mF", ".18mF", ".22mF", ".27mF", ".33mF", ".39mF", ".47mF", ".56mF",
                             ".68mF", ".82mF", "1.0mF", "1.2mF", "1.5mF", "1.8mF", "2.2mF", "2.7mF", "3.3mF", "3.9mF",
                             "4.7mF", "5.6mF", "6.8mF", "8.2mF", "10mF", "22mF", "33mF", "47uF"],

              "Resistors": ["100R", "220R", "470R", "680R", "1.0K", "2.2K", "1.2K", "3.3K", "4.7K", "2.0K", "10K",
                            "11K", "15K", "16K", "18K", "20K", "22K", "24K", "27K", "33K", "47K", "68K", "110K",
                            "150K", "220K", "300K", "470K", "680K", "1.0M", "1.2M", "10.0M"]
              }

for component_key, component_value in components.items():
    for dimension_key, dimension_value in dimensions.items():
        html = jinja2.Environment(  # Pandas DataFrame to HTML
            loader=jinja2.FileSystemLoader(searchpath='')).get_template(
            'ee_card_template.html').render(df=component_value, width=dimension_value[0], height=dimension_value[1])

        # Convert HTML to PDF
        with open('report_%s_%s.pdf' % (component_key, dimension_key), "w+b") as out_pdf_file_handle:
            pisa.CreatePDF(
                src=html,
                dest=out_pdf_file_handle)