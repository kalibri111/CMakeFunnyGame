#!/usr/bin/python3
with open("index.h", "w+") as file:
    cpp_code = """#pragma once
    
    std::string GetHelloWorldMessage() {
        return "Hello, world!\\n";
    }
    """
    file.write(cpp_code)
