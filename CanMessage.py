# can_message.py



import can
from can.interfaces.vector import get_channel_configs
import time
#from colorama import init, Fore
import threading
import os

timeout = 0.02

class Command:
    def __init__(self):
        self.json_data = {
            "legacy_Mode": {
                "handshake": {
                    "Step0": {
                        "mode":1,
                        "ct3":1,
                        "ct2":0,
                        "ct1":0,
                        "ct0":0,
                        "ctp":0x000000,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "Step1": {
                        "mode":1,
                        "ct3":1,
                        "ct2":0,
                        "ct1":0,
                        "ct0":1,
                        "ctp":0x000000,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "Step2": {
                        "mode":1,
                        "ct3":1,
                        "ct2":0,
                        "ct1":1,
                        "ct0":0,
                        "ctp":0x000000,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "Step3": {
                        "mode":1,
                        "ct3":1,
                        "ct2":0,
                        "ct1":1,
                        "ct0":1,
                        "ctp":0x000000,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    }
                },
                "address_Alloc": {
                    "mode":1,
                    "ct3":0,
                    "ct2":1,
                    "ct1":0,
                    "ct0":1,
                    "ctp":0x000000,
                    "arbitration_id": 0x00000000,
                    "data": 0x00,
                    "dlc":1,
                    "is_extended_id": True,
                    "is_remote_frame": False,
                    "answer_id": 0x00000000,
                    "answer_data": 0x00000000
                },
                "address_Alloc_Quick": {
                    "mode":1,
                    "ct3":0,
                    "ct2":1,
                    "ct1":0,
                    "ct0":1,
                    "ctp":0x000000,
                    "arbitration_id": 0x00000000,
                    "data": 0x00,
                    "dlc":0,
                    "is_extended_id": True,
                    "is_remote_frame": True,
                    "answer_id": 0x00000000,
                    "answer_data": 0x00000000
                },
                
                "Reset_Address_Allocation": {
                    "mode":1,
                    "ct3":0,
                    "ct2":1,
                    "ct1":0,
                    "ct0":0,
                    "ctp":0x0000,
                    "arbitration_id": 0x00000000,
                    "data": 0x00,
                    "dlc":1,
                    "is_extended_id": True,
                    "is_remote_frame": True,
                    "answer_id": 0x00000000,
                    "answer_data": 0x00000000
                },
            },
            "normal_Mode": {
                "global":{
                    "lru_Get_Commercial_Name_and_Number": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE141,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "lru_Get_Hardware_Type_and_Address": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE009,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },            
                    "reset_Adress": {
                        "mode":0,
                        "priority":0,
                        "mtd":0x4180,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Can_Mode": {
                        "mode":0,
                        "priority":0,
                        "mtd":0x4140,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Can_Mode": {
                        "mode":0,
                        "priority":0,
                        "mtd":0x4160,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Active_State": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xDF07,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_State_String": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xA00A,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_State": {
                        "mode":0,
                        "priority":0,
                        "mtd":0x5002,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_State": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xA006,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "identification": {
                    "get_Identifi_Read": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE001,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Basic_Ident": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE003,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Sw_Version": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE005,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Config_Version": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE007,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Sw_Equipment": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE009,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Mcu_Info": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE00B,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Cl_Read": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE00D,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Cfg_Struct_Size": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE00F,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "trace": {
                    "clear_Trace": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE011,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Trace": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE013,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_String_Trace_MSB": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE015,
                        "arbitration_id": 0x00000000,
                        "data": 0x0000,
                        "dlc":2,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_String_Trace_LSB": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE017,
                        "arbitration_id": 0x00000000,
                        "data": 0x0000,
                        "dlc":2,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Mask_Trace": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE019,
                        "arbitration_id": 0x00000000,
                        "data": 0x00000000,
                        "dlc":4,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Mask_Trace": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE01B,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    }
                },
                "configuration": {
                    "TODO":"TODO"
                },
                "read_componants":{
                    "get_Val_Adc":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4400,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Val_IO":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4420,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Val_Freq_PWM":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4440,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Val_Duty_Cycle_PWM":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4460,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Pwm_State":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4480,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Temperature":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x44A0,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_OTime":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x44C0,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "send_Operational_Time":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x44E0,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_System_Time":{
                        "mode":0,
                        "priority":0,
                        "mtd":0x4500,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "mode_Management": {
                    "set_Mode": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xA006,
                        "arbitration_id": 0x00000000,
                        "data": 0x04,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    
                    "get_Mode": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xA002,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_String_Mode": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xA00A,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "Erase_Cfg": {
                        "mode":0,
                        "priority":0,
                        "mtd":0x4823,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "edu_General": {
                    "set_Edu_Cmd": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE030,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Edu_Status": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE031,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Current": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE040,

                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Position": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE041,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "edu_Calibration" :{
                    "get_Pos_Cal_Min_Max": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0B1,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "send_Read_Pos_Step_Cal_Min_Max": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0B3,
                        "arbitration_id": 0x00000000,
                        "data": [0xFF,0x04],
                        "dlc":2,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "send_Read_Pos_Factory_Cal_Min_Max": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0B5,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":4,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Calibration_Parameters": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0B7,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Calibration_Parameters": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0B9,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":4,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Compute_Calibration": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0BB,
                        "arbitration_id": 0x00000000,
                        "data": [0x00, 0xFF],
                        "dlc":2,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Compute_Double_Calibration": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0BD,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "compute_Pitch_Calibration": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0BD,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":1,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "edu_Lumbar_System_PWM_Debug" :{
                    "get_Ldu_Pwm": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE080,
                        "arbitration_id": 0x00000000,
                        "data": 0x00,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "edu_Lumbar_System_General" :{
                    "set_Ldu_Cmd_Single": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE091,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Ldu_Cmd_Sequence": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE092,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "read_EVU_Board_Identification": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE095,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":3,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Ldu_Status": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE097,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Ldu_Bag_HS_Flag": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE099,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":3,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "set_Ldu_Generic": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE09A,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":8,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "edu_Lumbar_system_current_and_pressure" :{
                    "get_Ldu_Unity_PresUI": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0A0,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Ldu_Filtered_UI": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0A1,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                    "get_Ldu_No_Filtered_PresUI": {
                        "mode":0,
                        "priority":0,
                        "mtd":0xE0A2,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": True,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                },
                "srl_general":{
                    "get_Srl_Status": {
                        "mode":0,
                        "priority":3,
                        "mtd":0xA206,
                        "arbitration_id": 0x00000000,
                        "data": 0x000000,
                        "dlc":0,
                        "is_extended_id": True,
                        "is_remote_frame": False,
                        "answer_id": 0x00000000,
                        "answer_data": 0x00000000
                    },
                }

            }
        }

# adresse = 0x0A

class repeated_Timer:
    def __init__(self, interval, function, args=None, kwargs=None,debug=0):
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.is_running = False
        self.timer_thread = None
        self.debug = debug

    def _run(self):
        self.is_running = True
        while self.is_running:
            self.function(*self.args, **self.kwargs)
            # Attendre l'intervalle spécifié avant de réexécuter la fonction
            self.timer_thread = threading.Timer(self.interval, self._run)
            self.timer_thread.start()
            self.timer_thread.join()

    def start(self):
        if self.debug:
            #print(Fore.GREEN +"Timer Start",Fore.RESET)
            pass
        if not self.is_running:
            self.is_running = True
            self.timer_thread = threading.Timer(self.interval, self._run)
            self.timer_thread.start()
            if self.debug:
                #print(Fore.GREEN +"Timer Start complete",Fore.RESET)
                pass


    def stop(self):
        if self.debug:
            #print(Fore.RED +"Timer Stop",Fore.RESET)
            pass

        self.is_running = False
        self.timer_thread.cancel()

        
class can_Message:
    def __init__(self, json={},id=0x0A):
        #init()
        self.json= json
        self.handshake_status = -1
        self.id = id

    @staticmethod
    def create_arbitration_id_legacy(json_data):
        ctp_binary = ''.join(format(json_data[key], 'b') for key in ["mode", "ct3", "ct2", "ct1", "ct0"]) + format(json_data["ctp"], '024b')
        return ctp_binary

    def create_arbitration_id_normal(self, json_data):
        binary_result = format(json_data["mode"], '03b') + format(json_data["priority"], '02b') + format(json_data["mtd"] >> 8, '08b') + '00000000' + format(json_data["mtd"] & 0xFF, '08b') + '00'

        try:
            if isinstance(self.id, str):
                if self.id.startswith("0x"):
                    id_int = int(self.id[2:], 16)  
                else:
                    id_int = int(self.id)
            else:
                id_int = self.id

        except ValueError:
            raise ValueError("Invalid format for self.id (expected integer or hex string starting with '0x')")

        binary_result = format(id_int << 10 | int(binary_result, 2), '0' + str(len(binary_result)) + 'b')
        return binary_result


    @staticmethod
    def verif_arbitration_id_normal(binary_data):
        mode = int(binary_data[0:2], 2)
        priority = int(binary_data[2:4], 2)
        mtd_high_8_bits = int(binary_data[4:12], 2)
        srs = int(binary_data[12], 2)
        ide = int(binary_data[13], 2)
        id_val = int(binary_data[14:22], 2)
        mtd_low_8_bits = int(binary_data[22:30], 2)
        mtd = (mtd_high_8_bits << 8) | mtd_low_8_bits

        json_data = {
            "Verification": {
                "mode": mode,
                "priority": priority,
                "mtd": hex(mtd),  
                "srs": srs,
                "ide": ide,
                "id": id_val,
                "arbitration_id": 0x00000000,
                "data": 0x00,
                "dlc": 0,
                "is_extended_id": True,
                "is_remote_frame": True,
                "answer_id": 0x00000000,
                "answer_data": 0x00000000
            }
        }

        return json_data


    @staticmethod
    def convert_bin_to_hex(ctp_binary_padded):
        return(hex(int(ctp_binary_padded, 2)))
    
    @staticmethod
    def hex_to_binary(hex_value):
        return(bin(int(hex_value, 16))[2:].zfill(29))
    
    @staticmethod
    def parse_Answer_Json_legacy(json_data, binary_string):
        json_data["mode"] = binary_string[0:1]
        json_data["ct3"] = binary_string[1:2]
        json_data["ct2"] = binary_string[2:3]
        json_data["ct1"] = binary_string[3:4]
        json_data["ct0"] = binary_string[4:5]
        ctp_hex = hex(int(binary_string[-24:], 2))
        json_data["ctp"] = ctp_hex
        return json_data
    
    @staticmethod
    def parse_Ctp(json_data, binary_string):
        ctp_int = int(binary_string[-24:], 2)
        json_data["ctp"] = ctp_int
        return json_data

    def create_can_message_legacy(self, json_data):
        if json_data["arbitration_id"] == 0x00000000:
            json_data["arbitration_id"] = int(self.convert_bin_to_hex(self.create_arbitration_id_legacy(json_data)), 16)

        msg =  can.Message(
            arbitration_id=json_data["arbitration_id"],
            data=json_data["data"],
            is_extended_id=json_data["is_extended_id"],
            is_remote_frame=json_data["is_remote_frame"],
        )
        if json_data["data"] != 0x00:
            data_hex_str = hex(json_data["data"])[2:]  # Convert data to hexadecimal string
            if len(data_hex_str) % 2 != 0:
                data_hex_str = '0' + data_hex_str  # Add leading zero if necessary

            data_bytes = bytes.fromhex(data_hex_str) 
            msg.data = data_bytes
        msg.dlc = json_data["dlc"]
        return msg
    

    def create_can_message_normal(self, json_data):
        # if json_data["arbitration_id"] == 0x00000000:
        json_data["arbitration_id"] = int(self.convert_bin_to_hex(self.create_arbitration_id_normal(json_data)), 16)
    
        data = json_data["data"]
        if isinstance(data, int):
            data = bytes([data])  # Convertir en bytes si c'est un entier
            
        msg = can.Message(
            arbitration_id=json_data["arbitration_id"],
            data=data,
            dlc=json_data["dlc"],
            is_extended_id=json_data["is_extended_id"],
            is_remote_frame=json_data["is_remote_frame"],
        )
        return msg

class can_Bus:
    def __init__(self, interface='vector' ,app_name='CANalyzer',channel=0,bitrate=125000,Debug=False,bustype = None):
        self.debug = Debug

        if bustype==None:
            self.bus = can.Bus(interface=interface, app_name=app_name, channel=channel, bitrate=bitrate )
        else:
            os.system(f'sudo ip link set {channel} type can bitrate {bitrate}')
            os.system(f'sudo ifconfig {channel} up')
            # self.bus = can.interface.Bus(channel = channel, bustype = bustype)
            self.bus = can.interface.Bus(channel=channel, bustype=bustype, bitrate=bitrate)


    def __del__(self):
        os.system('sudo ifconfig can0 down')
        # self.bus.shutdown()

        
    def can_Send_Receive(self,msg):
        message = self.bus.recv(0.01)
        while message:

            message = self.bus.recv(0.01)
        message=None
        try :
            self.bus.send(msg)
            if self.debug == 1 :
                print("="*150)
                #print(Fore.BLUE +"Message send :",msg,Fore.RESET)
            message = self.bus.recv(timeout)
            if message and message.arbitration_id !=0 :
                if self.debug == 1 :
                    #print(Fore.GREEN +"Message reçu :",message,Fore.RESET)
                    pass
                if message.arbitration_id == 0xf7c0804:
                    return{"error":{"event_code":message.data}}
                elif message.arbitration_id == 0x00c:
                    print("CAN connected. CAN not powered or module not connected.")
                    # exit()
                elif message.arbitration_id == 0x024:
                    print("CAN not connected.")
                    # exit()
                    
                return{"id":message.arbitration_id,"data":message.data}
            else :
                if self.debug == 1 :
                    #print(Fore.RED +"Error: No Answer",Fore.RESET)
                    pass
                return{"error":None}
        except Exception as e:
            return{"error":e}


    def can_Send_Receive_Broadcast(self, msg):
        self.bus.flush_rx_buffer()

        try:
            self.bus.send(msg)
            if self.debug == 1:
                print("=" * 150)
                #print(Fore.BLUE + "Message send :", msg, Fore.RESET)

            received_messages = []  # Tableau pour stocker les messages reçus


            message = self.bus.recv(timeout)  # Initialisation de message avant la boucle

            while message is not None:  # Utilisation de 'is not None' pour vérifier si message n'est pas vide
                if message and message.arbitration_id != 0:
                    if self.debug == 1:
                        #print(Fore.GREEN + "Message reçu :", message, Fore.RESET)
                        pass
                    if message.arbitration_id == 0xf7c0804:
                        print("error !!! ")
                        return {"error": {"event_code": message.data}}

                    received_messages.append({"id": message.arbitration_id, "data": message.data})

                message = self.bus.recv(timeout)  # Mise à jour de message dans la boucle

            if not received_messages:
                if self.debug == 1:
                    #print(Fore.RED + "Error: No Answer", Fore.RESET)
                    pass
                return {"error": None}

            return received_messages

        except Exception as e:
            return {"error": e}




class can_Com:
    def __init__(self, Can=None,id=0x00):        
        self.bus = Can
        self.debug = Can.debug
        self.name = "NoName"
        self.id = id
        self.full_Id = "NoName1234"

        self.json_data = Command()
        self.message = can_Message(self.json_data.json_data,self.id)

    def __del__(self):
        del self.bus

    def set_id(self,id=0x00):
        self.id = id
        self.message.id = id

    def list_Devices(self):
        all_device = []

        for vcc in get_channel_configs():
            all_device.append({"name":vcc.name,"bus_params":vcc.bus_params})

        if len(all_device) == 0 :
            all_device.append({"error":"no devices on can"})

        return all_device

    def list_Slaves_New(self):
        message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["Reset_Address_Allocation"]))
        time.sleep(0.2)
        all_slave = []
        msg = self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["handshake"][f'Step0'])
        if self.debug == 1 :
            print("="*150)
            #print(Fore.BLUE +"Message send :",msg,Fore.RESET)
        self.bus.bus.send(msg)

        while True:
            # time.sleep(0.5)
            message = self.bus.bus.recv(1)
            if  message:
                if self.debug == 1 :
                    #print(Fore.GREEN + "Message reçu :", message, Fore.RESET)
                    pass


                if message.arbitration_id == 0x00c:
                    print("CAN connected. CAN not powered or module not connected.")
                    # exit()
                    return
                elif message.arbitration_id == 0x024:
                    print("CAN not connected.")
                    # exit()

                hex_string = hex(message.arbitration_id)[2:][-6:] 
                ascii_string = ""
                for i in range(0, len(hex_string), 2):
                    ascii_string += chr(int(hex_string[i:i+2], 16))
                all_slave.append({"id":hex(message.arbitration_id),"name":ascii_string})
            else:
                break
        if len(all_slave) == 0 :
            all_slave.append({"error":"no new devices on can"})
        message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["Reset_Address_Allocation"]))
        return all_slave

    def list_Slaves_Already(self):
        all_slave = []


        msg = self.message.create_can_message_normal(self.message.json["normal_Mode"]["global"]["lru_Get_Commercial_Name_and_Number"])
        self.bus.bus.send(msg)
        if self.debug == 1 :
            print("="*150)
            #print(Fore.BLUE +"Message sende :",msg,Fore.RESET)


        while True:
            message = self.bus.bus.recv(timeout)
            if message:
                id = hex(int(self.message.hex_to_binary(hex(message.arbitration_id))[11:19], 2))

                data  = message.data
                lru_name = message.data[:4].decode('ascii', errors='ignore')  
                lru_number = message.data[4:].decode('ascii', errors='ignore')  

                all_slave.append({"id":"0x" + id[2:].zfill(2).upper(),"name":lru_name,"number":lru_number,"lru":f"{lru_name}{lru_number}"})
                if self.debug == 1 :
                    #print(Fore.GREEN + "Message reçu :", message, Fore.RESET)
                    pass

                if message.arbitration_id == 0x00c:
                    print("CAN connected. CAN not powered or module not connected.")
                    # exit()
                    return
                elif message.arbitration_id == 0x024:
                    print("CAN not connected.")
                    # exit()
                    return
                    
            else:
                break

        if len(all_slave) == 0:
            all_slave.append({"error": "No Slave already set"})
        

        return all_slave


    def create_custom_can_message_normal(self, arbitration_id,data,dlc,rf):
        msg = can.Message(
            arbitration_id=arbitration_id,
            data=data,
            dlc=dlc,
            is_extended_id=True,
            is_remote_frame=rf,
        )
        message = self.bus.can_Send_Receive(msg)
        return message

    def discover(self):
        return self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["handshake"]['Step0']))

    def handshake(self):
        json = self.message.json["legacy_Mode"]["handshake"]
        message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["Reset_Address_Allocation"]))

        for i in range(0, 4):

            # Vérification de la taille du tableau
            if f'Step{i}' not in json:
                print("Erreur: Index de tableau invalide.")
                return None, None
            if self.debug == 1 :
                #print(Fore.YELLOW +f"Step : Step{i}",Fore.RESET)
                pass

            message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(json[f'Step{i}']))
            if "error" not in message:
                self.handshake_status = i
                json[f'Step{i}']["answer_id"] = f'0x{message["id"]:08X}'
                if i != 3:
                    if i == 0:
                        hex_string = hex(message["id"])[2:][-6:] 
                        ascii_string = ""
                        for n in range(0, len(hex_string), 2):
                            ascii_string += chr(int(hex_string[n:n+2], 16))
                        self.name = ascii_string
                        self.full_Id = self.name
                    elif i == 1 :
                        hex_string = hex(message["id"])[2:][-6:] 
                        if len(hex_string) >= 6:
                            self.full_Id += hex_string[3]  + hex_string[5] 
                        else: 
                            return json[f'Step{i}'] , f'Step{i}'
                    elif i == 2 :
                        hex_string = hex(message["id"])[2:][-6:] 
                        if len(hex_string) >= 6:
                            self.full_Id += hex_string[1]  + hex_string[3] 
                        else: 
                            return json[f'Step{i}'] , f'Step{i}'

                    self.message.parse_Ctp(json[f'Step{i+1}'],self.message.hex_to_binary(json[f'Step{i}']["answer_id"]))
                elif i == 3 :

                    return json[f'Step{i}'] , f'Step{i}'
            else:
                return json[f'Step{i}'] , f'Step{i}'



    def adrress_Alloc(self,id):
        self.id = id
        self.message.id = self.id
        self.message.json["legacy_Mode"]["address_Alloc"]["data"] = id
        try:
            if self.handshake_status ==3 :

                self.message.parse_Ctp(self.message.json["legacy_Mode"]["address_Alloc"],self.message.hex_to_binary(self.message.json["legacy_Mode"]["handshake"]['Step3']["answer_id"]))
                message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["address_Alloc"]))


                message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["Reset_Address_Allocation"]))
                message = self.set_Active_State()
                # message = self.set_Can_Mode("normal")

                return {"Setup":True}
            return {"Setup":False,"error":{"Handshake not completed":self.handshake_status}}
        except Exception as e :
            return {"Setup":False,"error":{"Handshake not completed":e}}

    
    def get_command(self,json):
        message = self.bus.can_Send_Receive(self.message.create_can_message_normal(json))
        if "error" not in message:
            try:
                hex_array = ['{:02X}'.format(byte) for byte in message["data"]]
                json["answer_id"] = hex(message["id"])
                json["answer_data"] = hex_array

                if self.debug :
                    #print(Fore.YELLOW, json , Fore.RESET)
                    pass

                return {"id": hex(message["id"]), "data": hex_array}
            except Exception as e:
                return {"error": "Error get_command","detail":e}
        else:
            return {"error": "No Answer"}
        
        
        
    def get_Address_Alloc_Quick(self):
        try :
            message = self.bus.can_Send_Receive(self.message.create_can_message_legacy(self.message.json["legacy_Mode"]["address_Alloc_Quick"]))
            hex_array = ['{:02X}'.format(byte) for byte in message["data"]]
            return {"id":hex(message["id"]),"data":hex_array}
        except Exception as e:
                return {"error": "No Answer"}
        
# =============================================================================================================================================================================================
# I) Global :
            # "reset_Adress": {
            # "set_Can_Mode": {
            # "get_Can_Mode": {
    def reset_Adress(self):
        return self.get_command(self.message.json["normal_Mode"]["global"]["reset_Adress"])
    
    def set_Can_Mode(self,mode):
        if mode=="config":
            return self.send_reset(self.message.json["normal_Mode"]["global"]["set_Can_Mode"],1)
        elif mode == "normal":
            return self.send_reset(self.message.json["normal_Mode"]["global"]["set_Can_Mode"],12)
        elif mode == "test":
            return self.send_reset(self.message.json["normal_Mode"]["global"]["set_Can_Mode"],4)

        return {"error": "Can mode completed"} 
        
    def get_Can_Mode(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["global"]["get_Can_Mode"])
        if "error" in json_data:
            return json_data
        else:
            byte2 = int(json_data['data'][1], 16)
            byte3 = int(json_data['data'][2], 16)

            # Interprétation des données en fonction de la documentation
            lru_can_mode_number = int(json_data['data'][1], 16)
            node_number = (byte3 & 0xF8) >> 3  # Bits 7:3
            pax_number = byte3 & 0x07  # Bits 2:0

            return {"mode_number":lru_can_mode_number,"node_number":node_number,"pax_number":pax_number,"adress":hex(byte3)}
    
    def set_Active_State(self):
        return self.get_command(self.message.json["normal_Mode"]["global"]["set_Active_State"])
    
    def set_State(self,mode):
        json = self.message.json["normal_Mode"]["global"]["set_State"]
        if mode=="Init" :
                json["data"] = 0
        elif mode=="Select" :
                json["data"] = 1
        elif mode=="Switch" :
                json["data"] = 2
        elif mode=="attAck" :
                json["data"] = 3
        elif mode=="Actif" :
                json["data"] = 4
        elif mode=="WriteCfg" :
                json["data"] = 5
        elif mode=="ActifU" :
                json["data"] = 6
        elif mode=="ActifUT" :
                json["data"] = 7
        elif mode=="ErrCbit" :
                json["data"] = 8
        elif mode=="Debug" :
                json["data"] = 9
        elif mode=="BadCfg" :
                json["data"] = 10
        elif mode=="Calib" :
                json["data"] = 11
        elif mode=="ErrPbit" :
                json["data"] = 12
        elif mode=="ErrSys" :
                json["data"] = 13
        elif mode=="Reset" :
                json["data"] = 14
        elif mode=="CodeLoad" :
                json["data"] = 15
        elif mode=="SuspenMT" :
                json["data"] = 16
        elif mode=="Package" :
                json["data"] = 17
        elif mode=="Request" :
                json["data"] = 18
        return self.get_command(json)


    def get_State(self):
        return self.get_command(self.message.json["normal_Mode"]["global"]["get_State"])
    
    def get_State_String(self, state_number):
        self.message.json["normal_Mode"]["global"]["get_State_String"]["data"] = state_number
        json_data = self.get_command(self.message.json["normal_Mode"]["global"]["get_State_String"])
        
        if "error" in json_data:
            return json_data
        else:
            state_characters = [chr(int(byte, 16)) for byte in json_data['data']]

            null_index = state_characters.index('\x00') if '\x00' in state_characters else len(state_characters)

            state = ''.join(state_characters[:null_index])

            return {"state": state}

    


    def lru_Get_Commercial_Name_and_Number(self):
        json =  self.get_command(self.message.json["normal_Mode"]["global"]["lru_Get_Commercial_Name_and_Number"])
        if "error" in json:
            return json
        else:
            data_int = [int(x, 16) for x in json['data']]
            lru_name = "".join(chr(byte) for byte in data_int[:3])
            lru_number = "".join(hex(byte)[3] for byte in data_int[4:])

            return {"id":json["id"],"name":lru_name,"number":lru_number,"lru":f"{lru_name}{lru_number}"}
    
    def lru_Get_Hardware_Type_and_Address(self):
        json =  self.get_command(self.message.json["normal_Mode"]["global"]["lru_Get_Hardware_Type_and_Address"])

        data_int = [int(x, 16) for x in json['data']]
        equipment_name = "".join(chr(byte) for byte in data_int[:3])
        return {"id":json["id"],"equipment":equipment_name,"hw_address":data_int[4]}
    
        
# =============================================================================================================================================================================================
# I) IDENTIFICATION  

        
    def get_Identifi_Read(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Identifi_Read"])

    def get_Basic_Ident(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Basic_Ident"])
    
    def get_Sw_Version(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Sw_Version"])

    def get_Config_Version(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Config_Version"])

    def get_Sw_Equipment(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["identification"]["get_Sw_Equipment"])

        id_binary = bin(int(json_data['id'], 16))[2:].zfill(32)

        equipment_type = id_binary[4:8]
        hardware_version = id_binary[8:12]
        lru_type = id_binary[12:16]

        equipment_type_decimal = int(equipment_type, 2)
        hardware_version_decimal = int(hardware_version, 2)
        lru_type_decimal = int(lru_type, 2)

        equipment_ascii = ''.join(chr(int(x, 16)) for x in json_data['data'][:3])
        hardware_version_response = int(json_data['data'][3], 16)
        lru_type_response = int(json_data['data'][4], 16)

        extracted_data = {
            "Equipment_Type": equipment_type_decimal,
            "Hardware_Version": hardware_version_decimal,
            "LRU_Type": lru_type_decimal,
            "Equipment_ASCII": equipment_ascii,
            "Hardware_Version_Response": hardware_version_response,
            "LRU_Type_Response": lru_type_response
        }

        return (extracted_data)


        # return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Sw_Equipment"])

    def get_Mcu_Info(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Mcu_Info"])

    def get_Cl_Read(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Cl_Read"])

    def get_Cfg_Struct_Size(self):
        return self.get_command(self.message.json["normal_Mode"]["identification"]["get_Cfg_Struct_Size"])

# =============================================================================================================================================================================================
# II) TRACE  

    def clear_Trace(self):
        return self.get_command(self.message.json["normal_Mode"]["trace"]["clear_Trace"])
    
    def get_Trace(self):
        return self.get_command(self.message.json["normal_Mode"]["trace"]["get_Trace"])
    
    def get_String_Trace_MSB(self):
        return self.get_command(self.message.json["normal_Mode"]["trace"]["get_String_Trace_MSB"])
    
    def get_String_Trace_LSB(self):
        return self.get_command(self.message.json["normal_Mode"]["trace"]["get_String_Trace_LSB"])
    
    def set_Mask_Trace(self , mask):
        self.message.json["normal_Mode"]["trace"]["set_Mask_Trace"]["data"] = mask
        return self.get_command(self.message.json["normal_Mode"]["trace"]["set_Mask_Trace"])
    
    def get_Mask_Trace(self):
        return self.get_command(self.message.json["normal_Mode"]["trace"]["get_Mask_Trace"])

    
# =============================================================================================================================================================================================
# III) read_componants  
    
    def send_reset(self,json,data):
        base = json["mtd"]
        json["mtd"] = json["mtd"] | data
        json["arbitration_id"] = 0x00000000
        msg = self.get_command(json)
        json["mtd"] = base
        return msg


    def get_Val_Adc(self, ADC): 
        if ADC < 0 or ADC > 7:
            return {"error": "ADC value out of range"}
        else:
            return self.send_reset(self.message.json["normal_Mode"]["read_componants"]["get_Val_Adc"],ADC)

    def get_Val_IO(self, IO): 
        if IO < 0 or IO > 2:
            return {"error": "IO value out of range"}
        else:
            return self.send_reset(self.message.json["normal_Mode"]["read_componants"]["get_Val_IO"],IO)

    def get_Val_Freq_PWM(self, PWM): 
        if PWM < 0 or PWM > 2:
            return {"error": "PWM value out of range"}
        else:
            return self.send_reset(self.message.json["normal_Mode"]["read_componants"]["get_Val_Freq_PWM"],PWM)
        
    def get_Val_Duty_Cycle_PWM(self):
        return self.get_command(self.message.json["normal_Mode"]["read_componants"]["get_Val_Duty_Cycle_PWM"])

    def get_Pwm_State(self):
        return self.get_command(self.message.json["normal_Mode"]["read_componants"]["get_Pwm_State"])
    
    def get_Temperature(self):
        message = self.get_command(self.message.json["normal_Mode"]["read_componants"]["get_Temperature"])
        if "error" in message:
            return message
        else:
            if message and 'data' in message:
                data = message['data']
                if len(data) >= 7:
                    instant_Temperature = int(data[0], 16)
                    min_Temp_Last_Reading = int(data[1], 16)
                    max_Temp_Last_Reading = int(data[2], 16)
                    min_Temp_Last_PowerUp = int(data[3], 16)
                    max_Temp_Last_PowerUp = int(data[4], 16)
                    min_Temp_Exploitation = int(data[5], 16)
                    max_Temp_Exploitation = int(data[6], 16)
                    return {
                        "instant_Temperature_°C": instant_Temperature,
                    }

                    # return {
                    #     "instant_Temperature_C": instant_Temperature,
                    #     "minTemp_Last_Reading_C": min_Temp_Last_Reading,
                    #     "maxTemp_Last_Reading_C": max_Temp_Last_Reading,
                    #     "minTemp_Last_PowerUp_C": min_Temp_Last_PowerUp,
                    #     "maxTemp_Last_PowerUp_C": max_Temp_Last_PowerUp,
                    #     "min_Temp_Exploitation_C": min_Temp_Exploitation,
                    #     "max_Temp_Exploitation_C": max_Temp_Exploitation
                    # }
            return message

        

    
    def get_OTime(self):
        return self.get_command(self.message.json["normal_Mode"]["read_componants"]["get_OTime"])
    
# "send_Operational_Time":{
    # "TODO":"TODO"

    def get_System_Time(self):
        return self.get_command(self.message.json["normal_Mode"]["read_componants"]["get_System_Time"])

# =============================================================================================================================================================================================
# IV) mode_Management  
    
        
    def set_Mode(self,mode):
        self.message.json["normal_Mode"]["mode_Management"]["set_Mode"]["data"] = mode
        return self.get_command(self.message.json["normal_Mode"]["mode_Management"]["set_Mode"])
    
    def get_Mode(self):
        return self.get_command(self.message.json["normal_Mode"]["mode_Management"]["get_Mode"])
    
    def get_String_Mode(self):
        return self.get_command(self.message.json["normal_Mode"]["mode_Management"]["get_String_Mode"])
    
    def Erase_Cfg(self):
        return self.get_command(self.message.json["normal_Mode"]["mode_Management"]["Erase_Cfg"])

# =============================================================================================================================================================================================
# V) edu_General  


    def set_Edu_Cmd(self,speed,event,power,state,position):
        
        self.message.json["normal_Mode"]["edu_General"]["set_Edu_Cmd"]["data"] = [speed, event, power, state ,0x00 ,0x00, position >> 8 & 0xFF, position & 0xFF]
        message = self.bus.can_Send_Receive(self.message.create_can_message_normal(self.message.json["normal_Mode"]["edu_General"]["set_Edu_Cmd"]))
        return message

    def get_Edu_Status(self):
        msg = self.get_command(self.message.json["normal_Mode"]["edu_General"]["get_Edu_Status"])

        if "error" in msg or msg["id"] == '0x0':
            return msg
        else:
            try :
                data_int = [int(x, 16) for x in msg['data']]
                state = data_int[0]
                event = data_int[1]
                position = ((data_int[2] << 8) | data_int[3]) & 0xFFF
                power = data_int[4]
                current_FEM = data_int[5]
                sense_actuator_displacement = data_int[6]

                state_description = {
                    7: "unlocking area",
                    6: "finalization",
                    5: "retraction after over current",
                    4: "error (received Emergency...)",
                    3: "problem (over current, ermergency, potentiometer problem...)",
                    2: "regulation power",
                    1: "pause",
                    0: "busy"
                }
                state_info = {bit: description for bit, description in state_description.items() if state & (1 << bit)}

                if not state_info:
                    state_info = {-1: "idle"}

                event_description = {
                    7: "speed min atteind",
                    6: "commande valide recue",
                    5: "switch etat electro-aimant",
                    4: "urgence",
                    3: "probleme",
                    2: "probleme potentiometre",
                    1: "zone interdite",
                    0: "limite 2"
                }
                event_info = {bit: description for bit, description in event_description.items() if event & (1 << bit)}

                parsed_data = {
                    "id": hex(self.id),
                    "state": state_info,
                    "event": event_info,
                    "position": position,
                    "power": power,
                    "current_FEM": current_FEM,
                    "sense_actuator_displacement": {
                        "command_reception": "Yes" if sense_actuator_displacement >> 7 & 0x01 else "No",
                        "command_sense": (sense_actuator_displacement >> 2) & 0x03,
                        "real_sense": sense_actuator_displacement & 0x03
                    }
                }

                return parsed_data
            except Exception as e :
                return{"error":e}




        

    def get_Current(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_General"]["get_Current"])
        try : 
            if "error" in json_data or json_data["id"] == '0x0':
                return json_data
            else:
                data_int = [int(x, 16) for x in json_data['data']]

                return {
                    "filtered_instant_current_mA": (data_int[0] << 8) | data_int[1],
                    "overfiltered_instant_ADC_forward_step": (data_int[2] << 8) | data_int[3],
                    "overfiltered_instant_ADC_backward_step": (data_int[4] << 8) | data_int[5],
                    "filtered_instant_torque_Newton": (data_int[6] << 8) | data_int[7]
                }
        except Exception as e:
            return{"error":{"event_code":e}}

    def get_Position(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_General"]["get_Position"])
        if "error" in json_data or json_data["id"] == '0x0':
            return json_data
        else:
            data_int = [int(x, 16) for x in json_data['data']]
            try :
                return {
                    "manufacture_position_None": (data_int[0] << 8) | data_int[1],
                    "filtered_position_step": (data_int[2] << 8) | data_int[3],
                    "position_step": (data_int[4] << 8) | data_int[5]
                }
            except Exception as e:
                return{"error":{"event_code":e}}



# =============================================================================================================================================================================================
# VI) edu_Calibration  
    
# "send_Read_Pos_Step_Cal_Min_Max": {
# "send_Read_Pos_Factory_Cal_Min_Max": {
# "set_Calibration_Parameters": {
# "get_Compute_Calibration": {
# "get_Compute_Double_Calibration": {
# "compute_Pitch_Calibration": {

    def get_Pos_Cal_Min_Max(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_Calibration"]["get_Pos_Cal_Min_Max"])
        if "error" in json_data or json_data["id"] == '0x0':
            return json_data
        else:
            data_int = [int(x, 16) for x in json_data['data']]

            calibration_state = data_int[0]
            min_calibration_double_position = (data_int[1] << 8) | data_int[2]
            max_calibration_double_position = (data_int[3] << 8) | data_int[4]
            calibration_simple_position = (data_int[5] << 8) | data_int[6]

            calibration_state_description = {
                2: "incorrect configurations"
            }
            calibration_state_info = {bit: "Set" if calibration_state & (1 << bit) else "Not set" for bit in calibration_state_description}

            parsed_data = {
                "calibration_state": calibration_state_info,
                "min_calibration_double_position": min_calibration_double_position,
                "max_calibration_double_position": max_calibration_double_position,
                "calibration_simple_position": calibration_simple_position
            }

            return parsed_data

        

    def get_Calibration_Parameters(self,parameters=0):
        self.message.json["normal_Mode"]["edu_Calibration"]["get_Calibration_Parameters"]["data"] = parameters
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_Calibration"]["get_Calibration_Parameters"])

        if "error" in json_data or json_data["id"] == '0x0':
            return json_data
        else:
            data_int = [int(x, 16) for x in json_data['data']]

            input_data_state = {
                "calibrated": "Calibrated" if not (data_int[1] & (1 << 0)) else "Not calibrated",
                "incorrect_input_value": "Set" if data_int[1] & (1 << 7) else None,
                "incorrect_configurations": "Set" if data_int[1] & (1 << 2) else None,
                "neutral_calibration": "Set" if data_int[1] & (1 << 1) else None,
                "simple_calibration_value": "Set" if (data_int[1] & (1 << 2)) and (data_int[1] & (1 << 0)) else None,
                "neutral_calibration_value": "Set" if (data_int[1] & (1 << 1)) and (data_int[1] & (1 << 0)) else None
            }

            parsed_data = {
                "parameter": data_int[0],
                "input_data_state": {key: value for key, value in input_data_state.items() if value is not None},
                "refer_to_parameter_1": data_int[2],
                "refer_to_parameter_2": data_int[3]
            }

            return parsed_data

    def send_Read_Pos_Step_Cal_Min_Max(self,min,max):
        self.message.json["normal_Mode"]["edu_Calibration"]["send_Read_Pos_Step_Cal_Min_Max"]["data"] = [(min >> 8) & 0xFF,  min & 0xFF,  (max >> 8) & 0xFF,max & 0xFF ]
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_Calibration"]["send_Read_Pos_Step_Cal_Min_Max"])
        if "error" in json_data or json_data["id"] == '0x0':
            return json_data
        else:
            

            parsed_data = {}

            input_data_state = int(json_data['data'][0], 16)
            parsed_data['calibrated'] = "Calibrated" if input_data_state & 0x01 else "Not calibrated"
            if input_data_state & 0x01: 
                parsed_data['input_data_state'] = {'calibrated': parsed_data['calibrated']}
            else:  
                bits = {
                    7: 'na',
                    6: 'calibration limit out of range',
                    5: 'computed result out off range',
                    4: 'incorrect parameter value 2',
                    3: 'incorrect parameter value 1',
                    2: 'incorrect configurations',
                    1: 'neutral calibration',
                    0: 'calibrated'  
                }
                    
                parsed_data['input_data_state'] = {bits[bit]: 'Set' if input_data_state & (1 << bit) else None for bit in bits}

            offset = int(json_data['data'][1] + json_data['data'][2], 16)
            parsed_data['calibration_offset'] = offset / 10.0

            coefficient = int(json_data['data'][3] + json_data['data'][4], 16)
            if coefficient >= 0x8000:
                coefficient -= 0x10000
            parsed_data['calibration_coefficient'] = coefficient / 1000.0

            return parsed_data


    
    def get_Compute_Calibration(self):
        json_data = self.get_command(self.message.json["normal_Mode"]["edu_Calibration"]["get_Compute_Calibration"])
        return json_data


# =============================================================================================================================================================================================
# VII) edu_Lumbar_System_General  

#  "edu_Lumbar_System_General" :{
#             "set_Ldu_Cmd_Single": {# "TODO":"TODO"
#             "set_Ldu_Cmd_Sequence": {# "TODO":"TODO"
#             "get_Ldu_Status": {
#             "set_Ldu_Bag_HS_Flag": {# "TODO":"TODO"
#             "set_Ldu_Generic": {# "TODO":"TODO"
# data_to_send = [
#     0x00,  # Air bag number (exemple: 0 pour le premier sac d'air)
#     0xFF,  # Speed (0xFF pour aucun effet)
#     0x01,  # Event (exemple: 1 pour gonfler)
#     0xFF,  # Power (0xFF pour aucun effet)
#     0x00,  # State (exemple: 00 pour régulation FEM)
#     0x00,  # Forbidden area (0x00 pour aucun effet)
#     0xFF, 0xFF  # Pressure (0xFFFF pour aucun effet)
# ]
    def set_Ldu_Cmd_Sequence(self, speed, event, power, state, pressure, time, command):
        # Diviser la valeur de la pression en deux parties (non implémenté dans la documentation)
        pressure_high = (pressure >> 8) & 0xFF  # Bits de poids fort
        # Assigner les valeurs à la donnée d'envoi
        self.message.json["normal_Mode"]["edu_Lumbar_System_General"]["set_Ldu_Cmd_Sequence"]["data"] = [
            speed,            # Vitesse (0xFF pour aucun effet)
            event,            # Événement
            power,            # Puissance (0xFF pour aucun effet)
            state,            # État
            pressure_high,    # Pression (bits de poids fort)
            time,             # Temps (0xFF pour aucun effet)
            0x00,             # Zone interdite (0x00 pour aucun effet)
            command           # Commande
        ]
        return self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_System_General"]["set_Ldu_Cmd_Sequence"])


    def set_Ldu_Cmd_Single(self,nb,speed,event,power,state,pressure):
        self.message.json["normal_Mode"]["edu_Lumbar_System_General"]["set_Ldu_Cmd_Single"]["data"] = [
            nb,  # Air bag number (exemple: 0 pour le premier sac d'air)
            speed,  # Speed (0xFF pour aucun effet)
            event,  # Event (exemple: 1 pour gonfler)
            power,  # Power (0xFF pour aucun effet)
            state,  # State (exemple: 00 pour régulation FEM)
            0x00,  # Forbidden area (0x00 pour aucun effet)
            int(hex(0x1004)[2:].zfill(4)[:2], 16) , 
            int(hex(0x1004)[2:].zfill(4)[2:], 16)  # Pressure (0xFFFF pour aucun effet)
        ]
        return self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_System_General"]["set_Ldu_Cmd_Single"])
    


    def get_Ldu_Status(self):

        msg = self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_System_General"]["get_Ldu_Status"])
        json_data = None
        if msg and "error" not in msg:
            # print(msg)

            binary_data = [bin(int(hex_str, 16))[2:].zfill(8) for hex_str in msg["data"]]
            try:
                
                binary_data = [bin(int(hex_str, 16))[2:].zfill(8) for hex_str in msg["data"]]
                state = int(binary_data[0], 2)  # Convertir la chaîne binaire en entier
                state_description = {
                    7: "unlocking area",
                    6: "finalization",
                    5: "retraction after over current",
                    4: "error (received Emergency...)",
                    3: "problem (over current, ermergency, potentiometer problem...)",
                    2: "regulation power",
                    1: "pause",
                    0: "busy"
                }
                json_state = {bit: description for bit, description in state_description.items() if state & (1 << bit)}
                if not json_state:
                    json_state = {-1: "idle"}
                # print("state_info", json_state)
                

                # json_state = {
                #     "problem": binary_data[0][4],
                #     "pause": binary_data[0][6],
                #     "busy": binary_data[0][7]
                # }

                # if all(value == '0' for value in json_state.values()):
                #     json_state = {-1: 'idle'}
                # else:
                #     json_state = {key: value for key, value in json_state.items() if value != '0'}



                json_event = {
                                "ack": binary_data[1][1],
                                "max_power": binary_data[1][2],
                                "min_power": binary_data[1][3]
                            }
                pressure = msg["data"][2]
                power = msg["data"][3]
                status_field = binary_data[4] + binary_data[5] + binary_data[6] + binary_data[7]

                # Création du dictionnaire de statuts pour chaque cycle
                status = {}

                # Parcours des 4 cycles, du dernier au premier
                for i in range(3, -1, -1):
                    cycle_index = i * 8
                    cycle_status = status_field[cycle_index:cycle_index + 3]
                    cycle_number = status_field[cycle_index + 3:cycle_index + 8]
                    status["cycle" + str(4 - i)] = {
                        "status": cycle_status[::-1],  # Inversion pour obtenir le MSB en premier
                        "cycle_number": cycle_number[::-1]  # Inversion pour obtenir le MSB en premier
                    }

                json_data={"state":json_state,"event":json_event,"pressure":pressure,"power":power,"status":status}
            except Exception as e:
                return{"error":{"event_code":e}}



        if json_data != None :
            return json_data

        else:
            return msg

        return msg


# =============================================================================================================================================================================================
# VIII) edu_Lumbar_system_current_and_pressure  

    def get_Ldu_Unity_PresUI(self):
        message = self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_system_current_and_pressure"]["get_Ldu_Unity_PresUI"])   
        if "error" in message:
            return message
        else:
            if message and 'data' in message:
                data = message['data']
                if len(data) >= 8:
                    filtered_pressure = int.from_bytes(bytes.fromhex(data[0] + data[1]), byteorder='big', signed=False)
                    filtered_voltage = int.from_bytes(bytes.fromhex(data[2] + data[3]), byteorder='big', signed=False)
                    filtered_current_electro_valves = int.from_bytes(bytes.fromhex(data[4] + data[5]), byteorder='big', signed=False)
                    filtered_current_pump_motor = int.from_bytes(bytes.fromhex(data[6] + data[7]), byteorder='big', signed=False)
                    return {
                        "filtered_pressure_hPa": filtered_pressure,
                        "filtered_voltage_mV": filtered_voltage,
                        "filtered_current_electro_valves_mA": filtered_current_electro_valves,
                        "filtered_current_pump_motor_mA": filtered_current_pump_motor
                    }
            return message
            
    def get_Ldu_Filtered_UI(self):
        message = self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_system_current_and_pressure"]["get_Ldu_Filtered_UI"])   
        if "error" in message:
            return message
        else:
            if message and 'data' in message:
                data = message['data']
                if len(data) >= 8:
                    filtered_pressure = int.from_bytes(bytes.fromhex(data[0] + data[1]), byteorder='big', signed=False)
                    filtered_voltage = int.from_bytes(bytes.fromhex(data[2] + data[3]), byteorder='big', signed=False)
                    filtered_current_electro_valves = int.from_bytes(bytes.fromhex(data[4] + data[5]), byteorder='big', signed=False)
                    filtered_current_pump_motor = int.from_bytes(bytes.fromhex(data[6] + data[7]), byteorder='big', signed=False)
                    return {
                        "filtered_pressure": filtered_pressure,
                        "filtered_voltage": filtered_voltage,
                        "filtered_current_electro_valves": filtered_current_electro_valves,
                        "filtered_current_pump_motor": filtered_current_pump_motor
                    }
            return message
     
    def get_Ldu_No_Filtered_PresUI(self):
        message = self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_system_current_and_pressure"]["get_Ldu_No_Filtered_PresUI"])   
        if "error" in message:
            return message
        else:
            if message and 'data' in message:
                data = message['data']
                if len(data) >= 8:
                    filtered_pressure = int.from_bytes(bytes.fromhex(data[0] + data[1]), byteorder='big', signed=False)
                    filtered_voltage = int.from_bytes(bytes.fromhex(data[2] + data[3]), byteorder='big', signed=False)
                    filtered_current_electro_valves = int.from_bytes(bytes.fromhex(data[4] + data[5]), byteorder='big', signed=False)
                    filtered_current_pump_motor = int.from_bytes(bytes.fromhex(data[6] + data[7]), byteorder='big', signed=False)
                    return {
                        "filtered_pressure": filtered_pressure,
                        "filtered_voltage": filtered_voltage,
                        "filtered_current_electro_valves": filtered_current_electro_valves,
                        "filtered_current_pump_motor": filtered_current_pump_motor
                    }
            return message
       

# =============================================================================================================================================================================================
# IX) edu_Lumbar_System_PWM_Debug  

           

    def get_Ldu_Pwm(self):
        return self.get_command(self.message.json["normal_Mode"]["edu_Lumbar_System_PWM_Debug"]["get_Ldu_Pwm"])

# =============================================================================================================================================================================================


    def get_Srl_Status(self):
        return self.get_command(self.message.json["normal_Mode"]["srl_general"]["get_Srl_Status"])

# =============================================================================================================================================================================================
# IX) test  

            



    def test_edu_general(self):
        print("\nTest des fonctions de test_edu_general :")
        print("get_Edu_Status:", self.get_Edu_Status())
        print("get_Current:", self.get_Current())
        print("get_Position:", self.get_Position())


    def get_Identification(self):
        print("\nTest des fonctions d'identification' :")

        print("Identifi Read:", self.get_Identifi_Read())
        print("Basic Ident:", self.get_Basic_Ident())
        print("Software Version:", self.get_Sw_Version())
        print("Configuration Version:", self.get_Config_Version())
        print("Software Equipment:", self.get_Sw_Equipment())
        print("MCU Information:", self.get_Mcu_Info())
        print("CL Read:", self.get_Cl_Read())
        print("Configuration Structure Size:", self.get_Cfg_Struct_Size())
        print("Address Alloc Quick:", self.get_Address_Alloc_Quick())
        print("get_Can_Mode : " , self.get_Can_Mode())
        print("get_Edu_Status :",self.get_Edu_Status())
        print("get_Srl_Status :",self.get_Srl_Status())

    def test_Trace(self):
        print("\nTest des fonctions de trace :")
        print("clear_Trace:", self.clear_Trace())
        print("get_Trace:", self.get_Trace())
        print("get_String_Trace_MSB:", self.get_String_Trace_MSB())
        print("get_String_Trace_LSB:", self.get_String_Trace_LSB())
        print("get_Mask_Trace:", self.get_Mask_Trace())
        mask = [0x04,0x02,0x05,0x01]
        print("\nTest de la fonction set_Mask_Trace avec le masque :", mask)
        print("set_Mask_Trace:", self.set_Mask_Trace(mask))
        print("get_Mask_Trace:", self.get_Mask_Trace())

    def test_ReadIO(self):
        print("\nTest des fonctions de readIO :")
        for i in range(8):
            print(f'get_Val_Adc {i}:', self.get_Val_Adc(i))
        for i in range(3):
            print(f'get_Val_IO {i}:', self.get_Val_IO(i)) 
        for i in range(3):
            print(f'get_Val_Freq_PWM {i}:', self.get_Val_Freq_PWM(i)) 
        print(f'get_Val_Duty_Cycle_PWM :', self.get_Val_Duty_Cycle_PWM()) 
        print(f'get_Pwm_State :', self.get_Pwm_State()) 
        print(f'get_Temperature :', self.get_Temperature())     
        print(f'get_OTime :', self.get_OTime())     
        print(f'get_System_Time :', self.get_System_Time()) 
        

    def test_edu_Calibration(self):
        print("get_Pos_Cal_Min_Max :",self.get_Pos_Cal_Min_Max())
        for i in range(5):

            print(f'get_Calibration_Parameters {i} :',self.get_Calibration_Parameters(i))

        print("send_Read_Pos_Step_Cal_Min_Max :",self.send_Read_Pos_Step_Cal_Min_Max(0,200))
        print("get_Pos_Cal_Min_Max :",self.get_Pos_Cal_Min_Max())

