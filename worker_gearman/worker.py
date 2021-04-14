from python3_gearman import GearmanWorker
import main

######################################################################################
##                        WORKER PYTHON GEARMAN CLARO VIDEO                         ##
##                                                                                  ##
##  Modulo/Worker en python el cual realiza el test de capitulos e imagenes         ##
##  en la plataforma de Claro Video                                                 ##
######################################################################################

# se define el worker, host y puerto al que estara a la escucha de cada peticion
# para realizar un nuevo Job
host = '127.0.0.1'
puerto = '4773'
worker = GearmanWorker(['{}:{}'.format(host, puerto)])

# funcion encarga de comunicarse al modulo de experiencia de usuario OWA
# el cual como resultado se obtiene una cadena en formato JSON
def test_claro_video(gearman_worker, gearman_job):
    response = main.main(cadena_json=gearman_job.data)
    return response

worker.register_task('job_test_claro_video', test_claro_video)
worker.work()