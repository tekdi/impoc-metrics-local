# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgreeter.proto\"\x1f\n\x0b\x46ileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"\x1f\n\x0c\x46ileResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x05\x43hunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\"\x1c\n\x08\x46ileList\x12\x10\n\x08\x66ileName\x18\x03 \x03(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyRequest2\xa9\x01\n\x07Greeter\x12\x1e\n\nUploadFile\x12\x06.Chunk\x1a\x06.Reply(\x01\x12&\n\x0c\x44ownloadFile\x12\x0c.FileRequest\x1a\x06.Chunk0\x01\x12.\n\x12getFilesToDownload\x12\r.EmptyRequest\x1a\t.FileList\x12&\n\x08sayHello\x12\r.HelloRequest\x1a\x0b.HelloReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_FILEREQUEST']._serialized_start=17
  _globals['_FILEREQUEST']._serialized_end=48
  _globals['_FILERESPONSE']._serialized_start=50
  _globals['_FILERESPONSE']._serialized_end=81
  _globals['_REPLY']._serialized_start=83
  _globals['_REPLY']._serialized_end=107
  _globals['_CHUNK']._serialized_start=109
  _globals['_CHUNK']._serialized_end=132
  _globals['_FILELIST']._serialized_start=134
  _globals['_FILELIST']._serialized_end=162
  _globals['_HELLOREQUEST']._serialized_start=164
  _globals['_HELLOREQUEST']._serialized_end=192
  _globals['_HELLOREPLY']._serialized_start=194
  _globals['_HELLOREPLY']._serialized_end=223
  _globals['_EMPTYREQUEST']._serialized_start=225
  _globals['_EMPTYREQUEST']._serialized_end=239
  _globals['_GREETER']._serialized_start=242
  _globals['_GREETER']._serialized_end=411
# @@protoc_insertion_point(module_scope)
