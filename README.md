# EX01 Developing a Simple Webserver
## Date:05.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot (42).png>) ![alt text](<Screenshot (43).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
