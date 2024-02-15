import grpc
import sys

def main():
    mod = grpc.protos('schema.proto')
    mod2 = grpc.protos('schema2.proto')

if __name__ == "__main__":
    main()