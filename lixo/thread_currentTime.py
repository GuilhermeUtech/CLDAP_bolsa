import threading
import time
from datetime import datetime

data_e_hora_atuais = datetime.now()

class ThreadOne(threading.Thread):
    def run(self):
        while(1):
            data_e_hora_atuais = datetime.now()
            data_em_texto = '{}{}{}{}{}{}.0Z'.format(data_e_hora_atuais.year,data_e_hora_atuais.month,data_e_hora_atuais.day,data_e_hora_atuais.hour, data_e_hora_atuais.minute, data_e_hora_atuais.second)
            data_e_hora_atuais = data_em_texto
            print(data_e_hora_atuais)
            time.sleep(60)
            
thingOne = ThreadOne()
thingOne.start()




