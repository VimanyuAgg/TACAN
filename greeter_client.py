# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


# 169.254.172.23 - bhushan

# 169.254.179.83 - seema
# 169.254.28.146 - gurnoor
def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  # response = stub.SayHello(helloworld_pb2.HelloRequest(name='Vimanyu'))
  response = stub.Handshake(
    helloworld_pb2.RequestMessage(nodeId="12", destinationId="21", message="Hello Dear Server !"))
  response1 = stub.SendPacket(helloworld_pb2.RequestMessage(nodeId="12", destinationId="21",
                                                            message="Hello Dear Server Please forward my request!"))

  print("Greeter client received: " + response.ackMessage + " from Node ID :" + response.nodeId)
  print("Greeter client received from sendPacket: " + response1.ackMessage + " from Node ID :" + response1.nodeId)


if __name__ == '__main__':
  run()
