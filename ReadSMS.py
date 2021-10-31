import time
import serial

def read_sms() -> dict:

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
        modem.write(b'AT+CMGF=1\r')
        time.sleep(0.2)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress("AT+CMGF=1",str(modem_response))

        # Getting SMS List
        modem.write(b'AT+CMGL="ALL"\r')
        time.sleep(0.5)
        modem_response = (modem.read_all()).strip().decode("utf-8")
        log_progress('AT+CMGL=ALL',modem_response)

        # Building List of Messages
        responselines = modem_response.splitlines()
        msgCount = 0
        collectnext = False
        msglist = []

        for line in responselines:
            if '+CMGL: ' in line:
                LineData = line.split(",")

                # Build Date 
                date = (LineData[4]).replace('"', '')
                date = (date).split("/")
                final_date = date[2] + "/" + date[1] + "/20" + date[0]
                # Build  Hour
                hour = (LineData[5]).replace('"', '')
                hour = hour[:8]
                message_date = final_date + " " + hour

                # Build Source
                message_source = LineData[2]
                message_source = message_source.replace('"', '')

                Message = {
                    'message_index' : msgCount,
                    'date'          : message_date,
                    'number'        : message_source
                }
                collectnext = True
                msgCount = msgCount + 1
            else:
                if collectnext == True:
                    # Add Message to dictionary 
                    Message['Message'] = line
                    # Add Message to List of Messages
                    msglist.append(Message)
                    # Reset CollectNext
                    collectnext = False


        log_progress('message_list',msglist)

        modem.close()


    return execution

