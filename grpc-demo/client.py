import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    # Connect to server
    channel = grpc.insecure_channel('localhost:50051')

    # Create stub
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    # Send request
    response = stub.SayHello(
        hello_pb2.HelloRequest(message="Hello")
    )

    # Print response
    print("Server replied:", response.reply)

if __name__ == "__main__":
    run()