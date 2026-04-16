import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

# Implement the service
class HelloService(hello_pb2_grpc.HelloServiceServicer):

    def SayHello(self, request, context):
        print("Client sent:", request.message)

        # Send response
        return hello_pb2.HelloResponse(
            reply="Hello World"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

    hello_pb2_grpc.add_HelloServiceServicer_to_server(
        HelloService(), server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server running...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()