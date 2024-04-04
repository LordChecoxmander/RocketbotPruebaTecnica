from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook

#configuracion de selenium webdriver
driver = webdriver.Chrome()
driver.get("https://roc.myrb.io/s1/forms/M6I8P2PDOZFDBYYG")

#abro el archivo xlsx, extraigo los datos y luego lo cierro
file = "./Base Seguimiento Observ Auditoría al_30042021.xlsx"
wb = load_workbook(file)
sheet = wb.active
wb.close()

def completeForm(row):
#Proceso 1 | observacion  2| tipo de riesgo 3| severidad 4| plan accion 5| Fecha compromiso 6| resonsabre 7| Area Res 8| correo Res  9| estado 10 -> -1
    #subir proceso
    driver.find_element("id", "process").send_keys(row[0].value)
    print("process "+row[0].value)

    #subir tipo de riesgo
    driver.find_element("id", "tipo_riesgo").send_keys(row[2].value)
    print("tipo_riesgo "+ row[2].value)

    #subir severidad
    driver.find_element("id", "severidad").send_keys(row[3].value)
    print("severidad "+ row[3].value)

    #subir Responsable
    driver.find_element("id", "res").send_keys(row[6].value)
    print("res "+ row[7].value)

    #subir Fecha Compormiso
    date_com = row[5].value.strftime("%m/%d/%Y")
    driver.find_element("id", "date").send_keys(date_com)
    
    #subir observacion
    driver.find_element("id", "obs").send_keys(row[1].value)
    print("obs "+ row[1].value)

    #clikear el submit
    driver.find_element("id", "submit").click()

def enviarCorreo():
    a = 1



for row in sheet.iter_rows(min_row=2, max_row=3, max_col=10):
    #evaluo la columna "J"(estado)
    print("estado: "+ row[9].value)
    match str.lower(row[9].value):
        case "regularizado":
            print("subir la información al formulario")
            completeForm(row)
        case "atrasado":
            print(", enviar un mail ")
            enviarCorreo()
        case 'pendiente':
            #en este caso debe ser ignorado
            continue

    print('--- linea ---')



a = input("ingresa algo")