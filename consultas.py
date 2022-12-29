
import sqlite3
import re

def cuenta_exp():
    conn=sqlite3.connect('alertas.s3db')
    c=conn.cursor()
    c.execute("SELECT COUNT(estado)FROM ingresos WHERE estado='N'")
    cuentas=c.fetchone()
    return cuentas
    conn.close()

def expedientes():
    conn=sqlite3.connect('alertas.s3db')
    c=conn.cursor()
    c.execute("SELECT nexp FROM ingresos ")
    exp=c.fetchall()
    return exp
    conn.close()

def fecha():
    conn=sqlite3.connect('alertas.s3db')
    c=conn.cursor()
    c.execute("SELECT fechaingreso FROM ingresos ")
    exp=c.fetchall()
    return exp
    conn.close()

def obtenerExp():    
    expediente=expedientes()
    exp='<br>'.join(map(str,expediente))
    ex=exp.replace('(', '')
    ex=ex.replace(')','')
    ex=ex.replace(',','')
    return ex

def especialista():
    conn=sqlite3.connect('alertas.s3db')
    c=conn.cursor()
    c.execute("SELECT especialista FROM ingresos ")
    exp=c.fetchone()
    esp= ','.join(str(v) for v in exp)
    nesp=re.sub(r'.', '', esp, count = 1)
    return nesp

