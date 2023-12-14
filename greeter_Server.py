import grpc
import os
from concurrent import futures
import greeter_pb2 as pb2
import greeter_pb2_grpc as pb2_grpc
from datetime import datetime

UPLOADS_FILE = 'uploaded_files.txt'
FILES_TO_UPLOAD_DIR = 'UploadedFilesOnRouter'
CHUNK_SIZE = 1024 * 1024  # 1MB

class Greeter(pb2_grpc.GreeterServicer):

    def save_chunks_to_file(self, chunks, filename):
        with open(filename, 'wb') as f:
            for chunk in chunks:
                f.write(chunk.buffer)

    def UploadFile(self, request_iterator, context):
        first_chunk = next(request_iterator)
        filename = first_chunk.buffer.decode('utf-8')
        file_path = os.path.join(FILES_TO_UPLOAD_DIR, filename)
        print(file_path)

        self.save_chunks_to_file(request_iterator, file_path)

        response = pb2.Reply()
        response.message = f"{os.path.getsize(file_path)}"
        # Record upload in a file
        with open(UPLOADS_FILE, 'a') as file:
             file.write(f"{context.peer()} {datetime.now()} {os.path.getsize(file_path)} {filename}\n")

        return response

    def DownloadFile(self, request, context):
            print(request.filename)
            file_name = request.filename
            # print(file_name)
            file_path = os.path.join(os.path.dirname(__file__),FILES_TO_UPLOAD_DIR, file_name)
            print("file_path_dir")
            print(os.path.join(os.path.dirname(__file__)))

            # Now, use file_path in your script
            # file_path = 'C://Users//Admin//PycharmProjects//MetricsLocal//test.txt'
            try:
                with open(file_path, 'rb') as f:
                    while True:
                        print("inside while")
                        piece = f.read(CHUNK_SIZE)
                        if not piece:
                            print("inside if")
                            break  # Exit the loop when there are no more chunks
                        yield pb2.Chunk(buffer=piece)
            except FileNotFoundError:
                # Log the error or send an appropriate error response
                print("FileNotFound")
                context.abort(grpc.StatusCode.NOT_FOUND, "File not found")
            except Exception as e:
                # Log the error or handle it based on your requirements
                context.abort(grpc.StatusCode.INTERNAL, f"Error during file download: {str(e)}")
                print(str(e))
    def getFilesToDownload(self,request,context):
        # listOfFiles = ['Onecourse_units.csv','Onecourse_sessions.csv']
        print("inside server getfilesToDownload method")
        print(os.listdir(FILES_TO_UPLOAD_DIR))
        listOfFiles =  [f for f in os.listdir(FILES_TO_UPLOAD_DIR) if os.path.isfile(os.path.join(FILES_TO_UPLOAD_DIR, f))]
        fileNames = pb2.FileList(fileName=listOfFiles)
        print("filename.fileName")
        print(fileNames.fileName)
        print("filenames")
        print(fileNames)
        # fileList.fileName.extend(listOfFiles)
        return fileNames
    def sayHello(self, request, context):
        print("Inside Say Hello Method")
        response = pb2.HelloReply();
        response.message = f"Hello {request.name}"
        return response
def serve():
    print("Server Running")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
