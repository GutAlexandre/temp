from threading import Lock
from flask import Flask, render_template, session, request, copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
import copy
import socket as udpSock

IP_loxone = "192.168.1.159"
loxone_tx_port = 7520
loxone_rx_port = 7001
message = b"lgt_off"
print("\n\n                  IAMS\n\n                  START\n\n")
sock = udpSock.socket(udpSock.AF_INET,udpSock.SOCK_DGRAM)
sock.bind(('', loxone_rx_port))
sock.sendto(message, (IP_loxone, loxone_tx_port))
sock.sendto(b"ch_on", (IP_loxone, loxone_tx_port))

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
print("up")

#====================================
#part can
import time
import signal
#from CanMessage import can_Com, can_Bus, repeated_Timer
import threading
import os
import sys
from collections import deque


# liste_slave = {
#     "RPC3301": {"id" : "0x0A","hard_id" :"0x00" },
#     "RPC3300": {"id" : "0x0B","hard_id" :"0x00" },
#     "P4C1790": {"id" : "0x0C","hard_id" :"0x00"},
#     "Broadcast": {"id" : "0x00","hard_id" :"0x00"},
#     "NoName1234": {"id" : "0x00","hard_id" :"0x00"},
# }

# globals()["database"] = []
# history_toast = []
# queue = deque()
# globals()["i"] = 0
# globals()["temp"] = None
# globals()["Json"] = {
#     "COMFORT": {
#         "heating_pad": {
#         "heating_None": "FALSE",
#         "command_temperature_°C": 0,
#         "actual_temperature_°C": 0
#         },
#         "mini_fridge": {
#         "cooling_None": "FALSE",
#         "can_1_presence_None": "FALSE",
#         "can_2_presence_None": "FALSE",
#         "command_temperature_°C": 0,
#         "actual_temperature_°C": 0
#         },
#         "reading_light": {
#         "actual_state_None": "ON",
#         "power_level_%": 10
#         },
#         # "mood_LEDs": {
#         # "R_%": 50,
#         # "G_%": 50,
#         # "B_%": 50,
#         # "W_%": 50
#         # }
#     },
#     "RPC3300": {},
#     "RPC3301": {},
#     "P4C1790": {}
# }


# globals()["flag1"] = 0
# globals()["flag2"] = 0
# globals()["flag3"] = 0
# globals()["flag4"] = 0
# globals()["flag5"] = 0
# globals()["flag6"] = 0

# try :
#     Can = can_Bus( app_name='CANalyzer', channel='can0', bitrate=125000, Debug=0, bustype = 'socketcan')

#     for nom, details in liste_slave.items():
#         globals()[nom] = can_Com(Can)
        
#     def get_already_init():
#         already_Init = globals()["Broadcast"].list_Slaves_Already()
#         return {"len":len(already_Init),"already_Init":already_Init}

#     def new_slave():
#         temp = can_Com(Can)
#         discovery = (temp.discover())

#         if "error" not in discovery:
#             print("handshake : ", temp.handshake())
#             globals()[temp.full_Id] = temp
#             print("adrress_Alloc : ", temp.adrress_Alloc(int(liste_slave[temp.full_Id]["id"] , 16) )) # Utilisation de id_int comme argument pour adrress_Alloc
#             globals()[temp.full_Id] = temp
#             print("New_Slave Init")
#         del temp
#         queue.appendleft(get_already_init)


#     def get_status(nb_sl):
#         status = RPC3300.get_Edu_Status()
#         globals()["Json"]["RPC3300"].update({"status": status})
#         # print("RPC3300",globals()["Json"]["RPC3300"])

#         if status:
#             if 'state' in status and 3 in status['state']:
#                 if globals()["flag4"]  == 0 :
#                     socketio.emit('crash_slave', {'name': 'RPC3300','id': liste_slave["RPC3300"]["id"],"type":"warning"})
#                     history_toast.append({'name': 'RPC3300','error': "Over current","type":"warning","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag4"] = 1 
#             else :
#                 globals()["flag4"] = 0
#             if "error" in status :
#                 nb_sl-=1
#                 if globals()["flag1"] == 0  :
#                     socketio.emit('lost_slave', {'name': 'RPC3300','id': liste_slave["RPC3300"]["id"],"type":"danger"})
#                     history_toast.append({'name': 'RPC3300','error': "Lru lost","type":"danger","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag1"] = 1 
#             else :
#                 globals()["flag1"] = 0

#         status = RPC3301.get_Edu_Status()
#         globals()["Json"]["RPC3301"].update({"status": status})
#         # print("RPC3301",RPC3301.id,status)


#         if status:
#             if 'state' in status and 3 in status['state']:
#                 if globals()["flag5"] == 0 :
#                     socketio.emit('crash_slave', {'name': 'RPC3301','id': liste_slave["RPC3301"]["id"],"type":"warning"})
#                     history_toast.append({'name': 'RPC3301','error': "Over current","type":"warning","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag5"] = 1 
#             else :
#                 globals()["flag5"] = 0
#             if "error" in status :
#                 nb_sl-=1
#                 if globals()["flag2"] == 0 :
#                     socketio.emit('lost_slave', {'name': 'RPC3301','id': liste_slave["RPC3301"]["id"],"type":"danger"})
#                     history_toast.append({'name': 'RPC3301','error': "Lru lost","type":"danger","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag2"] = 1 
#             else :
#                 globals()["flag2"] = 0

                

#         status = P4C1790.get_Ldu_Status()
#         globals()["Json"]["P4C1790"].update({"status": status})
        
#         if status:
#             if 'state' in status and 3 in status['state']:
#                 if globals()["flag6"] == 0  :
#                     socketio.emit('crash_slave', {'name': 'P4C1790','id': liste_slave["P4C1790"]["id"],"type":"warning"})
#                     history_toast.append({'name': 'P4C1790','error': "Over current","type":"warning","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag6"] = 1 
#             else :
#                 globals()["flag6"] = 0
#             if "error" in status :
#                 nb_sl-=1
#                 if globals()["flag3"] == 0 :
#                     socketio.emit('lost_slave', {'name': 'P4C1790','id': liste_slave["P4C1790"]["id"],"type":"danger"})
#                     history_toast.append({'name': 'P4C1790','error': "Lru lost","type":"danger","timestamp":time.time()})
#                     #get_history_toasts()
#                     globals()["flag3"] = 1 
#             else :
#                 globals()["flag3"] = 0

                

#         if nb_sl < len(liste_slave)-2 :

#             if globals()["i"] == 0:
#                 globals()["temp"] = can_Com(Can)
#                 discovery = (globals()["temp"].discover())
#                 if "error" not in discovery:
#                     globals()["i"]+=1
#                 else:
#                     globals()["i"]=0
#             elif globals()["i"] == 1:
#                 globals()["temp"].handshake()
#                 globals()["i"]=globals()["i"]+1
#             elif globals()["i"] == 2:
#                 globals()["temp"].adrress_Alloc(int(liste_slave[globals()["temp"].full_Id]["id"] , 16) )
#                 globals()[globals()["temp"].full_Id] = globals()["temp"]
#                 print("New_Slave Init")
#                 socketio.emit('new_slave', {'name': globals()["temp"].full_Id,'id': liste_slave[globals()["temp"].full_Id]["id"],"type":"success"})
#                 history_toast.append({'name': globals()["temp"].full_Id,'success': "Lru connected","type":"success","timestamp":time.time()})
#                 #get_history_toasts()


#                 globals()["i"]=globals()["i"]+1
#             elif globals()["i"] == 3:
#                 get_already_init()
#                 globals()["i"]=0
#                 del globals()["temp"]
#                 globals()["i"]=0
        


#     temp = can_Com(Can)


#     new_Slave = globals()["Broadcast"].list_Slaves_New()
#     print("list_Slaves_New : ", new_Slave)
#     time.sleep(0.1)
#     #list_Slaves_Already :  [{'id': '0x0A', 'name': 'RPC', 'number': '3301', 'lru': 'RPC3301'}, {'id': '0x0B', 'name': 'RPC', 'number': '3300', 'lru': 'RPC3300'}, {'id': '0x0C', 'name': 'P4C', 'number': '1790', 'lru': 'P4C1790'}]
#     already_Init = globals()["Broadcast"].list_Slaves_Already()
   
#     for slave in already_Init: 
#         try:

#             history_toast.append({
#                 "name": slave["name"] + slave["number"],
#                 'success': "Lru connected",
#                 "type": "success",
#                 "timestamp": time.time()
#             })
#         except (KeyError, TypeError):
#             print(f"Error processing slave: {slave}")


#     print("list_Slaves_Already : ", already_Init)

#     if "error" not in new_Slave[0]:
#         for slave in new_Slave:
#             new_slave()
#             time.sleep(1)
#     if "error" not in already_Init[0]:
#         for slave in already_Init:
#             time.sleep(1)
#             if slave["id"] != liste_slave[slave["lru"]]["id"] :
#                 print(f"Id of {slave['lru']} Wrong. Real :{liste_slave[slave['lru']]['id']}, attempt : {slave['id']}")
#                 # sys.exit()
#             else:
#                 globals()[slave['lru']].name = slave['lru']
#                 globals()[slave['lru']].set_id(int(slave["id"], 16))
#                 globals()[slave['lru']].message.handshake_status = 3


#     def main():
#         nb_sl = len(already_Init)
#         i=0
#         print("start main")
#         if RPC3300.id == 0x0 :
#             RPC3300.set_id(liste_slave["RPC3300"]["id"])
#         if RPC3301.id == 0x0 :
#             RPC3301.set_id(liste_slave["RPC3301"]["id"])
#         if P4C1790.id == 0x0 :
#             P4C1790.set_id(liste_slave["P4C1790"]["id"])

#         while True:
#             # json_data ={}
#             globals()["Json"]["timestamp"] = time.time()
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3300"].update({"temperature": RPC3300.get_Temperature()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3301"].update({"temperature": RPC3301.get_Temperature()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["P4C1790"].update({"temperature": P4C1790.get_Temperature()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3300"].update({"current": RPC3300.get_Current()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3301"].update({"current": RPC3301.get_Current()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["P4C1790"].update({"current": P4C1790.get_Current()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3300"].update({"position": RPC3300.get_Position()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["RPC3301"].update({"position": RPC3301.get_Position()}))
#             queue.append(lambda: get_status(nb_sl))
#             queue.append(lambda: globals()["Json"]["P4C1790"].update({"pression": P4C1790.get_Ldu_Unity_PresUI()}))
#             queue.append(lambda: get_status(nb_sl))


#             i=i+1
#             if i >= 35:  # À raison de 34 valeurs secondes max
#                 if len(globals()["database"]) > 300:
#                     globals()["database"].pop(0)
#                 # Créer une nouvelle instance de l'objet JSON en le clonant
#                 new_json = copy.deepcopy(globals()["Json"])
#                 globals()["database"].append(new_json)
#                 socketio.emit('database', {'data': globals()["database"]})

#                 i=0

#             if i % 10 == 0:
#                 socketio.emit('mydata', {'data': globals()["Json"]})


#             if queue:
#                 func = queue.popleft()
#                 status = func() 
#                 if status:
#                     if "len" in status:
#                         nb_sl=len(status["already_Init"])
#                 # time.sleep(0.5) 

#     #          

#     main_thread = threading.Thread(target=main)
#     main_thread.start()




#     def signal_handler(sig, frame):
#         print("Arrêt de l'exécution du script...")
#         os.system('sudo ifconfig can0 down')
#         sys.exit(0)
#     signal.signal(signal.SIGINT, signal_handler)

# except Exception as e:
#     print("Can non pris en charge :",e)
#     # python = sys.executable
#     # os.execl(python, python, *sys.argv)

# #====================================



def udp_receive():
    lgt_state = 0
    bool_light = 2
    while (True):
        data = sock.recv(40)
        if (len(data) >= 6):
            if (data[:6] == b'lgt_on'):
                globals()["Json"]["COMFORT"]["reading_light"]["actual_state_None"] = "ON"
                continue
            if (data[:6] == b'lgt_of'):
                globals()["Json"]["COMFORT"]["reading_light"]["actual_state_None"] = "OFF"
                continue
            if (data[:6] == b'c1_off'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["can_1_presence_None"] = "FALSE"
                continue
            if (data[:6] == b'c2_off'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["can_2_presence_None"] = "FALSE"
                continue
            if (data[:6] == b'ch_off'):
                globals()["Json"]["COMFORT"]["heating_pad"]["heating_None"] = "FALSE"
                continue
            if (data[:6] == b'fr_off'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["cooling_None"] = "FALSE"
                continue
            
        if (len(data) >= 5):
            if (data[:5] == b'c1_on'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["can_1_presence_None"] = "TRUE"
                continue
            if (data[:5] == b'c2_on'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["can_2_presence_None"] = "TRUE"
                continue
            if (data[:5] == b'ch_on'):
                globals()["Json"]["COMFORT"]["heating_pad"]["heating_None"] = "TRUE"
                continue
            if (data[:5] == b'fr_on'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["cooling_None"] = "TRUE"
                continue

        if (len(data) >= 3):
            if (data[:3] == b'cch'):
                globals()["Json"]["COMFORT"]["heating_pad"]["command_temperature_°C"] = data[3:].decode()
                continue
            if (data[:3] == b'cfr'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["command_temperature_°C"] = data[3:].decode()
                continue

        if (len(data) >= 2):
            if (data[:2] == b'ch'):
                globals()["Json"]["COMFORT"]["heating_pad"]["actual_temperature_°C"] = data[2:].decode()
                continue
            if (data[:2] == b'fr'):
                globals()["Json"]["COMFORT"]["mini_fridge"]["actual_temperature_°C"] = data[2:].decode()
                continue
            # if (lgt_state != bool_light):
            #     bool_light = lgt_state

udp_receive_thread = threading.Thread(target=udp_receive)
udp_receive_thread.start()


def background_thread():
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})


@app.route('/old')
def indexOld():
    return render_template('old_index.html', async_mode=socketio.async_mode)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/graph')
def graph():
    return render_template('graph.html', async_mode=socketio.async_mode)

@app.route('/encoders')
def encodersControl():
    return render_template('encoders_control.html', async_mode=socketio.async_mode)


@app.route('/alex')
def alex():
    return render_template('alex.html', async_mode=socketio.async_mode)

@socketio.event
def my_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.event
def light_on():
    message = b"lgt_on"
    sock.sendto(message, (IP_loxone, loxone_tx_port))

@socketio.event
def light_off():
    message = b"lgt_off"
    sock.sendto(message, (IP_loxone, loxone_tx_port))


@socketio.event
def my_broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.event
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.event
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})

@socketio.on('who')
def who():
    emit('liste_slave',{'data': liste_slave})

@socketio.on('get_history_toasts')
def get_history_toasts():
    emit('history_toasts',{'history': history_toast})


@socketio.on('lduon')
def lduon():
    emit('ldu_state',{'state': "on"})
    queue.appendleft(lambda : P4C1790.set_Ldu_Cmd_Single(0,0xFE,0,0xFE,3,0xFFFF))
    time.sleep(1)
    queue.appendleft(lambda : P4C1790.set_Ldu_Cmd_Single(0,0xFE,1,0xFE,3,0xFFFF))
    time.sleep(0.2)
    queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 500))
    time.sleep(0.1)
    queue.appendleft(lambda : RPC3301.set_Edu_Cmd(50, 3, 254, 255, 500))


@socketio.on('lduoff')
def lduoff():
    emit('ldu_state',{'state': "off"})
    queue.appendleft(lambda : P4C1790.set_Ldu_Cmd_Single(0,0xFE,0,0xFE,3,0xFFFF))
    time.sleep(1)
    queue.appendleft(lambda : P4C1790.set_Ldu_Cmd_Single(0,0xFE,2,0xFE,3,0xFFFF))   
    time.sleep(0.2)
    queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 0))
    time.sleep(0.1)
    queue.appendleft(lambda : RPC3301.set_Edu_Cmd(50, 3, 254, 255, 0))


# globals()["flagpreset"] = 0
# @socketio.on('preset')
# def preset(message):
#     print(globals()["flagpreset"],message['data'])
#     posmin = 710
#     posmax =3440
#     state=0
#     if message['data'] == 0:
#         globals()["flagpreset"] = 0
#         queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 1, 254, 255, 0))
#         time.sleep(0.5)
#         queue.appendleft(lambda : RPC3301.set_Edu_Cmd(0, 1, 254, 255, 0))
#         time.sleep(0.5)
#         return
#     if message['data'] == 1:
#         queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 500))
#         time.sleep(0.5)
#         globals()["flagpreset"] = 0
#         while globals()["flagpreset"] or any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values()):
#             where_mot1 = (int((globals()["Json"]["RPC3300"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#             where_mot2 = (int((globals()["Json"]["RPC3301"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#             #print(state,where_mot1,where_mot2)
#             if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
#                 queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(00, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 break
#             if(where_mot1 >= 20) and state<1:
                
#                 state=1
#                 #print(state)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(30, 3, 254, 255, 255))
#                 time.sleep(0.5)
#             if(where_mot1 >= 60) and state<2:
#                 state=2

#                 #print(state)

#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(70, 3, 254, 255, 500))
#                 time.sleep(0.5)

#             if(where_mot1 >= 50 or where_mot2>=50) and state<3:
            
#                 state=3
#                 #print(state)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 500))
#                 time.sleep(0.5)
#         emit('sequence', {'end': 1})
#         globals()["flagpreset"] = 0
#         print("end 1",globals()["flagpreset"])
#     if message['data'] == 2:
#         queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 0))
#         time.sleep(0.5)
#         globals()["flagpreset"] = 0
#         while globals()["flagpreset"] or any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values()):
#             where_mot1 = (int((globals()["Json"]["RPC3300"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#             where_mot2 = (int((globals()["Json"]["RPC3301"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#             #print(state,where_mot1,where_mot2)
#             if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
#                 queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(00, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 break

#             if(where_mot1 <= 20) and state<1:
                
#                 state=1
#                 #print(state)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(30, 3, 254, 255, 255))
#                 time.sleep(0.5)
#             if(where_mot1 <= 60) and state<2:
#                 state=2

#                 #print(state)

#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(70, 3, 254, 255, 0))
#                 time.sleep(0.5)

#             if(where_mot1 <= 50 or where_mot2<=50) and state<3:
            
#                 state=3
#                # print(state)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 0))
#                 time.sleep(0.5)
#         emit('sequence', {'end': 1})
#         globals()["flagpreset"] = 0
#         print("end 2")
#     if int(message['data'] )== 3:
#         globals()["flagpreset"] = 0
#         where_mot1 = (int((globals()["Json"]["RPC3300"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#         where_mot2 = (int((globals()["Json"]["RPC3301"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
#         queue.appendleft(lambda : RPC3300.set_Edu_Cmd(60, 3, 254, 255, 200))
#         time.sleep(0.5)
#         queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 200))
#         time.sleep(0.5)

#         while globals()["flagpreset"] or any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values()):
#             if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
#                 queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 queue.appendleft(lambda : RPC3301.set_Edu_Cmd(00, 3, 254, 255, 0))
#                 time.sleep(0.5)
#                 break
#         emit('sequence', {'end': 1})
#         globals()["flagpreset"] = 0
#         print("end 3")


globals()["flagpreset"] = 0
@socketio.on('preset')
def preset(message):
    print(globals()["flagpreset"],message['data'])
    posmin = 710
    posmax =3440
    step=0
    if int(message['data'] ) == 0: #arret complet
        globals()["flagpreset"] = 0
        queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 1, 254, 255, 0))
        time.sleep(0.5)
        queue.appendleft(lambda : RPC3301.set_Edu_Cmd(0, 1, 254, 255, 0))
        time.sleep(0.5)
    elif int(message['data'] ) == 1:
        globals()["flagpreset"] = 1
        queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 500))
        time.sleep(0.5)
        while globals()["flagpreset"] and (any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values())):
            where_mot1 = (int((globals()["Json"]["RPC3300"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
            where_mot2 = (int((globals()["Json"]["RPC3301"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
            if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
                queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                break
            if(where_mot1 >= 20) and step<1:
                step=1
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(30, 3, 254, 255, 500))
                time.sleep(0.5)
            if(where_mot1 >= 60) and step<2:
                step=2
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(70, 3, 254, 255, 500))
                time.sleep(0.5)
            if(where_mot1 >= 50 or where_mot2>=50) and step<3:
                step=3
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 500))
                time.sleep(0.5)
    elif int(message['data'] ) == 2:
        globals()["flagpreset"] = 1
        queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255, 0))
        time.sleep(0.5)
        
        while globals()["flagpreset"] and (any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values())):
            where_mot1 = (int((globals()["Json"]["RPC3300"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)
            where_mot2 = (int((globals()["Json"]["RPC3301"]["position"]["position_step"]-posmin)) * 100) / (posmax-posmin)

            if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
                queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                break

            if(where_mot1 <= 20) and step<1:
                step=1
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(30, 3, 254, 255, 0))
                time.sleep(0.5)
            if(where_mot1 <= 60) and step<2:
                step=2
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(70, 3, 254, 255, 0))
                time.sleep(0.5)
            if(where_mot1 <= 50 or where_mot2<=50) and step<3:
                step=3
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 0))
                time.sleep(0.5)
    elif int(message['data'] )== 3:
        globals()["flagpreset"] = 1
        queue.appendleft(lambda : RPC3300.set_Edu_Cmd(60, 3, 254, 255, 200))
        time.sleep(0.5)
        queue.appendleft(lambda : RPC3301.set_Edu_Cmd(60, 3, 254, 255, 200))
        time.sleep(0.5)

        while globals()["flagpreset"] and (any(state == "busy" for state in globals()["Json"]["RPC3300"]["status"]["state"].values()) or any(state == "busy" for state in globals()["Json"]["RPC3301"]["status"]["state"].values())):
            if any(state == "probleme" for state in globals()["Json"]["RPC3300"]["status"]["event"].values()) or any(state == "probleme" for state in globals()["Json"]["RPC3301"]["status"]["event"].values()) :
                queue.appendleft(lambda : RPC3300.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                queue.appendleft(lambda : RPC3301.set_Edu_Cmd(0, 1, 254, 255, 0))
                time.sleep(0.5)
                break
    emit('sequence', {'end': 1})
    globals()["flagpreset"] = 0
    print("end",int(message['data'] ))

@socketio.on('close_room')
def on_close_room(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         to=message['room'])
    close_room(message['room'])


@socketio.event
def my_room_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         to=message['room'])


@socketio.event
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def new_connexion(message):
    emit('what is', {'cmdRot1': 'Connected', 'count': 0})


@socketio.event
def new_data(message):
    print("dataa", message)
    emit('dataa', {'dataa': 'Connected', 'count': 0})


@socketio.event
def new_position_rot_1(message):
#    temp = int((message['data'] * 500) / 100)
    posmin = 710
    posmax =3440

    temp = int(message['data'])
    temp = int(((temp-posmin) * 500) / (posmax-posmin))
    print("rotatif 1, new position", temp)

    queue.appendleft(lambda : RPC3300.set_Edu_Cmd(50, 3, 254, 255,temp ))
    time.sleep(0.5)

@socketio.event
def new_position_rot_2(message):
    print("rotatif 2, new position", message['data'])
    #temp = int((message['data'] * 500) / 100)
    posmin = 710
    posmax =3440

    temp = int(message['data'])
    temp = int(((temp-posmin) * 500) / (posmax-posmin))

    queue.appendleft(lambda : RPC3301.set_Edu_Cmd(50, 3, 254, 255, temp))
    time.sleep(0.5)


globals()["state_pneumatic"] = 0

@socketio.event
def new_position_pn(message):

    temp = int(message['data'])
    print(temp)
    if temp== 0:
        queue.appendleft(lambda: P4C1790.set_Ldu_Cmd_Single(0, 0xFE, 0, 0xFE, 3, 0xFFFF))
        time.sleep(1)
        return
    if temp < 0:
        if globals()["state_pneumatic"] != 1:
            queue.appendleft(lambda: P4C1790.set_Ldu_Cmd_Single(0, 0xFE, 0, 0xFE, 3, 0xFFFF))
            time.sleep(0.5)
            queue.appendleft(lambda : P4C1790.set_Ldu_Cmd_Single(0,0xFE,2,0xFE,3,0xFFFF))
            time.sleep(0.5)
            globals()["state_pneumatic"] = 1 
            return
    if globals()["state_pneumatic"] != 2:
        queue.appendleft(lambda: P4C1790.set_Ldu_Cmd_Single(0, 0xFE, 0, 0xFE, 3, 0xFFFF))
        time.sleep(0.5)
        globals()["state_pneumatic"] = 2 
    if temp > 0:
        queue.appendleft(lambda: P4C1790.set_Ldu_Cmd_Single(0, temp, 1, 0xFE, 3, 0xFFFF))
        time.sleep(0.5)

@socketio.event
def fr_on():
    sock.sendto(b"fr_off", (IP_loxone, loxone_tx_port))

@socketio.event
def fr_off():
    sock.sendto(b"fr_on", (IP_loxone, loxone_tx_port))

@socketio.event
def ch_on():
    sock.sendto(b"ch_off", (IP_loxone, loxone_tx_port))

@socketio.event
def ch_off():
    sock.sendto(b"ch_on", (IP_loxone, loxone_tx_port))

@socketio.event
def new_color(message):

    rd = str(message['data'][0])
    gr = str(message['data'][1])
    bl = str(message['data'][2])

    new_values = {
        "R_%": rd,
        "G_%": gr,
        "B_%": bl
    }

    # globals()["Json"]["COMFORT"]["mood_LEDs"].update(new_values)
    try:
        message = b"lred" + rd.encode()
        sock.sendto(message, (IP_loxone, loxone_tx_port))
        print(message)
        time.sleep(0.1)
        message = b"lgreen" + gr.encode()
        sock.sendto(message, (IP_loxone, loxone_tx_port))
        print(message)
        time.sleep(0.1)
        message = b"lblue" + bl.encode()
        sock.sendto(message, (IP_loxone, loxone_tx_port))
        print(message)
        time.sleep(0.1)
    except Exception as e :
        print("errrrrooor :",e)

    

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)

def runWebServer(debug: bool, host : str)-> None:
    socketio.run(app, allow_unsafe_werkzeug=True,debug=debug, host=host)
    print("run")

