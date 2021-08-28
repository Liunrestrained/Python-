class BaseServer:
    def serve_forever(self, poll_interval=0.5):
        self._handle_request_noblock()

    def _handle_request_noblock(self):
        self.process_request(request, client_address)

    def process_request(self, request, client_address):
        pass


class TCPServer(BaseServer):
    pass


class ThreadingMixIn:
    def process_request(self, request, client_address):
        pass


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


obj = ThreadingTCPServer()
obj.serve_forever()
