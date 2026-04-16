import grpc
import add_pb2
import add_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = add_pb2_grpc.AddServiceStub(channel)

    response = stub.AddNumbers(
        add_pb2.AddRequest(a=5,b=3)
    )

    print("result from server  :" ,response.result)

if __name__ == '__main__':
    run()


# python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. add.proto