import smtplib, subprocess, getpass, sys, time, platform
from datetime import datetime
from colorama import Fore as f, Back as b

SO = platform.system()

if SO == "Windows":
    comando_limpiar = "cls"
else:
    comando_limpiar = "clear"

subprocess.call(comando_limpiar, shell=True)

# ------------------------------------------------------------------------
# Banner de bienvenida de la herramienta/Banner of  welcome of the tool   
# ------------------------------------------------------------------------
def banner_inicio():
    print(f.GREEN+" ▅▅════════════════════════════════════════════▅▅")
    print(f.GREEN+"▐"+f.RED+"   ╔══╗───────────╔═╦═╗╔══╗╔══╗╔╗─────╔═╦╗╔═╗"+f.GREEN+"   ▋")
    print(f.GREEN+"▐"+f.RED+"   ║══╣╔═╗╔═╗─╔══╗║║║║║║╔╗║╚║║╝║║─╔══╗║║║║║╬║"+f.GREEN+"   ▋")
    print(f.GREEN+"▐"+f.RED+"   ╠══║║╬║║╬╚╗║║║║║║║║║║╠╣║╔║║╗║╚╗╚══╝║║║║║╗╣"+f.GREEN+"   ▋")
    print(f.GREEN+"▐"+f.RED+"   ╚══╝║╔╝╚══╝╚╩╩╝╚╩═╩╝╚╝╚╝╚══╝╚═╝────╚╩═╝╚╩╝"+f.GREEN+"   ▋")
    print(f.GREEN+"▐"+f.RED+"   ────╚╝─────────────────────────────────────  "+f.GREEN+"▋")
    print(f.GREEN+"▐▅▅════════════════════════════════════════════▅▅▋") 
    print(f.GREEN+" ║   "+f.YELLOW+"         [+]Creador:"+f.RED+" Not-Risks"+f.GREEN+"             ║")
    print(f.GREEN+" ╠══════════════════════════════════════════════╣")
    print(f.GREEN+" ║   "+f.YELLOW+"[+]Telegram:"+f.RED+" https://t.me/hackersAsperger"+f.GREEN+"  ║")
    print(f.GREEN+" ╚══════════════════════════════════════════════╝")
    print(f.RESET)


# --------------------------------------------------------------------------------------------------------------------------
# Elegir a que tipo de servicio de correo pertenece la víctima/To choose to that type of mail service the victim belongs     
# --------------------------------------------------------------------------------------------------------------------------
def elegir_servicio():
    global tipo_servicio 
    print(f.GREEN+" ========================================")
    print(f.GREEN+" ║"+f.RED+ "  [Servicio de correo de la victima]"+f.GREEN+   "  ║")
    print(f.GREEN+" ========================================")
    print(f.YELLOW+" [01]-"+f.GREEN+" Gmail")
    print(f.YELLOW+" [02]-"+f.GREEN+" Outlook/Hotmail")
    print(f.YELLOW+" [03]-"+f.GREEN+" Yahoo")
    print(f.YELLOW+" [04]-"+f.GREEN+" (LEER!!!)")
    print(f.YELLOW+" [05]-"+f.GREEN+" Salir de SpamMAIL-NR")
    tipo_servicio = input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")
    tipo_servicio.lower()

    if tipo_servicio == "04" or tipo_servicio == "4" or tipo_servicio == "Salir":
        subprocess.call(comando_limpiar, shell=True)
        print("[LEER SI ES PRIMERA VEZ QUE USA LA HERRAMIENTA]")
        print("""*Para poder usar un correo como remitente debe tener la opcion de ACCESO A APLICACIONES MENOS SEGURAS (activada)...

 [LINKS DIRECTOS]

 Gmail: https://myaccount.google.com/u/0/security?hl=es#connectedapps

 Outlook/Hotmail: https://outlook.live.com/owa/?path=/options/popandimap

 Yahoo: https://login.yahoo.com/account/security?.scrumb=xTZ2fUgh2eG#other-apps""")

        input(f.YELLOW+"\n[!]"+f.GREEN+" Preciones ENTER para ir atras.")
        subprocess.call(comando_limpiar, shell=True)
        banner_inicio()
        elegir_servicio()
        
    elif tipo_servicio == "05" or tipo_servicio == "5" or tipo_servicio == "leer":
        subprocess.call(comando_limpiar, shell=True)
        sys.exit()
   
    elif tipo_servicio == "1" or tipo_servicio == "01" or tipo_servicio == "2" or tipo_servicio == "02" or tipo_servicio == "3" or tipo_servicio == "03":
        pass

    else:
        print(f.YELLOW+" \n [!]"+f.RED+" ERROR.. No existe la opcione... vuelva a intentarlo")
        input(f.GREEN+" Precione 'ENTER' para continuar")
        subprocess.call(comando_limpiar, shell=True)
        banner_inicio()
        elegir_servicio()

    subprocess.call(comando_limpiar, shell=True)
    banner_inicio()

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"        [Correo de la victima]ㅤ "+f.GREEN+"     ║")
    print(f.GREEN+" =========================================")
    correo_victima = input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"       [Correo del remitente]          "+f.GREEN+"║")
    print(f.GREEN+" =========================================")
    correo_remitente = input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"        [Clave del remitente]   "+f.GREEN+"       ║")
    print(f.GREEN+" =========================================")
    clave = getpass.getpass(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"   [Confirme la clave del remitente]   "+f.GREEN+"║")
    print(f.GREEN+" =========================================")
    clave_confirmar = getpass.getpass(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"    [Cantidad de Correos a enviar]   "+f.GREEN+"  ║")
    print(f.GREEN+" =========================================")
    cantidad_correos = int(input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> "))

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"         [Titulo del correo]   "+f.GREEN+"       ║")
    print(f.GREEN+" =========================================")
    titulo_correo = input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    print(f.GREEN+" =========================================")
    print(f.GREEN+" ║"+f.RED+"         [Cuerpo del correo]   "+f.GREEN+"       ║")
    print(f.GREEN+" =========================================")
    cuerpo_correo = input(f.GREEN+" ["+f.RED+"SpamMAIL-NR"+f.GREEN+"]>> ")

    correo_enviar = "Subject: {}\n{}".format(titulo_correo, cuerpo_correo)

    print(f.YELLOW+"\n [!]"+f.GREEN+" Estructurando correo...")
    time.sleep(3)
    
    if clave != clave_confirmar:
        print(f.YELLOW+" [!]"+f.RED+" ERROR... las claves no coinciden, vuelva a intentarlo, precione ENTER para continuar.")
        input()
        subprocess.call(comando_limpiar, shell=True)
        banner_inicio()
        elegir_servicio()

    else:
        pass

    if tipo_servicio == "01" or tipo_servicio == "1" or tipo_servicio == "Gmail":
        host_servicio = "smtp.gmail.com"
        puerto = 587
        activar_servidor(correo_victima, correo_remitente, clave, cantidad_correos, correo_enviar, host_servicio, puerto)

    elif tipo_servicio == "02" or tipo_servicio == "2" or tipo_servicio == "Outlook":
        host_servicio = "smtp-mail.outlook.com"
        puerto = 587
        activar_servidor(correo_victima, correo_remitente, clave, cantidad_correos, correo_enviar, host_servicio, puerto)

    elif tipo_servicio == "03" or tipo_servicio == "3" or tipo_servicio == "Yahoo":
        host_servicio = "smtp.mail.yahoo.com"
        puerto = 25
        activar_servidor(correo_victima, correo_remitente, clave, cantidad_correos, correo_enviar, host_servicio, puerto)

def activar_servidor(correo_victima, correo_remitente, clave, cantidad_correos, correo_enviar, host_servicio, puerto):
    print(f.YELLOW+" [!]"+f.GREEN+" Conectando con el servidor...")
    time.sleep(2)
    try:
        servidor_gmail = smtplib.SMTP(host_servicio, puerto)
        servidor_gmail.starttls()
        print(f.YELLOW+" [+]"+f.GREEN+" Conexion exitosa con el servidor.")

    except smtplib.SMTPConnectError:
        print(f.YELLOW+" [!]"+f.RED+" ERROR... no se pudo establecer la conexion con el servidor, compruebe su internet y vuelva a intentarlo, precione ENTER para continuar")
        input()
        subprocess.call(comando_limpiar, shell=True)
        banner_inicio()
        elegir_servicio()

    print(f.YELLOW+" [!]"+f.GREEN+" Iniciando seccion con la cuenta del remitente establecido...")
    time.sleep(2)

    try:
        servidor_gmail.login(correo_remitente, clave)
        print(f.YELLOW+" [+]"+f.GREEN+" Inicio de seccion exitoso con la cuenta del usuario establecido.")
        
    except smtplib.SMTPAuthenticationError:
        print(f.YELLOW+" [!]"+f.GREEN+" ERROR... no se pudo iniciar seccion con la cuenta del remitente estalbecido, compruebe tener abilitada la opcion de APPs menos seguras en su cuenta, precione ENTER para continuar.")
        input()
        subprocess.call(comando_limpiar, shell=True)
        banner_inicio()
        elegir_servicio()
	
    inicio_tiempo, final_tiempo =  0, 0

    for i in range(1, cantidad_correos + 1):
        servidor_gmail.sendmail(correo_remitente, correo_victima, correo_enviar)
        hora_actual = datetime.now().strftime("%H:%M:%S")

        print(f.GREEN+" \n====================================================")
        print(f.YELLOW+" [+] "+f.GREEN+f"Correo {i} enviado satisfactoriamente")
        print(f.YELLOW+" Remitente: "+f.RED+correo_remitente+f.YELLOW+"\n Víctima: "+f.RED+correo_victima+f.YELLOW+"\n Hora: "+f.RED+hora_actual)
        print(f.GREEN+"====================================================")

    servidor_gmail.quit()
    input(f.YELLOW+" \n [+]"+f.GREEN+" Fin del proceso, precione ENTER para continuar.")
    subprocess.call(comando_limpiar, shell=True)
    banner_inicio()
    elegir_servicio()

subprocess.call(comando_limpiar, shell=True)
banner_inicio()
elegir_servicio()
