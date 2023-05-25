# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import fileService_pb2 as proto_dot_fileService__pb2


class FileserviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.stream_unary(
                '/fileservice.Fileservice/UploadFile',
                request_serializer=proto_dot_fileService__pb2.FileData.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/fileservice.Fileservice/DownloadFile',
                request_serializer=proto_dot_fileService__pb2.FileInfo.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.FileData.FromString,
                )
        self.FileSearch = channel.unary_unary(
                '/fileservice.Fileservice/FileSearch',
                request_serializer=proto_dot_fileService__pb2.FileInfo.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )
        self.ReplicateFile = channel.stream_unary(
                '/fileservice.Fileservice/ReplicateFile',
                request_serializer=proto_dot_fileService__pb2.FileData.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )
        self.FileList = channel.unary_unary(
                '/fileservice.Fileservice/FileList',
                request_serializer=proto_dot_fileService__pb2.UserInfo.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.FileListResponse.FromString,
                )
        self.FileDelete = channel.unary_unary(
                '/fileservice.Fileservice/FileDelete',
                request_serializer=proto_dot_fileService__pb2.FileInfo.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )
        self.UpdateFile = channel.stream_unary(
                '/fileservice.Fileservice/UpdateFile',
                request_serializer=proto_dot_fileService__pb2.FileData.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )
        self.getClusterStats = channel.unary_unary(
                '/fileservice.Fileservice/getClusterStats',
                request_serializer=proto_dot_fileService__pb2.Empty.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ClusterStats.FromString,
                )
        self.getLeaderInfo = channel.unary_unary(
                '/fileservice.Fileservice/getLeaderInfo',
                request_serializer=proto_dot_fileService__pb2.ClusterInfo.SerializeToString,
                response_deserializer=proto_dot_fileService__pb2.ack.FromString,
                )


class FileserviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicateFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getClusterStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getLeaderInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileserviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=proto_dot_fileService__pb2.FileData.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=proto_dot_fileService__pb2.FileInfo.FromString,
                    response_serializer=proto_dot_fileService__pb2.FileData.SerializeToString,
            ),
            'FileSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.FileSearch,
                    request_deserializer=proto_dot_fileService__pb2.FileInfo.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
            'ReplicateFile': grpc.stream_unary_rpc_method_handler(
                    servicer.ReplicateFile,
                    request_deserializer=proto_dot_fileService__pb2.FileData.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
            'FileList': grpc.unary_unary_rpc_method_handler(
                    servicer.FileList,
                    request_deserializer=proto_dot_fileService__pb2.UserInfo.FromString,
                    response_serializer=proto_dot_fileService__pb2.FileListResponse.SerializeToString,
            ),
            'FileDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.FileDelete,
                    request_deserializer=proto_dot_fileService__pb2.FileInfo.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
            'UpdateFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UpdateFile,
                    request_deserializer=proto_dot_fileService__pb2.FileData.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
            'getClusterStats': grpc.unary_unary_rpc_method_handler(
                    servicer.getClusterStats,
                    request_deserializer=proto_dot_fileService__pb2.Empty.FromString,
                    response_serializer=proto_dot_fileService__pb2.ClusterStats.SerializeToString,
            ),
            'getLeaderInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getLeaderInfo,
                    request_deserializer=proto_dot_fileService__pb2.ClusterInfo.FromString,
                    response_serializer=proto_dot_fileService__pb2.ack.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fileservice.Fileservice', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Fileservice(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/fileservice.Fileservice/UploadFile',
            proto_dot_fileService__pb2.FileData.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/fileservice.Fileservice/DownloadFile',
            proto_dot_fileService__pb2.FileInfo.SerializeToString,
            proto_dot_fileService__pb2.FileData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fileservice.Fileservice/FileSearch',
            proto_dot_fileService__pb2.FileInfo.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicateFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/fileservice.Fileservice/ReplicateFile',
            proto_dot_fileService__pb2.FileData.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fileservice.Fileservice/FileList',
            proto_dot_fileService__pb2.UserInfo.SerializeToString,
            proto_dot_fileService__pb2.FileListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fileservice.Fileservice/FileDelete',
            proto_dot_fileService__pb2.FileInfo.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/fileservice.Fileservice/UpdateFile',
            proto_dot_fileService__pb2.FileData.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getClusterStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fileservice.Fileservice/getClusterStats',
            proto_dot_fileService__pb2.Empty.SerializeToString,
            proto_dot_fileService__pb2.ClusterStats.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getLeaderInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fileservice.Fileservice/getLeaderInfo',
            proto_dot_fileService__pb2.ClusterInfo.SerializeToString,
            proto_dot_fileService__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)