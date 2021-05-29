import os, datetime
import json, base64
import time, requests
from io import BytesIO
from selenium import webdriver

def send_devtools(driver, cmd, params={}):
        try:
            resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
            url = driver.command_executor._url + resource
            body = json.dumps({'cmd': cmd, 'params': params})
            response = driver.command_executor._request('POST', url, body)
            if (response.get('value') is not None):
                return response.get('value')
            else:
                return None
        except Exception as e:
            print("Error in function send_devtools ", e)
            


def save_as_pdf(driver, path, options={}):
        try:
            result = send_devtools(driver, "Page.printToPDF", options)
            if (result is not None):
                with open(path, 'wb') as file:
                    file.write(base64.b64decode(result['data']))
                return True
            else:
                return False
        except Exception as e:
            print("Error in function save_as_pdf", e)
            
            
def make_sure_path_exists(pdfFolder):
    try:
        os.makedirs(pdfFolder)
    except OSError as exception:
        pass

def htmlTopdf1(driver,url,r,item):
        try:        
            #Folder_Name =  date.today().strftime("%d_%m_%Y")
            Folder_Name =  '22-Mar-2021'
            pdfFolder = os.path.join(r, Folder_Name)
            print("Pdf Folder :", pdfFolder)
            make_sure_path_exists(pdfFolder)
            r=requests.get(url)
            if r.status_code != 200:
                print("Issue: PDF not generated")
                return False
            driver.get(url)
            driver.execute_script("document.body.style.zoom='100%'")
            time.sleep(3)
            pdf_name = "test.pdf"
            name = os.path.join(pdfFolder,pdf_name)
            val = save_as_pdf(driver, name, {'pageRanges':'1-5', 'preferCSSPageSize': True, 'marginTop': 0, 'marginBottom': 0, 'marginLeft': 0, 'marginRight': 0, 'landscape': False, 'printBackground': True})
        except Exception as e:
            print("Issue: PDF not generated in ", e)
            return False
        return True 

def createPDF1():
    today=datetime.date.today()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1600,1000)
    url = 'http://127.0.0.1:5000/dash-financial-report/full-view'
    prt = htmlTopdf1(driver,url,os.path.join('reports'),{"id":1,"Date":today.strftime("%d_%m_%Y")})
    driver.quit()
    

        