# a python replacement for the netcat tool

# import libraries
import sys
import socket
import getop
import threading
import subprocess

# define global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# create main function responsible for handling command line arguments and calling the rest of the functions

# Usage command to show user proper syntax
def usage():
    print("BHP Net Tool\n\nUsage: netcat-replacement.py -t target_host -p port\n"
    print("-l --listen                   -listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run      -execute the given file upon receiving a connection")
    print("-c --command                  -initialize a command shell")
    print("-u --upload-destination       -upon receiving a connection upload a file and write to [destination]\n\n\n")
    print("Examples\n")
    print("netcat-replacement.py -t 192.168.56.6 -p 5555 -l -c")
    print("netcat-replacement.py -t 192.168.56.4 -p 5555 -l -e=\"cat /etc/password\"")
    print("echo 'ABCDEFG' | ./netcat-replacement.py -t 192.168.56.5 -pm 135")
    sys.exit()

def client_sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to out target host
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)

        while True:
            # now wait for data back
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print response,   # I dont think this comma should be here but it was in the book
            #print(reponse)

            # wait for more input
            buffer = raw_input("")
            buffer += "\n"

            # send it off
            client.send(buffer)
    except:
        print("[*] Excpetion! Exiting")

        # tear down the connection
        client.close()

# creat the server loop function
def server_loop():
    global target

    # if no target is defined, we listen on all interfaces
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # spin off a thread to handle our new client
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def run_command():

    # trim the newline
    comand = command.rstrip()

    # run the command and get the output back
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=true)
    except:
        output = "Failed to execute command.\r\n"

    # send the output back to the client
    return(output)




# main command to run script
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    # if no argument is given, run usage funciton to show usage
    if not len(sys.argv[1:]):
        usage()

    # read the commanline options
    try:
        opts, args= getopt.getopt(sys.argv[1:],"hle:t:p:cu",["help","listen","execute","target","port","comand","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    # Target the argument option, and set the user input to the appropriate global variable
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--commandshelll"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    # are we going to listen or just send data from stdin?
    if not listen and len(target) and port > 0 :

        # read in teh buffer from the command line. This will block so send CTRL-D if not sending input to stdin
        buffer = sys.stdin.read()

        # send data off
        client_sender(buffer)

    # we are going to listen and potentially upload things, execute commands, and drop a shell back depending on out command line options above
    if listen:
        server_loop()

main()
