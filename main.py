def main():
    print("Hello from test-remote-server-mcp!")
from fastmcp import FastMCP
import random
import json
#create the fastmcp server instance
mcp=FastMCP("Simple calculator Server")
#Tool: add two number
@mcp.tool
def add(a:int,b:int)->int:
    """Add two numbers together.
    Args:
       a:First Number
       b:Second number
    Returns:
    The sum of a and b
    """
    return a+b
@mcp.tool
def Multiply(a:int,b:int)->int:
    """Multiply two numbers together.
    Args:
       a:First Number
       b:Second number
    Returns:
    The multiply of a and b
    """
    return a*b
#resource:server information
@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server."""
    info={
        "name":"simple calculator server",
        "version":"1.0.0",
        "description":"A basic mcp server with math tools",
        "tools":["add","Multiply"],
        "author":"Your name"
    }
    return json.dumps(info,indent=2)



    


if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8000)
    #main()
