from app.server import AppServer
from app.dashFinReport import app
from app.printpdf import createPDF1
from flask import render_template, flash, redirect, url_for, request, g , current_app
#from app import server
#from flask import g
#from flask_babel import _, get_locale




@AppServer.route('/', methods=['GET', 'POST'])
@AppServer.route('/index', methods=['GET', 'POST'])
def index():
    return redirect('/app/dashFinReport') 	
    
@AppServer.route('/printReport', methods=['GET', 'POST'])    
def print():
    result = createPDF1()
    return redirect('/index') 	
	
	   	
        
   
