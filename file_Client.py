import grpc
import greeter_pb2 as pb2
import greeter_pb2_grpc as pb2_grpc
import os
import itertools
from datetime import datetime
import logging




CHUNK_SIZE = 1024 * 1024  # 1MB
LOG_FILE = 'C://Users//Admin//Downloads//log.txt'

# Configure logging
logging.basicConfig(filename='client_log.txt', level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')

def upload_files(stub, files_to_upload):
    for file in files_to_upload:
        try:
            upload_file(stub, file)
        except Exception as e:
            logging.error(f"Error uploading file {file}: {str(e)}")

def upload_file(stub, file_path):
    try:
        with open(file_path, 'rb') as file:
            first_chunk = pb2.Chunk(buffer=os.path.basename(file_path).encode('utf-8'))
            request_iterator = itertools.chain((first_chunk,), (pb2.Chunk(buffer=chunk) for chunk in iter(lambda: file.read(CHUNK_SIZE), b'')))
            response = stub.UploadFile(request_iterator)
        filename = os.path.basename(file_path)
        uploadedSize = int(response.message)
        sizeToUpload = os.path.getsize(file_path)
        if uploadedSize == sizeToUpload:
            print(f"File uploaded successfully. Server response: {response.message}")
            with open(LOG_FILE, 'a') as log_file:
                log_file.write(f"{datetime.now()} {os.path.getsize(filename)} {filename} Delivered\n")
        else:
            logging.error(f"Error uploading file {file_path}. Incomplete upload.")
    except Exception as e:
        logging.error(f"Error uploading file {file_path}: {str(e)}")

def download_file(stub, server_file_path, local_file_path):
    try:
        request = pb2.FileRequest(filename=server_file_path)
        response_iterator = stub.DownloadFile(request)
        with open(local_file_path, 'wb') as file:
            for chunk in response_iterator:
                file.write(chunk.buffer)
        print(f"File downloaded successfully to {local_file_path}")
    except Exception as e:
        logging.error(f"Error downloading file {server_file_path} to {local_file_path}: {str(e)}")

def run():
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = pb2_grpc.FileServiceStub(channel)

        # Example usage
        upload_file(stub, 'C://Users//Admin//Downloads//Onecourse_sessions.csv')
        files_to_upload = ['C://Users//Admin//Downloads//Onecourse_units.csv', 'C://Users//Admin//Downloads//Onecourse_sessions.csv']
        upload_files(stub, files_to_upload)
        download_file(stub, 'test.txt', 'C://Users//Admin//PycharmProjects//MetricsLocal//Test3.txt')

    except Exception as e:
        logging.error(f"Error in gRPC client: {str(e)}")

if __name__ == '__main__':
    run()
