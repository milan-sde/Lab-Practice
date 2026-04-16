import grpc
import add_pb2
import add_pb2_grpc
from concurrent import futures


class AddService(add_pb2_grpc.AddServiceServicer):
    def AddNumbers(self,request,context):
        print("Received : ",request.a,request.b)
        ans = request.a + request.b
        return add_pb2.AddResponse(result=ans)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

    add_pb2_grpc.add_AddServiceServicer_to_server(
        AddService(),
        server
    )

    server.add_insecure_port('[::]:50051')
    server.start()

    print("server running")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    