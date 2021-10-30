import time
import serial

recipient = "+5541987012013"
message = "Essa Mensagem Top"

echo_command = True
get_device_status = False
debug = False

phone = serial.Serial("COM13",  115200, timeout=5)
try:

    if(debug == True): 
        print("Let's start the Modem with Clean Configuration")
    phone.write(b'ATZ\r')
    time.sleep(1)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    if(echo_command == True):
        # Let's enable the Echo to Check the progress
        if(debug == True): 
            print("Enabling Echo response of AT Commands")
        phone.write(b'ATE\r')
        time.sleep(0.1)
        quantity = phone.in_waiting
        response =  (phone.read(quantity)).strip().decode( "utf-8" )
        if(debug == True): 
            print(response)
            print("-------------------------------------")
            print("")

    if(get_device_status == True):
        # Device Status
        if(debug == True): 
            print("Getting Device Information")
        phone.write(b'ATI\r')
        time.sleep(0.5)
        quantity = phone.in_waiting
        response =  (phone.read(quantity)).strip().decode( "utf-8" )
        if(debug == True): 
            print(response)
            print("-------------------------------------")
            print("")
    
        if(debug == True): 
            print("registration status of the device...")
        phone.write(b'AT+CGREG?\r')
        time.sleep(2)
        quantity = phone.in_waiting
        response =  (phone.read(quantity)).strip().decode( "utf-8" )
        if(debug == True): 
            print(response)
            print("-------------------------------------")
            print("")

        if(debug == True): 
            print("get the network information:")
        phone.write(b'AT+COPS?\r')
        time.sleep(2)
        quantity = phone.in_waiting
        response =  (phone.read(quantity)).strip().decode( "utf-8" )
        if(debug == True): 
            print(response)
            print("-------------------------------------")
            print("")

        if(debug == True): 
            print("check the signal quality:")
        phone.write(b'AT+CSQ\r')
        time.sleep(2)
        quantity = phone.in_waiting
        response =  (phone.read(quantity)).strip().decode( "utf-8" )
        if(debug == True): 
            print(response)
            print("-------------------------------------")
            print("")

    # Sets the device to full functionality.
    if(debug == True):
        print("Seeting Device as Full IN/OUT")
    phone.write(b'AT+CFUN=1\r')
    time.sleep(0.2)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
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
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    # Setting Character Type 
    if(debug == True): 
        print("Seeting Char Type")
    phone.write(b'AT+CSCS="IRA"\r')
    time.sleep(0.2)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")
    
    # Destination
    if(debug == True): 
        print("Sending Message To")
    phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
    time.sleep(0.5)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    # Message
    if(debug == True): 
        print("Message")
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

    if(debug == True): 
        print("Exit")
    phone.write(bytes([26]))
    time.sleep(0.5)
    quantity = phone.in_waiting
    response =  (phone.read(quantity)).strip().decode( "utf-8" )
    if(debug == True): 
        print(response)
        print("-------------------------------------")
        print("")

finally:
    phone.close()


