from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import consultas
import extras
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///alertas.s3db'
db=SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def enviar():
    now = datetime.now()
    resultado=extras.current_date_format(now)


    cuenta=consultas.cuenta_exp()
    values = ','.join(str(v) for v in cuenta)
    expedient=consultas.obtenerExp()
    fecha=consultas.fecha()
    espe=consultas.especialista()
     

    fc='<BR>'.join(map(str,fecha))

    username="rariasbe@pj.gob.pe"
    password=request.form
    ps=password.get('contrasena')
    destinatario=request.form
    de=destinatario.get('destinatario')
    

    
    asunto=(f"""Ingresos al {resultado}""")

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"]=asunto
    mensaje["From"]="BotAlertasSSED"
    mensaje["To"]=de

    html= f"""
<html>
<body>
<p><font size=6> Dr(a). {espe} Usted posee <b>{values}</b> escritos en estado pendiente de proveer.</font><br>
 Los Expedientes son los siguiente:<br>
 <table>
    <tr>
        <td><b>Expediente</b></td>
        <td>          </td>
        <td><b>Fecha de Ingreso</b></td>
    </tr>
  <tr>

    <td>{expedient}</td>
    <td>======></td>
    <td>{fc}</td>

  </tr>
 
 </table>
 
</body>
</html>"""

    parte_html = MIMEText(html,"html")
    mensaje.attach(parte_html)
    context= ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
     server.login(username,ps)
     server.sendmail("BotAlertasSSED",de,mensaje.as_string())
    return "enviado"


if __name__=='__main__':
    app.run(debug=True) 


