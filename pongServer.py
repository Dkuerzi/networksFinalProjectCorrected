import socket
from _thread import *
import pickle

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

#  Created list of player locations
players = [[350, 0], [-350, 0]]


def threaded_client(conn, player):
    # send the starting position to the client
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # get a position from the client
            data = pickle.loads(conn.recv(2048))
            # updates the positoon in the array for the given player
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    # Setting the reply to the opposing players coordinates
                    reply = players[0]
                else:
                    reply = players[1]

            # send out the position of the opposing player to all of the clients
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    # Accepts incoming connections
    conn, addr = s.accept()
    print("Connected to:", addr)
    # Starts a thread to constantly send and receive new positions
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
