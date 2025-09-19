from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title> 

        </title>
    </head>
    <body>
        <h1 align="center">device specification-25017544</h1>
        <table border="2" cellspacing="5" cellpadding="10">
            <tr>
                <th>s.no.</th>
                <th>storage</th>
                <th>graphics card</th>
                <th>installed ram</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>954GB</td>
                <td>128MB</td>
                <td>16.0GB</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>130GB</td>
                <td>intel(r)</td>
                <td>5600mts</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>140GB</td>
                <td>i7</td>
                <td>7000mts</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>150GB</td>
                <td>i5</td>
                <td>8000mts</td>

                

            </tr>
            
        </table>
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()