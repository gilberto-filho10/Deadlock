import threading

impressora = threading.Lock()
camera = threading.Lock()

def romeo():
    impressora.acquire()
    print("Romeo esta usando a impressora")

    print("Romeo solicita a camera")
    camera.acquire()
    
    # Etapa Final que não consegui ser executada #
    print("Romeo termina de usar os recursos")

    camera.release()
    impressora.release()

def julieta():
    camera.acquire()
    print("Julieta esta usando a camera")

    print("Julieta solicita a impressora")
    impressora.acquire()

    # Etapa Final que não consegui ser executada #
    print("Julieta termina de usar os recursos")
    camera.release()
    impressora.release()

def main():
    t_A = threading.Thread(target=romeo, args=[])
    t_B = threading.Thread(target=julieta, args=[])

    t_A.start()
    t_B.start()

    t_A.join()
    t_B.join()

main()