import pytest
from unittest.mock import MagicMock, patch
from file_Client import upload_file, upload_files, download_file, run



@pytest.fixture
def grpc_stub():
    return MagicMock()

# Positive test cases

def test_positive_upload_file(grpc_stub):
    with patch('grpc.insecure_channel'):
        grpc_stub.UploadFile.return_value = MagicMock(message='1024')

        upload_file(grpc_stub, 'test_file.txt')

        grpc_stub.UploadFile.assert_called_once()
        grpc_stub.UploadFile.assert_called_with(MagicMock())

def test_positive_upload_files(grpc_stub):
    with patch('grpc.insecure_channel'):
        grpc_stub.UploadFile.return_value = MagicMock(message='1024')

        upload_files(grpc_stub, ['file1.txt', 'file2.txt'])

        assert grpc_stub.UploadFile.call_count == 2

def test_positive_download_file(grpc_stub):
    with patch('grpc.insecure_channel'):
        grpc_stub.DownloadFile.return_value = iter([MagicMock(buffer=b'chunk1'), MagicMock(buffer=b'chunk2')])

        download_file(grpc_stub, 'server_file.txt', 'local_file.txt')

        grpc_stub.DownloadFile.assert_called_once()
        grpc_stub.DownloadFile.assert_called_with(MagicMock(filename='server_file.txt'))

# Negative test cases

def test_negative_upload_file_invalid_file(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(FileNotFoundError):
            upload_file(grpc_stub, 'nonexistent_file.txt')

def test_negative_upload_file_empty_file(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(ValueError):
            upload_file(grpc_stub, 'empty_file.txt')

def test_negative_upload_files_empty_list(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(ValueError):
            upload_files(grpc_stub, [])

def test_negative_upload_files_invalid_file(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(FileNotFoundError):
            upload_files(grpc_stub, ['nonexistent_file.txt', 'existing_file.txt'])

def test_negative_download_file_invalid_server_path(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(ValueError):
            download_file(grpc_stub, '../server_file.txt', 'local_file.txt')

def test_negative_download_file_invalid_local_path(grpc_stub):
    with patch('grpc.insecure_channel'):
        with pytest.raises(ValueError):
            download_file(grpc_stub, 'server_file.txt', '/invalid/path/local_file.txt')

def test_negative_download_file_server_error(grpc_stub):
    with patch('grpc.insecure_channel'):
        grpc_stub.DownloadFile.side_effect = grpc.RpcError('Server error')
        with pytest.raises(Exception):
            download_file(grpc_stub, 'server_file.txt', 'local_file.txt')
