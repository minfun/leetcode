from multiprocessing import Process, Queue, Pipe


def f(q):
    q.put([42, None, 'hello'])


def f2(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()

    parent_conn, chile_conn = Pipe()
    p2 = Process(target=f2, args=(chile_conn,))
    p2.start()
    print(parent_conn.recv())
    p2.join()
