import datetime
from flask import Flask, request, make_response, render_template, url_for
from flask_restful import Resource, Api
from json import dumps
import json
import argparse
import broadlink

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument("--timeout", type=int, default=5, help="timeout to wait for receiving discovery responses")
parser.add_argument("--ip", default=None, help="ip address to use in the discovery")
args = parser.parse_args()


app = Flask(__name__)
api = Api(app)

def getDeviceName(deviceType):
  name = {
    0x2711: "SP2",
    0x2719: "Honeywell SP2",
    0x7919: "Honeywell SP2",
    0x271a: "Honeywell SP2",
    0x791a: "Honeywell SP2",
    0x2720: "SPMini",
    0x753e: "SP3",
    0x7D00: "OEM branded SP3",
    0x947a: "SP3S",
    0x9479: "SP3S",
    0x2728: "SPMini2",
    0x2733: "OEM branded SPMini",
    0x273e: "OEM branded SPMini",
    0x7530: "OEM branded SPMini2",
    0x7546: "OEM branded SPMini2",
    0x7918: "OEM branded SPMini2",
    0x7D0D: "TMall OEM SPMini3",
    0x2736: "SPMiniPlus",
    0x2712: "RM2",
    0x2737: "RM Mini",
    0x273d: "RM Pro Phicomm",
    0x2783: "RM2 Home Plus",
    0x277c: "RM2 Home Plus GDT",
    0x272a: "RM2 Pro Plus",
    0x2787: "RM2 Pro Plus2",
    0x279d: "RM2 Pro Plus3",
    0x27a9: "RM2 Pro Plus_300",
    0x278b: "RM2 Pro Plus BL",
    0x2797: "RM2 Pro Plus HYC",
    0x27a1: "RM2 Pro Plus R1",
    0x27a6: "RM2 Pro PP",
    0x278f: "RM Mini Shate",
    0x27c2: "RM Mini 3",
    0x2714: "A1",
    0x4EB5: "MP1",
    0x4EF7: "Honyar oem mp1",
    0x4EAD: "Hysen controller",
    0x2722: "S1 (SmartOne Alarm Kit)",
    0x4E4D: "Dooya DT360E (DOOYA_CURTAIN_V2)",
  }
  return name.get(deviceType, "Not Supported") 

@app.route('/discover')
def discover():
  html=''
  devices = broadlink.discover(timeout=6, local_ip_address=args.ip)
  for device in devices:
    if device.auth():
       html = html + '<tr class="row100 body">'
       html = html + '<td class="cell100 column1 device_name">'+ getDeviceName(device.devtype) +'</td>'
       html = html + '<td class="cell100 column2 device_type">'+ format(hex(device.devtype)) +'</td>'
       html = html + '<td class="cell100 column3 device_ip ">'+ device.host[0] +'</td>'
       html = html + '<td class="cell100 column4 device_mac">'+ ''.join(format(x, '02x') for x in device.mac) +'</td>'
       html = html + '</tr>'
  return render_template('discovery.htm',content=html)

@app.route('/')
def devices():
  return render_template('devices.htm')


if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=7020)

