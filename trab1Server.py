import time

import rpyc


class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_get_answer(self):  # este é um método exposto
        return 42

    exposed_the_real_answer_though = 43  # este é um atributo exposto

    def get_question(self):  # este método não é exposto
        return "Qual é  a cor do cavalo branco de Napoleão?"

    def get_value(self, n):
        ret = 0
        for i in n:
            ret += i
        return ret

    def exposed_get_sum(self, n):
        start = time.time()
        array = []
        for i in range(0, n):
            array.append(i)
        sum_total = self.get_value(array)
        end = time.time()
        print(end - start)
        return sum_total


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()



