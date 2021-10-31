import time
import serial

def send_sms(recipient: str, message: str) -> dict:

    # We will store all the data and configs of the execution on this dictionary
    execution = {
        "verbose": False
    }

    def log_progress (data_name: str, value):

        # replace quotes
        if '"' in value:
            value = value.replace('"', "'")

        execution[data_name] = value
        if (execution["verbose"]) == True:
            print(data_name," = ",value)


    try:
        modem = serial.Serial("COM13",  115200, timeout=4)
        log_progress("modem_port_details",str(modem))
        modem_connected = True
    except Exception as e:
        log_progress("error_message",str(e))
        modem_connected = False

    execution["modem_connected"] = modem_connected

    if modem_connected == True:

        # enable Echo
        modem.write(b'ATE0\r')
        time.sleep(0.2)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress("ATE0",str(modem_response))

        # Device Status
        modem.write(b'ATI\r')
        time.sleep(0.2)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress("ATI",str(modem_response))

        # Sets SMS Text Mode
        modem.write(b'AT+CFUN=1\r')
        time.sleep(0.2)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress("AT+CFUN=1",str(modem_response))

        # Getting SMS List
        modem.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress('AT+CMGF=1',str(modem_response))

        # IRA
        modem.write(b'AT+CSCS="IRA"\r')
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress('AT+CSCS=IRA',str(modem_response))

        # Destination
        modem.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress(message,str(modem_response))

        # Message
        modem.write(message.encode() + b"\r")
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress(message,str(modem_response))

        # Close / Exit
        modem.write(bytes([26]))
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress(message,str(modem_response))


        modem.close()


    return execution











