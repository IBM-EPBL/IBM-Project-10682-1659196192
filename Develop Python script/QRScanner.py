import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
#from ibmcloudant.cloudant_v1 import Cloudant_v1
from ibmcloudant.cloudant_v1 import CloudantV1

from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-2x3slc1z0cwbin5pcaaaclzqi2g9p2gd5j4goteo3pd9','168a3f057d8e22e93874f9a4d92a9624')
service = CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-amoudkk04osw9s8ofdgy4ywsguhm184fbqjo7qgbbvr:168a3f057d8e22e93874f9a4d92a9624@210f6ad9-8436-49d8-bae7-e7e376a647f8-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _,frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data",obj.data)
        a = obj.data.decode('UTF-8')
        cv2.putText(frame,"Ticket",(50,50),font,2,(255,0,0),3)
        #print(a)
        try:
            response = service.get_document(
                db='booking',
                doc_id = a
                ).get_result()
            print(response)
            time.sleep(5)
        except Exception as e:
            print("Not a valid Ticket")
            time.sleep(5)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()


                                
