#include <iostream>
#include <cctype>
#include "server_http.hpp"

#define PORT 8080

using HttpServer = SimpleWeb::Server<SimpleWeb::HTTP>;

/**
 * This is your handler
 */
void handler(std::shared_ptr<HttpServer::Response> response, std::shared_ptr<HttpServer::Request> request) {
  auto reqSize  = request->content.size();
  *response << "HTTP/1.1 200 OK\r\n"
            << "Content-Length: " << reqSize << "\r\n\r\n";
  constexpr auto bufSize = 1<<12;
  char buf[bufSize];
  while(!request->content.eof()){
    request->content.read(buf, bufSize);
    for(auto i=0;i<request->content.gcount();i++){
      *response << std::string{char(std::toupper(buf[i]))};
    }
  }
}

int main() {
  HttpServer server;
  server.config.port = PORT;
  server.resource["^.*$"]["POST"] = handler;
  server.on_error = [](std::shared_ptr<HttpServer::Request> /*request*/, const SimpleWeb::error_code & ec) {
    if (ec != boost::asio::error::eof) {
      std::cerr << ec.message() <<std::endl;
    }
  };
  std::cout << "starting http server on port "<<PORT<<std::endl;
  server.start();
}
