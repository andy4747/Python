#!/bin/python3
import os

resolv_path = "/etc/resolv.conf"

def change_dns(first, last):
    with open(resolv_path, "w") as file:
        file.write(f"nameserver  {first}\nnameserver  {last}\n")
        print("DNS changed")

def main():
    change_dns("1.1.1.1", "1.0.0.1")

if __name__ == "__main__":
    main()
