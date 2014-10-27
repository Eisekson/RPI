import socket
import sys
import pygame

import time





pygame.init()



display = pygame.display.set_mode((320,240),0,32)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 10000)
# server_address = ('192.168.1.105', 10000)
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

WHITE = (255,255,255)
BLACK = (0,0,0)

display.fill(WHITE)
pixArr = pygame.PixelArray(display)
pixArr[100][100] = BLACK
pixArr[101][101] = BLACK
pixArr[102][102] = BLACK

pygame.display.update()

while True:

    print >> sys.stderr, 'awiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >> sys.stderr, 'connection from', client_address
        i = 0
        step = 0
        strlen = 0
        strCount = 0
        colorImg = list()
        colorStr = ""

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(99999999)
            if len(data) == 0:
                break
            if step == 0:
                print data
                colorStr = ""
                strCount = 0
                connection.sendall("ok1")
                step += 1
            elif step == 1:
                print data
                connection.sendall("ok2")
                strlen = int(data)
                step += 1

            else:
                # print data
                strCount += len(data)
                connection.sendall(str(strCount))
                colorStr += data
                # print colorImg
                # print len(colorImg)
                # print len(pixArr)
                # print len(pixArr[0])
                # print len(pixArr[1])

                # for i in range(240):
                #     for j in range(320):
                #         pixArr[i][j+j*320] = (int(colorImg[k][0]),int(colorImg[k][1]),int(colorImg[k][2]))
                #         k+=1
                # pygame.display.update()

                if strCount >= strlen:
                    print "finish image send"
                    display.fill(WHITE)


                    colorImg = list(rgb.split(',') for rgb in colorStr.split('.'))
                    pixArr = pygame.PixelArray(display)
                    k = 0
                    for i in range(240):
                        for j in range(320):
                            pixArr[j][i] = pygame.Color(int(colorImg[k][0]),int(colorImg[k][1]),int(colorImg[k][2]))
                            k+=1
                    # print pixArr[0][0]
                    print colorImg[0][0]
                    print colorImg[0][1]
                    print colorImg[0][2]
                    pygame.display.update()
                    step = 0
                    time.sleep(5)
                    pygame.quit()
                    break

                    # print i
                    # i += 1
                    # if len(data) == 0:
                    # break
                    # # print >> sys.stderr, 'received "%s"' % data
                    # if data:
                    #     # print >> sys.stderr, 'sending data back to the client'
                    #     connection.sendall("su")
                    # else:
                    #     print >> sys.stderr, 'no more data from', client_address
                    # break

    finally:
        # Clean up the connection
        connection.close()
