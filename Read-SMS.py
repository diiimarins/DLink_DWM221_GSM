import time
import serial

port = "COM13"
phone = serial.Serial(port,  115200, timeout=5)

debug = False

try:  
    # Let's enable the Echo to Check the progress
    if(debug == True): 
        print("Enabling Echo response of AT Commands")
    phone.write(b'ATE\r')
    time.sleep(0.1)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode("utf-8")
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    
    # Device Status
    if(debug == True): 
        print("Getting Device Information")
    phone.write(b'ATI\r')
    time.sleep(0.5)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode("utf-8")
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")


    # Sets SMS Text Mode
    if(debug == True): 
        print("Seeting Set SMS Text Mode")
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.2)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode("utf-8")
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")


    # Device Status
    if(debug == True): 
        print("Getting SMS List")
    phone.write(b'AT+CMGL="ALL"\r')
    time.sleep(0.5)
    quantity = phone.in_waiting
    read = phone.read(quantity)
    response = (read).strip().decode("utf-8")
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    responselines = response.splitlines()

    msgCount = 0
    collectnext = False
    msglist = []

    for line in responselines:
        if "+CMGL: " in line:

            LineData = line.split(",")
            Message = {
                "MessageIndex" : msgCount,
                "Date"         : LineData[4] + LineData[5],
                "Number"       : LineData[2]
            }

            collectnext = True
            msgCount = msgCount + 1

        else:
            if collectnext == True:
                # Add Message to dictionary 
                Message["Message"] = line

                # Add Message to List of Messages
                msglist.append(Message)

                # Reset CollectNext
                collectnext = False


finally:
    print(msglist)
    phone.close()


